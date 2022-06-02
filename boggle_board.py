import string
import random


def print_board(board):
    for row in board:
      print(row[0], row[1], row[2], row[3])

class BoggleBoard:
    dice = [
        'AAEEGN',
        'ELRTTY',
        'AOOTTW',
        'ABBJOO',
        'EHRTVW',
        'CIMOTU',
        'DISTTY',
        'EIOSST',
        'DELRVY',
        'ACHOPS',
        'HIMNQU',
        'EEINSU',
        'EEGHNW',
        'AFFKPS',
        'HLNNRZ',
        'DEILRX'
      ]

  def __init__(self):
    self.board = [
      ['_', '_', '_', '_'],
      ['_', '_', '_', '_'],
      ['_', '_', '_', '_'],
      ['_', '_', '_', '_']      
      ]
    return print_board(self.board)

  

  def shake(self):
    for row in self.board:
      for col in range(len(row)):
        letter = random.choice(string.ascii_uppercase)
        row[col] = letter
        
    return print_board(self.board)


board = BoggleBoard()

board.shake()