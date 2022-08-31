move1=input("Enter choice for player 1: ")
move2=input("Enter choice for player 2: ")
if move1==move2:
    print("It\'s tie")
elif (move1=="rock" and move2=="paper")or(move1=="scisser" and move2=="rock")or(move1=="paper" and move2=="scisser"):
    print("Player 2 wins")
elif (move1=="paper" and move2=="rock") or (move1=="rock" and move2=="scisser") or (move1=="scisser" and move2=="paper"):
    print("Player 1 wins")
