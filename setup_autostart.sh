#!/bin/bash
# Script para configurar inicialização automática do Snap Startup

echo "=== Configuração de Autostart ==="
echo ""

# Obter o diretório do projeto
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Atualizar o caminho no arquivo .desktop
DESKTOP_FILE="$PROJECT_DIR/snap-startup.desktop"
sed -i "s|Exec=.*|Exec=python3 $PROJECT_DIR/snap_startup.py|g" "$DESKTOP_FILE"

# Copiar para autostart
AUTOSTART_DIR="$HOME/.config/autostart"
mkdir -p "$AUTOSTART_DIR"
cp "$DESKTOP_FILE" "$AUTOSTART_DIR/"

echo "✓ Arquivo de autostart copiado para $AUTOSTART_DIR"
echo ""
echo "O programa será iniciado automaticamente na próxima vez que você fizer login!"
echo ""
echo "Para remover o autostart, execute:"
echo "  rm $AUTOSTART_DIR/snap-startup.desktop"
