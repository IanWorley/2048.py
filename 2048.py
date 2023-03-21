import random
import pprint
import keyboard

def print_game(gameBoard):
   for i in range(4):
       print("|", end="")
       for j in range(4):
           if gameBoard[i][j] == 0:
               print(" ", end="|")
           else: 
                print(gameBoard[i][j], end="|")
       print()





def game_start(gameBoard):
    for _ in range(2):
      x =  random.randint(0,3)
      d = random.randint(0,3)
      if gameBoard[x][d] == 0:
        gameBoard[x][d] = random.randint(1,2) * 2



def main():
    gameBoard = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]
    game_start(gameBoard)
    while True:
        if keyboard.on_press_key("up"):
            print("up")
        elif keyboard.on_press_key("down"):
            print("down")
        elif keyboard.on_press_key("left"):
            print("left")
        elif keyboard.on_press_key("right"):
            print("right")



        print_game(gameBoard)


if __name__ == "__main__":
    main()

    
