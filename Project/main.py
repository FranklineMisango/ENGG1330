import plane
import board
import os

def print_logo():
    print("""
                               _                  
     /\                       | |                 
    /  \   ___ _ __ ___  _ __ | | __ _ _ __   ___ 
   / /\ \ / _ \ '__/ _ \| '_ \| |/ _` | '_ \ / _ \ 
  / ____ \  __/ | | (_) | |_) | | (_| | | | |  __/ 
 /_/____\_\___|_|  \___/| .__/|_|\__,_|_| |_|\___| 
                        | |   _____ _
                        |_|  / ____| |                                       
                            | |    | |__   ___  ___ ___                      
                            | |    | '_ \ / _ \/ __/ __|                     
                            | |____| | | |  __/\__ \__ \                     
                             \_____|_| |_|\___||___/___/                     
    Press ENTER to continue
    """)
    input()

def main():
    print_logo()
    game = board.Board()
    while True:
        game.update_board()
main()