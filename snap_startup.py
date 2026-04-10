#!/usr/bin/env python3
"""
Programa simples de startup - Pressione ESPAÇO para ativar
"""

import pyttsx3
import subprocess
import time
from datetime import datetime

def get_greeting():
    """Retorna saudação baseada na hora"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Bom dia!"
    elif 12 <= hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def speak(text):
    """Fala o texto"""
    print(f"[Falando] {text}")
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
    except:
        try:
            subprocess.run(['espeak', text], timeout=5)
        except:
            print("Erro ao falar, mas continuando...")

def open_apps():
    """Abre Brave e VSCode"""
    print("[Abrindo] Brave...")
    for cmd in ['brave-browser', 'brave']:
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            break
        except:
            pass

    time.sleep(1)

    print("[Abrindo] VSCode...")
    try:
        subprocess.Popen('code', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        print("VSCode não encontrado")

def main():
    print("=" * 50)
    print("🚀 SNAP STARTUP")
    print("=" * 50)
    print("\nPressione ESPAÇO para ativar")
    print("Pressione ESC para sair\n")

    try:
        import keyboard

        while True:
            if keyboard.is_pressed('space'):
                print("\n✨ [ATIVADO!]\n")
                greeting = get_greeting()
                speak(greeting)
                open_apps()
                print("\n✓ Programa finalizado!")
                break

            if keyboard.is_pressed('esc'):
                print("\nSaindo...")
                break

            time.sleep(0.1)

    except ImportError:
        print("❌ Biblioteca keyboard não instalada\n")
        print("Execute: pip install keyboard\n")
        print("Ou use a versão com input:")
        input("Pressione ENTER para ativar o programa: ")
        greeting = get_greeting()
        speak(greeting)
        open_apps()
        print("\n✓ Programa finalizado!")

if __name__ == "__main__":
    main()
