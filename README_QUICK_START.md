# 🚀 Snap Startup - Inicialização Rápida

## Opção 1: One-Liner (Mais Rápido) ⚡

Execute este comando para setup e execução automática:

```bash
python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip && pip install opencv-python mediapipe pyttsx3 && python3 snap_startup.py
```

Ou, separado em linhas para entender melhor:

```bash
# 1. Criar virtual environment
python3 -m venv venv

# 2. Ativar o ambiente
source venv/bin/activate

# 3. Instalar dependências
pip install --upgrade pip
pip install opencv-python mediapipe pyttsx3

# 4. Executar o programa
python3 snap_startup.py
```

## Opção 2: Script Automático 🤖

Se você tem o arquivo `setup_and_run.sh`:

```bash
chmod +x setup_and_run.sh
./setup_and_run.sh
```

## Opção 3: Instalação Completa (com autostart) 🔧

Se você tem `install.sh`:

```bash
bash install.sh
```

Depois execute com:

```bash
./run.sh
```

## Nota sobre a Versão

A versão atual usa **detecção de movimento** em vez de MediaPipe, o que:
- ✅ Funciona em mais sistemas
- ✅ Menos dependências pesadas
- ✅ Compatível com Python 3.11+
- ✅ Detecta movimento rápido de mão na câmera

## Opção 4: Via APT (Menos Recomendado)

Se preferir instalar globalmente (requer --break-system-packages):

```bash
pip3 install --break-system-packages opencv-python mediapipe pyttsx3
python3 snap_startup.py
```

## Como Usar o Programa

Após instalar e executar:

1. **Levante sua mão** para frente da câmera
2. **Estale os dedos** rapidamente (polegar + indicador)
3. O programa vai:
   - Falar a saudação (Bom dia/tarde/noite)
   - Abrir Brave
   - Abrir VSCode
   - Encerrar automaticamente

## Próximas Vezes

Uma vez instalado via venv, para executar novamente:

```bash
source venv/bin/activate
python3 snap_startup.py
```

Ou simplesmente:

```bash
./run.sh
```

## Se a Câmera não funcionar

Verificar câmera:

```bash
ls /dev/video*
```

Dar permissão:

```bash
sudo usermod -a -G video $USER
```

Depois faça logout e login novamente.

## Troubleshooting

**"ModuleNotFoundError"**: Certifique-se de que o venv está ativado (você deve ver `(venv)` no terminal)

**Câmera preta**: Verifique iluminação e se outra aplicação não está usando a câmera

**Som não funciona**: Instale espeak:
```bash
sudo apt-get install -y espeak espeak-ng
```

Aproveite! 🎉
