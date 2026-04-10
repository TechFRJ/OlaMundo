# 🚀 INÍCIO RÁPIDO - SEM COMPLICAÇÕES

## Passo 1: Instalar
```bash
cd ~/Área\ de\ trabalho/OlaMundo
source venv/bin/activate
pip install pyttsx3 keyboard
```

## Passo 2: Executar
```bash
python3 snap_startup.py
```

## Passo 3: Usar
- **Pressione ESPAÇO** para ativar
- **Pressione ESC** para sair

É isso! 🎉

---

## O que o programa faz:

1. ✅ Fala "Bom dia", "Boa tarde" ou "Boa noite" (conforme a hora)
2. ✅ Abre Brave (navegador)
3. ✅ Abre VSCode
4. ✅ Encerra o programa

## Se der erro de som:

```bash
sudo apt-get install -y espeak espeak-ng
```

Depois tente novamente.

---

## Alternativa: Sem teclado

Se a biblioteca `keyboard` não funcionar, o programa vai pedir para você pressionar ENTER no terminal:

```bash
python3 snap_startup.py
Pressione ENTER para ativar o programa: [você digita ENTER aqui]
```

Simples assim! ✌️
