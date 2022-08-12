from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from view import Ui_MainWindow
import random

class Controller(QMainWindow, Ui_MainWindow):
    '''
    A class representing a game of Rock Paper Scissors
    '''
    player_choice = ""          # Player Choice Holder
    computer_choice = ""        # Computer Choice Holder
    player_wins = 0             # Player Wins Count
    computer_wins = 0           # Computer Wins Count

    def __init__(self, *args, **kwargs) -> None:
        '''
        An initializer method that sets up the gui and makes the buttons work
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.rock_button.clicked.connect(lambda : self.rock())
        self.paper_button.clicked.connect(lambda : self.paper())
        self.scissors_button.clicked.connect(lambda : self.scissors())
        self.reset_button.clicked.connect(lambda: self.reset())

    def rock(self) -> None:
        '''
        A method that makes the player choice rock and calls the play method.
        '''
        Controller.player_choice = "Rock"
        self.play()

    def paper(self) -> None:
        '''
        A method that makes the player choice paper and calls the play method.
        '''
        Controller.player_choice = "Paper"
        self.play()

    def scissors(self) -> None:
        '''
        A method that makes the player choice scissors and calls the play method.
        '''
        Controller.player_choice = "Scissors"
        self.play()

    def play(self) -> None:
        '''
        A method that determines who won and calls the winner method and updates the wins
        '''
        game = ["Rock", "Paper", "Scissors"]  # List used for random generator
        Controller.computer_choice = random.choice(game)
        self.player_picture.setPixmap(QtGui.QPixmap(f"{Controller.player_choice}.png"))
        self.computer_picture.setPixmap(QtGui.QPixmap(f"{Controller.computer_choice}.png"))

        # Tie
        if Controller.player_choice == Controller.computer_choice:
            self.player_choice.setText(f"Player Choice: {Controller.player_choice}")
            self.computer_choice.setText(f"Computer Choice: {Controller.computer_choice}")
            self.outcome.setText(f"Outcome: Tie")

        # Scissors
        elif Controller.player_choice == "Scissors":
            if Controller.computer_choice == "Paper":
                self.winner(1)
            else:
                self.winner(2)

        # Paper
        elif Controller.player_choice == "Paper":
            if Controller.computer_choice == "Rock":
                self.winner(1)
            else:
                self.winner(2)

        # Rock
        else:
            if Controller.computer_choice == "Scissors":
                self.winner(1)
            else:
                self.winner(2)

        self.player_wins.setText(f"Player Wins: {Controller.player_wins}")
        self.computer_wins.setText(f"Computer Wins: {Controller.computer_wins}")

    def winner(self, num) -> None:
        '''
        A method that updates the choice strings and adds wins to the corresponding winner
        '''
        self.player_choice.setText(f"Player Choice: {Controller.player_choice}")
        self.computer_choice.setText(f"Computer Choice: {Controller.computer_choice}")

        if num == 1:
            self.outcome.setText(f"Outcome: Player Win")
            Controller.player_wins += 1
        else:
            self.outcome.setText(f"Outcome: Computer Win")
            Controller.computer_wins += 1

    def reset(self) -> None:
        '''
        A method that resets all the variables to the original format.
        '''
        Controller.player_wins = 0
        Controller.computer_wins = 0
        self.player_wins.setText(f"Player Wins: ")
        self.computer_wins.setText(f"Computer Wins: ")
        self.player_choice.setText(f"Player Choice: ")
        self.computer_choice.setText(f"Computer Choice: ")
        self.outcome.setText(f"Outcome:")
        self.player_picture.setPixmap(QtGui.QPixmap(f"RPS.png"))
        self.computer_picture.setPixmap(QtGui.QPixmap(f"RPS.png"))