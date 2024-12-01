from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import httpx
from string import Template

controller = Controller()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate" # ENDPOINT where model will generate response
OLLAMA_CONFIG = {"model": "mistral:7b-instruct-q4_K_S",
                 "keep_alive": "5m",
                 "stream": False 
}

PROMPT_TEMPLATE = Template(
    """Fix all typos and casing and puctuation in this text, but preserve all new line characters, return only the corrected text, don't include a preamble
    $text
    """
)


def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(OLLAMA_ENDPOINT,
                          json={"prompt": prompt, **OLLAMA_CONFIG},
                          headers={"Content-Type": "application/json"},
                          timeout=10)
    if response.status_code != 200:
        return None
    return response.json()["response"].strip()



def fix_current_line():
    # Select the current line: shortcut on mac -> Cmd + Shift + Left arrow key
    controller.press(Key.cmd)
    controller.press(Key.shift)
    controller.press(Key.left)

    controller.release(Key.cmd)
    controller.release(Key.shift)
    controller.release(Key.left)

    fix_selection()

def fix_selection():
    # Copy section to the clipboard
    with controller.pressed(Key.cmd):
        controller.tap('c')
    
    # Get the text from clipboard
    time.sleep(0.1)
    text = pyperclip.paste()

    # Fix the text
    fixed_text = fix_text(text)

    # Copy back to clipboard 
    pyperclip.copy(fixed_text)
    time.sleep(0.1)

    # Insert text
    with controller.pressed(Key.cmd):
        controller.tap('v')

def on_f1():
    fix_current_line()

def on_f2():
    fix_selection()




with keyboard.GlobalHotKeys({
        '<122>': on_f1,
        '<120>': on_f2}) as h:
    h.join()
