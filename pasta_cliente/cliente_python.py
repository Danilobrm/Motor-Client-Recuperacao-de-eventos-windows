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
    
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                while True:
                    ipv4_address = socket.gethostbyname(socket.gethostname())
                    current_titles = get_active_window_titles()
                    
                    if current_titles:
                        await enviar_informacoes(websocket, Info(ipv4_address, current_titles, ""))

                    urls = get_chrome_url()
                    if urls:
                        await enviar_informacoes(websocket, Info(ipv4_address, urls, ""))

                    # Verificar o tempo de inatividade do teclado e do mouse
                    if keyboard_idle_time >= 15 or mouse_idle_time >= 15:
                        await enviar_informacoes(websocket, Info(ipv4_address, [], f"Teclado: {keyboard_idle_time} segundos, Mouse: {mouse_idle_time} segundos"))

                    # Incrementar o tempo de inatividade
                    keyboard_idle_time += 2
                    mouse_idle_time += 2

                    await asyncio.sleep(2)  # Ajuste o intervalo de tempo conforme necessário
        except (websockets.exceptions.ConnectionClosedError, websockets.exceptions.InvalidURI, websockets.exceptions.InvalidHandshake, TimeoutError) as e:
            print(f"Erro na conexão: {e}")
            print("Tentando reconectar em 5 segundos...")
            await asyncio.sleep(5)  # Aguarde antes de tentar reconectar

def main():
    asyncio.run(monitorar_e_enviar())

if __name__ == '__main__':
    main()
