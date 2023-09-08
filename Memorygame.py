import time
from light import *
from Button import *
from Displays import *

class Memorygame:
    """
    this is the class for the counter gadget that can count up and reset and display 
    a count on an LCD
    """

    def __init__(self):
        self._number = 0
        self._display = LCDDisplay(sda = 0, scl = 1, i2cid = 0)
        self._led1 = Pin(5, Pin.OUT)
        self._led2 = Pin(6, Pin.OUT)
        led_pins = [5,6]
        self._button1 = Button(16,"Yellow", buttonhandler =self)
        
        self._button2 = Button(17, "green", buttonhandler =self)
        self.display() 
        mydisplay.showText("start")

        for pin in led_pins:
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)


def generate_pattern(length):
    return [random.choice(led_pins) for _ in range(length)]


def play_pattern(pattern):
    for led_pin in pattern:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)
        
        import RPi.GPIO as GPIO
import time
import random


GPIO.setmode(GPIO.BCM)

led_pins = [6,7]  
button_pins = [16,17]  

# Set up the GPIO pins
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to generate a random sequence
def generate_sequence(length):
    return [random.choice(led_pins) for _ in range(length)]

# Function to light up and turn off LEDs in the sequence
def play_sequence(sequence):
    for led_pin in sequence:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)

# Function to check if the player repeats the sequence correctly
def check_sequence(player_sequence, sequence):
    return player_sequence == sequence

try:
    while True:
        # Generate a random sequence
        sequence = generate_sequence(5)  
        
        # Display the sequence to the player
        play_sequence(sequence)

        # Get the player's input
        player_sequence = []
        for _ in range(len(sequence)):
            print("Press the corresponding buttons for the sequence:")
            for led_pin in sequence:
                GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(0.5)
            for led_pin in sequence:
                GPIO.output(led_pin, GPIO.LOW)

            # Wait for button presses (replace with actual button input handling)
            for button_pin in button_pins:
                while GPIO.input(button_pin) == GPIO.HIGH:
                    pass
                player_sequence.append(button_pin)
                time.sleep(0.2)  # Debounce time

        # Check if the player's input matches the sequence
        if check_sequence(player_sequence, sequence):
            print("Correct! Next round.")
        else:
            print("Wrong sequence. Game over.")
            break

except KeyboardInterrupt:
    # Cleanup GPIO on Ctrl+C
    GPIO.cleanup()
