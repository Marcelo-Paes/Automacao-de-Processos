import pyautogui
import time
from PIL import ImageGrab
import threading
import keyboard

# Variável global para controlar a interrupção da automação
stop_thread = False

# Função para monitorar a tecla "Esc" e interromper a automação
def check_for_esc():
    global stop_thread
    while True:
        if keyboard.is_pressed('esc'):
            stop_thread = True
            print("Automação interrompida pelo usuário.")
            break
        time.sleep(0.1)

# Função para encontrar uma cor específica na tela e clicar nela
def find_color_and_click2(target_rgb, tolerance=10):
    global stop_thread
    if stop_thread:
        return

    # Captura a tela inteira
    screen = ImageGrab.grab()
    width, height = screen.size

    # Varre os pixels da tela procurando pela cor alvo
    for x in range(width):
        for y in range(height):
            if stop_thread:
                return

            color = screen.getpixel((x, y))
            # Verifica se a cor do pixel está dentro da tolerância definida
            if all(abs(color[i] - target_rgb[i]) <= tolerance for i in range(3)):
                pyautogui.click(x, y)
                print(f'Clicked at ({x}, {y})')
                return
    print("Cor não encontrada na tela.")

# Função principal que executa a automação
def run_automation():
    global stop_thread

    if stop_thread:
        return

    # Aguarda 3 segundos antes de iniciar a automação
    print("Aguardando 3 segundos para iniciar a automação...")
    time.sleep(3)

    if stop_thread:
        return

    # Copia (Ctrl + C) e realiza uma sequência de cliques e atalhos de teclado
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    pyautogui.click(674, 22)
    time.sleep(1)

    pyautogui.click(384, 449)
    time.sleep(1)

    pyautogui.click(550, 824)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    if stop_thread:
        return

    pyautogui.press('enter')
    time.sleep(2)

    if stop_thread:
        return

    pyautogui.click(437, 23)
    time.sleep(1)

    pyautogui.press('right', presses=2, interval=0.5)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    pyautogui.click(674, 22)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # Define a cor que você quer procurar (em RGB)
    target_color = (255, 150, 50)  # Exemplo: Cor laranja

    # Define a área da tela para procurar a cor
    region = (0, 0, 1920, 1080)  # Área completa da tela

    # Função para procurar a cor dentro de uma área específica da tela
    def find_color_and_click(target_color, region):
        global stop_thread
        if stop_thread:
            return

        # Captura a área especificada da tela
        screenshot = ImageGrab.grab(bbox=region)

        # Varre os pixels da área capturada
        for x in range(screenshot.width):
            for y in range(screenshot.height):
                if stop_thread:
                    return

                r, g, b = screenshot.getpixel((x, y))
                if (r, g, b) == target_color:
                    # Ajusta as coordenadas para a tela inteira
                    screen_x = x + region[0]
                    screen_y = y + region[1]
                    pyautogui.click(screen_x, screen_y)
                    print(f"Cor encontrada e clicada em: ({screen_x}, {screen_y})")
                    return
        print("Cor não encontrada na área especificada.")

    # Aguarda 2 segundos antes de começar a busca pela cor
    time.sleep(2)

    # Executa a busca e clique na cor definida
    find_color_and_click(target_color, region)

    if stop_thread:
        return

    # Mantém pressionada a tecla "End" por 2 segundos
    time.sleep(2)
    pyautogui.keyDown('end')
    time.sleep(2)
    pyautogui.keyUp('end')
    time.sleep(1)

    if stop_thread:
        return

    # Procura e clica em outra cor definida na tela
    time.sleep(1)
    target_color2 = (0, 117, 255)  # Exemplo: Cor azul
    find_color_and_click2(target_color2)

    if stop_thread:
        return

    # Busca e clica em botões "Salvar" e "Voltar" na tela
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write('Salvar')
    time.sleep(1)

    find_color_and_click(target_color, region)
    time.sleep(2)
    pyautogui.click(1277, 204)
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)

    pyautogui.write('Voltar')
    find_color_and_click(target_color, region)
    time.sleep(2)
    pyautogui.click(437, 23)
    time.sleep(1.5)

    if stop_thread:
        return

    # Navega no sistema pressionando teclas de seta e outros comandos
    pyautogui.press('right', presses=3, interval=0.5)
    time.sleep(0.5)

    if stop_thread:
        return

    pyautogui.press('x')
    time.sleep(0.5)

    pyautogui.press('down')
    time.sleep(0.5)

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
