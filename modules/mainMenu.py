'''
Module responsible for displaying the main menu panel.
'''

import pygame
import sys
from modules.gameStateManager import GameStateManager
from modules.buttons import Button

class MainMenu:
    def __init__(self, screen: pygame.Surface, gameState: GameStateManager):

        MARGIN = 20
        WHITE = pygame.Color("White")

        self.screen = screen
        self.window = screen.get_rect()
        self.gameState = gameState
        self.startIMG = pygame.image.load("images/start_button.png")
        self.htpIMG = pygame.image.load("images/htp_button.png")
        self.quitIMG = pygame.image.load("images/quit_button.png")
        self.startButton = Button(self.startIMG)
        self.htpButton = Button(self.htpIMG)
        self.quitButton = Button(self.quitIMG)
        self.titleIMG = pygame.image.load("images/title.png")
        self.title_box = self.titleIMG.get_rect()

        self.screen.fill(pygame.Color("Black"))

        buttonHeight = self.startIMG.get_height()
        self.title_box.top = self.window.top + MARGIN
        self.title_box.centerx = self.window.centerx
        startPos = (self.window.centerx, 
                    self.title_box.bottom + MARGIN + buttonHeight)
        htpPos = (startPos[0], 
                  startPos[1] + MARGIN + buttonHeight)
        quitPos = (htpPos[0], 
                      htpPos[1] + MARGIN + buttonHeight)
        
        self.startButton.set_pos(startPos)
        self.htpButton.set_pos(htpPos)
        self.quitButton.set_pos(quitPos)


    def run(self):
        '''
        Run method displays the panel on the screen.
        '''
        
        MARGIN = 30

        BLACK = pygame.Color("Black")

        pygame.display.set_caption("Main Menu")
        
        self.screen.fill(BLACK)
        self.screen.blit(self.titleIMG, self.title_box)
        self.startButton.draw(self.screen)
        self.htpButton.draw(self.screen)
        self.quitButton.draw(self.screen)

        self.startButton.onClick(self.gameState.set_state, "LevelSelection")
        self.htpButton.onClick(self.gameState.set_state, "HowTo")
        self.quitButton.onClick(self.quit)
        self.controls()

    def quit(self):
        '''
        Quit the program.
        '''
        
        pygame.quit()
        sys.exit()

    def controls(self):
        '''
        Method for handling the inputs the user is making.
        '''
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameState.set_state("AskQuit")