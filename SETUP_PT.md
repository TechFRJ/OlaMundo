# 📱 Snap Startup - Programa de Inicialização com Gesto

Um programa inovador para Linux que detecta um gesto de estalar dedos (snap) e abre seus aplicativos favoritos com uma saudação personalizada!

## ✨ Funcionalidades

- 👋 **Detecção de Gesto**: Detecta quando você estala o dedo
- 🎙️ **Saudação Personalizada**: Fala "Bom dia", "Boa tarde" ou "Boa noite" baseado na hora
- 🌐 **Abre Aplicativos**: Inicia automaticamente Brave e VSCode
- 🚀 **Autostart**: Executa automaticamente ao fazer login

## 📋 Pré-requisitos

- Linux (Ubuntu/Debian recomendado)
- Python 3.7+
- Câmera web
- Microfone (para síntese de voz)

## 🚀 Instalação Rápida

### 1. Instalar dependências automáticamente:
```bash
cd /home/user/OlaMundo
bash install.sh
```

### 2. Ou instalar manualmente:

**Dependências do sistema:**
```bash
sudo apt-get update
sudo apt-get install -y python3-pip libportaudio2 espeak espeak-ng
```

**Dependências Python:**
```bash
pip3 install -r requirements.txt
```

## 🎯 Como Usar

### Teste Manual
```bash
python3 snap_startup.py
```

Ao iniciar:
- A câmera será ativada
- Levante sua mão para a câmera
- **Estale os dedos** (junte o dedo indicador ao polegar rapidamente)
- O programa fará a saudação e abrirá os aplicativos

### Configurar para Iniciar Automaticamente

#### No GNOME/Ubuntu 20.04+:
```bash
mkdir -p ~/.config/autostart
cp snap-startup.desktop ~/.config/autostart/
```

#### No KDE/Plasma:
```bash
mkdir -p ~/.config/autostart
cp snap-startup.desktop ~/.config/autostart/
```

Depois de fazer logout e login novamente, o programa iniciará automaticamente.

## 🎮 Controles

- **Estalar Dedos**: Ativa o programa
- **ESC**: Sair do programa

## 🔧 Personalização

### Editar horários da saudação

Abra `snap_startup.py` e modifique a função `get_greeting()`:

```python
def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Bom dia!"
    elif 12 <= hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
```

### Adicionar mais aplicativos

Modifique a função `open_applications()`:

```python
def open_applications():
    subprocess.Popen(['brave-browser'])
    time.sleep(1)
    subprocess.Popen(['code'])
    # Adicione mais:
    subprocess.Popen(['firefox'])
```

## 🐛 Troubleshooting

### Câmera não funciona
```bash
# Verificar dispositivos de câmera
ls /dev/video*

# Testar permissões
sudo usermod -a -G video $USER
```

### Som não funciona
```bash
# Instalar eSpeak corretamente
sudo apt-get install -y espeak espeak-ng
```

### Aplicativos não abrem
Verifique se Brave e VSCode estão instalados:
```bash
which brave-browser
which code
```

## 📝 Notas Técnicas

- **Detecção de Snap**: Usa MediaPipe para rastrear mãos
- **Síntese de Voz**: Usa pyttsx3 com eSpeak
- **Visão**: OpenCV para captura de câmera
- **Compatibilidade**: Linux com suporte a X11/Wayland

## 📄 Licença

Veja LICENSE para detalhes.

## 💡 Dicas

1. **Iluminação**: Use boa iluminação para melhor detecção
2. **Distância**: Mantenha a mão entre 30-60cm da câmera
3. **Velocidade**: O snap deve ser rápido e definido
4. **Calibração**: O programa tem cooldown de 1 segundo entre snaps

Aproveite! 🎉
