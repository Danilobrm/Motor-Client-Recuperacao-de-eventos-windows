import asyncio
import websockets
import pygetwindow as gw
import re
import socket
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput import mouse, keyboard
import getpass

# Variáveis globais para rastrear o tempo de inatividade do teclado e do mouse
keyboard_idle_time = 0
mouse_idle_time = 0

class Info:
    def __init__(self, ipv4_address, titles, inactivity):
        self.ipv4_address = ipv4_address
        self.titles = titles  # titles é agora uma lista
        self.inactivity = inactivity

async def enviar_informacoes(websocket, info):
    username = getpass.getuser()
    titles_str = ', '.join(info.titles)  # Converte a lista de títulos em uma string
    await websocket.send(f"{username}: {info.ipv4_address}, {titles_str}, {info.inactivity}")

def get_active_window_titles():
    windows = gw.getWindowsWithTitle('')
    titles = [window.title for window in windows if window.isActive]
    return titles

def get_chrome_url():
    active_window_titles = get_active_window_titles()
    urls = []
    for title in active_window_titles:
        if 'Google Chrome' in title:
            match = re.search(r'https?://[^\s]+', title)
            if match:
                urls.append(match.group(0))
    return urls

async def monitorar_e_enviar():
    global keyboard_idle_time, mouse_idle_time
    
    uri = 'ws://Administrador:8080'  # Substitua pelo endereço IP do servidor
    
    mouse_controller = MouseController()
    keyboard_controller = KeyboardController()
    
    def on_keyboard_activity(event):
        global keyboard_idle_time
        keyboard_idle_time = 0
    
    def on_mouse_activity(x, y):
        global mouse_idle_time
        mouse_idle_time = 0
    
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
                        await enviar_informacoes(websocket, Info(ipv4_address, "Teclado: {keyboard_idle_time} segundos, Mouse: {mouse_idle_time} segundos"))

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
