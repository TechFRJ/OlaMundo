#!/usr/bin/env python3
"""
Programa de startup com detecção de gesto snap (estalar dedos).
Quando o usuário estala o dedo, o programa:
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

try:
    from mediapipe import solutions
    from mediapipe.framework.formats import landmark_pb2
    import mediapipe as mp
    mp_hands = solutions.hands
    mp_drawing = solutions.drawing_utils
except (ImportError, AttributeError):
    print("❌ Erro ao importar MediaPipe. Tentando reinstalar...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "mediapipe"], check=True)
    sys.exit(1)

# Inicializar MediaPipe
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Inicializar text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Variáveis para detectar snap
snap_detected = False
last_snap_time = 0
snap_cooldown = 1.0  # Esperar 1 segundo entre snaps

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
    engine.say(text)
    engine.runAndWait()

def open_applications():
    """Abre Brave e VSCode"""
    print("[Abrindo] Brave...")
    try:
        subprocess.Popen(['brave-browser'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Brave não encontrado. Tentando alternativas...")
        try:
            subprocess.Popen(['brave'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            print("Aviso: Brave não encontrado no sistema")

    time.sleep(1)

    print("[Abrindo] VSCode...")
    try:
        subprocess.Popen(['code'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Aviso: VSCode não encontrado no sistema")

def detect_snap(landmarks):
    """
    Detecta gesto de estalar dedos (snap).
    Snap é quando o dedo indicador e polegar se tocam rapidamente.
    """
    if landmarks is None or len(landmarks) < 21:
        return False

    # Pontos chave: polegar (4), indicador (8)
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    index_pip = landmarks[6]

    # Calcular distância entre polegar e indicador
    thumb_x, thumb_y = thumb_tip.x, thumb_tip.y
    index_x, index_y = index_tip.x, index_tip.y

    distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

    # Se os dedos estão muito próximos (distância < 0.05), é um snap
    return distance < 0.05

def main():
    """Função principal"""
    global snap_detected, last_snap_time

    print("Iniciando detector de snap...")
    print("Pressione ESC para sair. Estale o dedo para ativar!")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erro: Não foi possível acessar a câmera")
        sys.exit(1)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Erro ao ler frame da câmera")
                break

            # Espelhar a imagem para melhor UX
            frame = cv2.flip(frame, 1)

            # Converter BGR para RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Processar mãos
            results = hands.process(rgb_frame)

            # Desenhar mãos
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS
                    )

                    # Detectar snap
                    if detect_snap(hand_landmarks.landmark):
                        current_time = time.time()
                        if current_time - last_snap_time > snap_cooldown:
                            snap_detected = True
                            last_snap_time = current_time

                            # Executa ações do snap
                            print("\n[SNAP DETECTADO!]")
                            cap.release()
                            cv2.destroyAllWindows()

                            # Saudação
                            greeting = get_greeting()
                            speak(greeting)

                            # Abrir aplicativos
                            open_applications()

                            print("Programa finalizado!")
                            return

            # Mostrar frame
            cv2.imshow('Snap Detector', frame)

            # ESC para sair
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
