import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key

clicking = False
mouse = Controller()
toggle_key = Key.f5

def clicker():
	while True:
		if clicking:
			mouse.click(Button.left)
		time.sleep(0.001)

def toggle_event(key):
	global clicking
	if key == toggle_key:
		clicking = not clicking

threading.Thread(target=clicker, daemon=True).start()
with Listener(on_press=toggle_event) as listener:
	listener.join()