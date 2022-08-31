import random
import os
import time
def game_start():
    turn=random.randint(1,2)
    row1=["   0    ","   1    ","   2    "]
    row2=["   3    ","   4    ","   5    "]
    row3=["   6    ","   7    ","   8    "]
    print(f"it's player {turn}'s turn")
    for i in range(9):
        os.system("cls")
        print(f"{row1[0]}   |   {row1[1]}   |   {row1[2]}")
        print('----------------------------------------')
        print(f"{row2[0]}   |   {row2[1]}   |   {row2[2]}")
        print('----------------------------------------')
        print(f"{row3[0]}   |   {row3[1]}   |   {row3[2]}")
        print('----------------------------------------')
        if row1[0]==row1[1]==row1[2]=="Player 1" or row2[0]==row2[1]==row2[2]=="Player 1" or row3[0]== row3[1]==row3[2]=="Player 1" or  row1[0]==row2[0]==row3[0]=="Player 1" or  row1[1]==row2[1]==row3[1]=="Player 1" or  row1[2]==row2[2]==row3[2]=="Player 1" or row1[0]==row2[1]==row3[2]=="Player 1" or row1[2]==row2[1]==row3[0]=="Player 1":
            print("player 1 wins")
            time.sleep(2)
            game_start()
        elif row1[0]==row1[1]==row1[2]=="Player 2" or row2[0]==row2[1]==row2[2]=="Player 2" or row3[0]== row3[1]==row3[2]=="Player 2" or  row1[0]==row2[0]==row3[0]=="Player 2" or  row1[1]==row2[1]==row3[1]=="Player 2" or  row1[2]==row2[2]==row3[2]=="Player 2" or row1[0]==row2[1]==row3[2]=="Player 2" or row1[2]==row2[1]==row3[0]=="Player 2":
            print("player 2 wins")
            time.sleep(2)
            game_start()
        choice=int(input(f"Player {turn} Enter your choice: "))
        if 0<=choice<=2:
            if turn==1:
                row1[choice]="Player 1"
                turn=2
            else:
                
                row1[choice]="Player 2"
                turn=1
        elif 3<=choice<=5:
            if turn==1:
                
                row2[choice-3]="Player 1"
                turn=2
            else:
                
                row2[choice-3]="Player 2"
                turn=1
        elif 6<=choice<=8:
            if turn==1:
                
                row3[choice-6]="Player 1"
                turn=2
            else:
                
                row3[choice-6]="Player 2"
                turn=1
        else:
            print("Please enter a valid index!!")
            return game_start()     

game_start()

        
            
