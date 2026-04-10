#!/bin/bash
# Script de instalação do Snap Startup

echo "=== Snap Startup - Instalador ==="
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale Python3 primeiro."
    exit 1
fi

echo "✓ Python3 encontrado"

# Instalar dependências do sistema
echo ""
echo "Instalando dependências do sistema..."
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    libportaudio2 \
    espeak \
    espeak-ng

# Instalar dependências Python
echo ""
echo "Instalando dependências Python..."
pip3 install -r requirements.txt

# Dar permissão de execução
chmod +x snap_startup.py

echo ""
echo "✓ Instalação concluída!"
echo ""
echo "Para executar o programa:"
echo "  python3 snap_startup.py"
echo ""
