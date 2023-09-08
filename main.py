
from Memorygame import *

def main():
    
    game = Memorygame()  

    
    game.display_welcome_message("start")

    
    game.display_blink_pattern()

    
    user_input = input("Enter the sequence of button presses: ")

    
    game.process_user_input(user_input)

    
    game.display_feedback()
    game.play_sound()

    
    game.display_game_over_message("game over")

if __name__ == "__main__":
    main()
