#!/bin/bash
# Script de instalação do Snap Startup com Virtual Environment

echo "=== Snap Startup - Instalador com venv ==="
echo ""

# Obter diretório do projeto
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale Python3 primeiro."
    exit 1
fi

echo "✓ Python3 encontrado"

# Criar virtual environment
echo ""
echo "Criando virtual environment..."
python3 -m venv "$VENV_DIR"

# Ativar venv
echo "Ativando virtual environment..."
source "$VENV_DIR/bin/activate"

# Instalar dependências do sistema
echo ""
echo "Instalando dependências do sistema..."
sudo apt-get update
sudo apt-get install -y \
    python3-dev \
    libatlas-base-dev \
    libjasper-dev \
    libtiff5-dev \
    libjasper-dev \
    libjpeg-dev \
    libpng-dev \
    libharfbuzz0b \
    libwebp6 \
    libtiff5 \
    libjasper-dev \
    libatlas-base-dev \
    libqtgui4 \
    libqt4-test \
    libhdf5-dev \
    libharfbuzz0b \
    libwebp6 \
    libportaudio2 \
    espeak \
    espeak-ng

# Instalar dependências Python
echo ""
echo "Instalando dependências Python..."
pip install --upgrade pip
pip install -r requirements.txt

# Dar permissão de execução
chmod +x snap_startup.py

# Atualizar script launcher
cat > run.sh <<'LAUNCHER'
#!/bin/bash
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$PROJECT_DIR/venv/bin/activate"
python3 "$PROJECT_DIR/snap_startup.py"
LAUNCHER

chmod +x run.sh

echo ""
echo "✓ Instalação concluída!"
echo ""
echo "Para executar o programa:"
echo "  ./run.sh"
echo ""
echo "Ou ativar o venv manualmente:"
echo "  source venv/bin/activate"
echo "  python3 snap_startup.py"
echo ""
