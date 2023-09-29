import machine
import utime
import random
import time
import random
from Displays import *
from Model import *
from Button import *
from Counters import *
from Lights import *
from CompositeLights import *
from Numbers import *

class GamePlay:
    def __init__(self):
        self._display = LCDDisplay(sda = 0, scl = 1, i2cid = 0)
        self.randomNumbers = []
        self.entriesValue = 0
        self.score = 0
        self._buttonYellow = Button(20, "1", buttonhandler = self)
        self._buttonGreen = Button(17, "2", buttonhandler = self)
        self._lightYellow = Light(5, "1")
        self._lightGreen = Light(6, "2")
        self._randomArray = Numbers()
        self._model = Model(9, self, debug=True)
        self._model.addButton(self._buttonYellow)
        self._model.addButton(self._buttonGreen)
        self._model.addTransition(0, [BTN1_PRESS, BTN2_PRESS], 1)  
        self._model.addTransition(1, [NO_EVENT], 2)
        self._model.addTransition(2, [BTN1_PRESS], 3)
        self._model.addTransition(2, [BTN2_PRESS], 4)
        self._model.addTransition(5, [BTN1_PRESS, BTN2_PRESS], 1)
        self._model.addTransition(6, [BTN1_PRESS, BTN2_PRESS], 0)

    def run(self):
        self._model.run()  

    def blinkYellowLight(self):
        self._lightYellow.blink()

    def blinkGreenLight(self):
        self._lightGreen.blink()
        '''
state 0 : idle
state 1: random numbers 
state 2 : input entry state
state 3 :yellow 
state 4 :green
state 5: won
state 6:end game
'''
    def stateEntered(self, state, event):
        if state == 0:
            self._display.reset()
            self.score = 0
            self._display.showText("Begin Game")
            self._display.showText(f"Score: {self.score}", 1)
            randomNumbers = []
        elif state == 1:
            self._display.showText("watch LEDs")
            self.entriesValue = 0
            self.randomNumbers = self._randomArray.create_random_array()
            print(self.randomNumbers)
            for number in self.randomNumbers:
                lightNumber = number
                print(lightNumber)
                if lightNumber == 1:
                    self.blinkYellowLight()
                elif lightNumber == 2:
                    self.blinkGreenLight()  
        
        elif state == 2:
            self._display.showText("press the Colors")
            if self.entriesValue == 3:
                self._model.gotoState(5)
        
        elif state == 3:
            self.blinkYellowLight()
            if self.randomNumbers[self.entriesValue] == 1:
                self.entriesValue = self.entriesValue + 1
                self._model.gotoState(2)
            else:
                self._model.gotoState(6)
        elif state == 4:
            self.blinkGreenLight()
            print(self.entriesValue)
            print(self.randomNumbers)
            if self.randomNumbers[self.entriesValue] == 2:
                self.entriesValue = self.entriesValue + 1
                print(self.entriesValue)
                self._model.gotoState(2)
            else:
                self._model.gotoState(6)

        elif state == 5:
            self.score = self.score + 1
            self._display.showText(f"points: {self.score}", 1)
            self._display.showText("Your points")

        elif state == 6:
            self._display.showText("Game Over!")
            self._display.showText(f"Final points: {self.score}", 1)

    def stateLeft(self, state, event):
        pass
    def stateDo(self, state):
        pass
        
if __name__ == '__main__':
    game = GamePlay()
    game.start_game()
    game.run()





        

