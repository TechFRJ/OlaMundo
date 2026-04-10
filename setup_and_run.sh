#!/bin/bash
# Script rápido para setup e execução

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

echo "🚀 Snap Startup - Setup Rápido"
echo ""

# Se venv não existe, criar
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Criando virtual environment..."
    python3 -m venv "$VENV_DIR"

    echo "📥 Ativando venv e instalando dependências..."
    source "$VENV_DIR/bin/activate"

    pip install --upgrade pip setuptools wheel > /dev/null 2>&1

    echo "⏳ Instalando OpenCV (pode levar alguns minutos)..."
    pip install opencv-python mediapipe pyttsx3 > /dev/null 2>&1

    echo "✓ Dependências instaladas!"
fi

# Ativar venv e executar
echo ""
echo "▶️  Iniciando Snap Startup..."
source "$VENV_DIR/bin/activate"
python3 "$PROJECT_DIR/snap_startup.py"
