global win
global no_repeats
global block_values
import random as random
block_values = {
    "row1": [1,2,3],
    "row2": [4,5,6],
    "row3": [7,8,9]
}

no_repeats = []

def block_row(var1, var2, var3):
    first = "+"+7*"-"+"+"+"+"+7*"-"+"+"+"+"+7*"-"+"+"
    second = "|"+7*' '+"|"+7*' '+"|"+7*' '+"|"
    third = "|"+3*' '+ var1 + "   " +"|"+3*' '+ var2 + "   "+"|"+3*' '+ var3 + "   " +"|"
    fourth = "|"+7*' '+"|"+7*' '+"|"+7*' '+"|"
    fifth = "+"+7*"-"+"+"+"+"+7*"-"+"+"+"+"+7*"-"+"+"
    return first + "\n" + second + "\n" + third + "\n" + fourth + "\n" + fifth
    
def draw_board():
    block_dict = {}
    for i in block_values.keys():
        block_dict[i] = block_row(str(block_values[i][0]),str(block_values[i][1]),str(block_values[i][2]))
    print(block_dict["row1"] + "\n" + block_dict["row2"]+ "\n" + block_dict["row3"])
win = False
def define_winner(value):
    if value == "xxx":
        print("X Wins!")
        win = True
        
        
    elif value =="ooo":
        print('O wins!')
        win = True

def win_con(dic):
    for key in dic.keys():
        tester = ""
        for value in dic[key]:
            tester += str(value)
        define_winner(tester)
    for i in range(3):
        tester = ""
        for key in dic.keys():
            tester += str(dic[key][i])
        define_winner(tester)

def player_turn():
    chosen = int(input("Choose a square for your X:  "))
    if chosen in no_repeats:
        print("Already chosen")
        player_turn()
    try:
        if chosen >= 1 and chosen <= 9: 
            no_repeats.append(chosen)
            return chosen
    except:
        print("Invalid choice")
        player_turn()
        

player = True



def turn_checker():
    if player:
        return True
    elif not player:
        return False
    
    

def change_blck_value(x):
    for value in block_values.keys():
        for i in range(3):
            if block_values[value][i] == x:
                if turn_checker():
                    block_values[value][i] = "x"
                else:
                    block_values[value][i] = "o"
def bot_turn():
    num = random.randint(1,10)
    if num in no_repeats:
        bot_turn()
    elif num > 9:
        bot_turn()
    else:
        no_repeats.append(num)
        return num
    
draw_board()
counter = 0
while win != True:
    print("round: ", counter)
    print("player Turn")
    change_blck_value(player_turn())
    draw_board()
    win_con(block_values)
    player = False
    print("Bot Turn")
    change_blck_value(bot_turn())
    win_con(block_values)
    draw_board()
    player = True
    counter += 1
                
