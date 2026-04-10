#!/usr/bin/env python3
"""
Programa de startup com detecção de movimento de mão (alternativa simplificada).
Quando detecta movimento rápido de mão, o programa:
1. Verifica a hora
2. Faz uma saudação apropriada (Bom dia, Boa tarde, Boa noite)
3. Abre Brave e VSCode
4. Encerra o programa
"""

import cv2
import pyttsx3
import subprocess
import time
import sys
from datetime import datetime
import numpy as np

# Inicializar text-to-speech
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    VOICE_AVAILABLE = True
except Exception as e:
    print(f"⚠️ Aviso: Síntese de voz não disponível: {e}")
    VOICE_AVAILABLE = False

def get_greeting():
    """Retorna a saudação apropriada baseada na hora"""
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return "Bom dia!"
    elif 12 <= hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def speak(text):
    """Fala o texto usando síntese de voz"""
    print(f"[Falando] {text}")
    if VOICE_AVAILABLE:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Erro ao falar: {e}")
    else:
        # Usar espeak diretamente se pyttsx3 não funcionar
        try:
            subprocess.run(['espeak', text], timeout=5)
        except Exception as e:
            print(f"Erro ao usar espeak: {e}")

def open_applications():
    """Abre Brave e VSCode"""
    print("[Abrindo] Brave...")
    for cmd in ['brave-browser', 'brave']:
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            break
        except FileNotFoundError:
            continue
    else:
        print("Aviso: Brave não encontrado no sistema")

    time.sleep(1)

    print("[Abrindo] VSCode...")
    try:
        subprocess.Popen('code', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Aviso: VSCode não encontrado no sistema")

def detect_hand_motion(prev_frame, curr_frame, threshold=1000000):
    """
    Detecta movimento significativo na imagem (possível snap).
    Usa diferença de frames como indicador.
    """
    if prev_frame is None:
        return False

    # Converter para escala de cinza
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

    # Calcular diferença
    frame_diff = cv2.absdiff(prev_gray, curr_gray)

    # Aplicar threshold
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Contar pixels significativos
    motion_count = np.sum(thresh > 0)

    return motion_count > threshold

def main():
    """Função principal"""
    print("🎯 Snap Startup - Versão Alternativa (Detecção de Movimento)")
    print("Aproxime a mão da câmera e faça um movimento rápido para ativar!")
    print("Pressione ESC para sair.\n")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Erro: Não foi possível acessar a câmera")
        sys.exit(1)

    prev_frame = None
    motion_count = 0
    motion_threshold = 5  # Detectar movimento 5 frames seguidos

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Erro ao ler frame da câmera")
                break

            # Espelhar a imagem
            frame = cv2.flip(frame, 1)

            # Detectar movimento
            if detect_hand_motion(prev_frame, frame):
                motion_count += 1
                print(f"🤚 Movimento detectado! ({motion_count}/{motion_threshold})", end='\r')

                if motion_count >= motion_threshold:
                    print("\n\n✨ [SNAP DETECTADO!]")
                    cap.release()
                    cv2.destroyAllWindows()

                    # Saudação
                    greeting = get_greeting()
                    speak(greeting)

                    # Abrir aplicativos
                    open_applications()

                    print("✓ Programa finalizado!")
                    return
            else:
                motion_count = 0

            # Mostrar frame
            cv2.imshow('Snap Detector', frame)
            prev_frame = frame.copy()

            # ESC para sair
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
