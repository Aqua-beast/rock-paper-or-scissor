import random

def fun():
    print("Let's play rock, paper, scissor !!\n")
    option = input("select 'r' for rock, 'p' for paper or 's' for scissor\n").lower()
    game = random.choice(['r', 'p', 's'])
    print("Computer chose:", game)
    if game == option:
        return "That's a tie!"
    if is_Win(option, game):
        return "You won!"
    return "You lose!"
    
def is_Win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    return False

print(fun())
