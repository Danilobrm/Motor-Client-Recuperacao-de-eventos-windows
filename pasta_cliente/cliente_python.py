import asyncio
import websockets
import pygetwindow as gw
import socket
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput import mouse, keyboard
import json
import getpass
import time

# Global variables to track keyboard and mouse idle time
keyboard_idle_time = 0
mouse_idle_time = 0
idle_time = 0
last_keyboard_activity = time.time()
last_mouse_activity = time.time()
last_active_title = None
last_active_program = None
last_idle_time = 0

class Info:
    def __init__(self, ipv4_address, username):
        self.user = {
            'ipv4_address': ipv4_address,
            'username': username,
        }
        self.programs = {}
        self.idle_time = 0

    def update_active_program_title(self, program, title):
        current_time = time.time()
        if program not in self.programs:
            self.programs[program] = {'titles': [title], 'start_time': current_time, 'total_time': 0}
        else:
            if self.programs[program]['titles'][-1] != title:
                self.programs[program]['titles'].append(title)
            self.programs[program]['total_time'] += current_time - self.programs[program]['start_time']
            self.programs[program]['start_time'] = current_time

    def to_dict(self):
        return {
            'user': self.user,
            'programs': self.programs,
            'idle_time': self.idle_time
        }

def get_active_window_title():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title
    except Exception as e:
        print(f"Error getting active window title: {e}")
    return None

async def enviar_informacoes(websocket, info):
    info_dict = info.to_dict()
    info_json = json.dumps(info_dict)
    print(info_json)
    await websocket.send(info_json)

async def monitorar_e_enviar():
    global keyboard_idle_time, mouse_idle_time, idle_time, last_keyboard_activity, last_mouse_activity, last_active_title, last_active_program, last_idle_time
    
    server_ip = 'localhost'  # Replace with your server's IP address
    port = 8080
    username = getpass.getuser()
    ipv4_address = socket.gethostbyname(socket.gethostname())
    uri = f'ws://{server_ip}:{port}'
    
    mouse_controller = MouseController()
    keyboard_controller = KeyboardController()
    
    def on_keyboard_activity(event):
        global last_keyboard_activity
        last_keyboard_activity = time.time()
    
    def on_mouse_activity(x, y):
        global last_mouse_activity
        last_mouse_activity = time.time()
    
    keyboard_listener = keyboard.Listener(on_press=on_keyboard_activity)
    mouse_listener = mouse.Listener(on_move=on_mouse_activity)
    
    keyboard_listener.start()
    mouse_listener.start()
    
    try:
        info = Info(ipv4_address, username)
        async with websockets.connect(uri) as websocket:
            # Send user data upon connection
            active_title = get_active_window_title()
            if active_title:
                program, title = active_title.rsplit(' - ', 1) if ' - ' in active_title else (active_title, "")
                info.update_active_program_title(program, title)
            await enviar_informacoes(websocket, info)
                    
            while True:
                active_title = get_active_window_title()

                current_time = time.time()
                keyboard_idle_time = current_time - last_keyboard_activity
                mouse_idle_time = current_time - last_mouse_activity

                if keyboard_idle_time >= 3 and mouse_idle_time >= 3:
                    idle_time += 1
                else:
                    idle_time = 0

                info.idle_time = idle_time

                if active_title != last_active_title or idle_time != last_idle_time:
                    last_active_title = active_title
                    last_idle_time = idle_time
                    if active_title:
                        program, title = active_title.rsplit(' - ', 1) if ' - ' in active_title else (active_title, "")
                        info.update_active_program_title(program, title)
                    await enviar_informacoes(websocket, info)

                await asyncio.sleep(1)  # Adjust time interval as needed
    except (websockets.exceptions.ConnectionClosedError, websockets.exceptions.InvalidURI, websockets.exceptions.InvalidHandshake, TimeoutError) as e:
        print(f"Error connecting: {e}")
        print("Attempting to reconnect in 5 seconds...")
        await asyncio.sleep(5)  # Wait before attempting to reconnect
    finally:
        keyboard_listener.stop()
        mouse_listener.stop()

def main():
    asyncio.run(monitorar_e_enviar())

if __name__ == '__main__':
    main()
