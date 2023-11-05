import pyautogui
import keyboard
import time
from config import *

def main():

    screen_width, screen_height = get_screen_resolution()

    mouse_x_position = screen_width/2 
    mouse_y_position = screen_height/2
    
    running = True
    mouse_sensitivity = 30

    while running:
        move = False
        #get keyboard input
        if keyboard.is_pressed("ctrl+alt+up"):
            mouse_y_position -= mouse_sensitivity
            move = True          

        if keyboard.is_pressed("ctrl+alt+down"):
            mouse_y_position += mouse_sensitivity
            move = True    

        if keyboard.is_pressed("ctrl+alt+left"):
            mouse_x_position -= mouse_sensitivity
            move = True    
        
        if keyboard.is_pressed("ctrl+alt+right"):
            mouse_x_position += mouse_sensitivity
            move = True        
        
        if keyboard.is_pressed("ctrl+q"):
            running = False

        if keyboard.is_pressed("ctrl+alt+["):
            pyautogui.click(mouse_x_position, mouse_y_position)
        
        if move:
            pyautogui.moveTo(mouse_x_position, mouse_y_position, duration=0.001)

        

        


if __name__ == '__main__':
    main()
