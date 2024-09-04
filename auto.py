import pyautogui
import time
from PIL import ImageGrab
import threading
import keyboard

# Variável global para controlar a interrupção
stop_thread = False

def check_for_esc():
    global stop_thread
    while True:
        if keyboard.is_pressed('esc'):
            stop_thread = True
            print("Automação interrompida pelo usuário.")
            break
        time.sleep(0.1)

def find_color_and_click2(target_rgb, tolerance=10):
    global stop_thread
    if stop_thread:
        return

    screen = ImageGrab.grab()
    width, height = screen.size

    for x in range(width):
        for y in range(height):
            if stop_thread:
                return

            color = screen.getpixel((x, y))
            if all(abs(color[i] - target_rgb[i]) <= tolerance for i in range(3)):
                pyautogui.click(x, y)
                print(f'Clicked at ({x}, {y})')
                return
    print("Cor não encontrada na tela.")

def run_automation():
    global stop_thread

    if stop_thread:
        return

    # Aguarda 3 segundos antes de iniciar a automação
    print("Aguardando 3 segundos para iniciar a automação...")
    time.sleep(3)

    if stop_thread:
        return

    # Simula pressionar Ctrl + C (Copiar)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    if stop_thread:
        return

    # Clica na coordenada (674, 22)
    pyautogui.click(674, 22)
    time.sleep(1)

    # Clica na coordenada (384, 449)
    pyautogui.click(384, 449)
    time.sleep(1)

    # Clica na coordenada (550, 824)
    pyautogui.click(550, 824)
    time.sleep(1)

    # Simula pressionar Ctrl + A (Selecionar tudo)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)

    # Simula pressionar Ctrl + V (Colar)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    if stop_thread:
        return

    # Pressiona Enter
    pyautogui.press('enter')
    time.sleep(2)

    if stop_thread:
        return

    # Clica na coordenada (437, 23)
    pyautogui.click(437, 23)
    time.sleep(1)

    # Pressiona duas vezes a tecla da seta direita
    pyautogui.press('right', presses=2, interval=0.5)
    time.sleep(1)

    # Simula pressionar Ctrl + C (Copiar)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    if stop_thread:
        return

    # Clica na coordenada (674, 22)
    pyautogui.click(674, 22)
    time.sleep(1)

    # Simula pressionar Ctrl + F (Procurar)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)

    # Simula pressionar Ctrl + V (Colar)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # Define a cor que você quer procurar (em RGB)
    target_color = (255, 150, 50)  # Exemplo: Cor vermelha

    # Define a área da tela para procurar a cor (x1, y1, x2, y2)
    region = (0, 0, 1920, 1080)  # Área completa da tela

    def find_color_and_click(target_color, region):
        global stop_thread
        if stop_thread:
            return

        # Captura a área especificada da tela
        screenshot = ImageGrab.grab(bbox=region)

        # Percorre os pixels da imagem capturada
        for x in range(screenshot.width):
            for y in range(screenshot.height):
                if stop_thread:
                    return

                r, g, b = screenshot.getpixel((x, y))
                if (r, g, b) == target_color:
                    # Ajusta as coordenadas para a tela
                    screen_x = x + region[0]
                    screen_y = y + region[1]

                    # Clica na posição da cor encontrada
                    pyautogui.click(screen_x, screen_y)
                    print(f"Cor encontrada e clicada em: ({screen_x}, {screen_y})")
                    return
        print("Cor não encontrada na área especificada.")

    # Aguarda 2 segundos antes de começar a busca pela cor
    time.sleep(2)

    # Executa a função de busca e clique
    find_color_and_click(target_color, region)

    if stop_thread:
        return

    # Mantém pressionada a tecla END por 2 segundos
    time.sleep(2)
    pyautogui.keyDown('end')
    time.sleep(2)
    pyautogui.keyUp('end')
    time.sleep(1)

    if stop_thread:
        return

    # Substitui a coordenada clicada anteriormente pela função find_color_and_click2
    time.sleep(1)
    target_color2 = (0, 117, 255)
    find_color_and_click2(target_color2)

    if stop_thread:
        return

    # Simula pressionar Ctrl + F (Procurar)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write('Salvar')
    time.sleep(1)

    # Executa a função de busca e clique
    find_color_and_click(target_color, region)
    time.sleep(2)
    pyautogui.click(1277, 204)
    time.sleep(1)

    # Simula pressionar Ctrl + F (Procurar)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)

    pyautogui.write('Voltar')
    find_color_and_click(target_color, region)
    time.sleep(2)
    pyautogui.click(437, 23)
    time.sleep(1.5)

    if stop_thread:
        return

    # Pressiona a tecla da seta direita 3 vezes
    pyautogui.press('right', presses=3, interval=0.5)
    time.sleep(0.5)

    if stop_thread:
        return

    # Pressiona a tecla "x"
    pyautogui.press('x')
    time.sleep(0.5)

    # Pressiona a tecla para baixo
    pyautogui.press('down')
    time.sleep(0.5)

    # Pressiona a tecla da seta para esquerda 5 vezes
    pyautogui.press('left', presses=5, interval=0.3)

    print("Automação concluída.")

# Inicia a thread para monitorar a tecla "Esc"
esc_thread = threading.Thread(target=check_for_esc)
esc_thread.start()

# Loop principal para repetir a automação 2 vezes
for i in range(2):
    if stop_thread:
        break
    run_automation()
    print(f"Iteração {i + 1} concluída.")

print("Programa finalizado.")
