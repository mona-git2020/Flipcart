from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

def select_file_from_window(locations):
	print(locations)
	for char in locations:
		print(char)
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.12)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)