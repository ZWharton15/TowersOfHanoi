#Import the stack class
from data_structures import Stack
import sys
import os


def get_clear_command():
    #string used to clear console is different on windows to linux or mac
    if "win" in sys.platform:
        return "cls"
    else:
        return "clear"

#Establish the number of disks in the game
def choose_disk_amount():
    num_disks = 0
    while num_disks < 3:
      try:
        num_disks = int(input("\nHow many disks do you want to play with? (3+)\n"))
      except:
        print("Not a number, please try again.")
    return num_disks

#Get the users input for each move
def get_input():
    #The list of valid inputs
    choices = [stack.get_name()[0] for stack in stacks]
    
    #Ask for input until a valid choice is made
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {letter} for {name}")
        
        user_input = input("> ")
        user_input = user_input.upper()
        
        #Emergency break condition 
        if user_input == "Q":
            sys.exit(0)
        
        #Find which stack was selected and return it
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

#Update the 3 towers visually
def make_tower(tower, num_disks, towers):
    row = ""
    counter = num_disks-1
    tower_contents = tower.get_all_items()
    new_tower = []
    for i in range(num_disks+1, 0, -1):
        for j in range(6):
            if i == 1:
                row += "_"
            else:
                if j == 2:
                    if counter < len(tower_contents):
                        #fix formatting if there are more than 10 nodes
                        if len(tower_contents) > 9:
                            row += str(tower_contents[counter]).zfill(2)
                        else:
                            row += str(tower_contents[counter])
                    else:
                        row += "|"
                else:
                    row += " "
                    
        new_tower.append(row)
        row = ""
        counter -= 1
    towers.append(new_tower)
    pass
                
#Draw the 3 towers inline with eachother
def draw_towers(towers):
    tower1 = towers[0]
    tower2 = towers[1]
    tower3 = towers[2]
    
    for i in range(len(tower1)):
        print(tower1[i] + "   " + tower2[i] + "   " + tower3[i])
    #Add a label to the bottom of each tower
    print("Left     Middle   Right")
        
def print_title(player_moves, best_moves):
    print("~~~Towers of Hanoi~~~")
    print("Least Possible Moves: " + str(best_moves))
    print("Your Moves: " + str(player_moves))
    print("\n")

def make_move(towers):
    #Loop until a complete valid move is chosen
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        if from_stack.is_empty():
            print("That tower is empty. Try again...")
            draw_towers(towers)
            continue
        
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        
        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            break
        else:
            print("\n\nInvalid Move: Try again...")
            draw_towers(towers)
            
def game_loop(num_disks):
    num_user_moves = 0
    clear_string = get_clear_command()
    
    #Display the minimum number of moves to complete
    num_optimal_moves = 2**num_disks - 1
    print("Optimum amount of moves to complete: " + str(num_optimal_moves))
    
    #Loop until the size of the end stack is the size of the number of nodes in the game
    while right_stack.get_size() != num_disks:
        os.system(clear_string)
        
        #Display text at top of console
        print_title(num_user_moves, num_optimal_moves)
        
        towers = []
        #Update each of the stacks and put them into a list of lists
        for stack in stacks:
            make_tower(stack, num_disks, towers)
        
        
        #Draw the updated stacks each loop
        draw_towers(towers)
        
        #Call method to validate move
        make_move(towers)
        num_user_moves += 1
        
    return num_user_moves, num_optimal_moves

#Starting point of the game (Contains all the game logic)
def start():
    os.system(get_clear_command())
    num_disks = choose_disk_amount()
    
    #Push nodes to starting stack so that the biggest number is on the bottom of the stack
    for i in range(num_disks, 0, -1):
        left_stack.push(i)
    
    #Call a method to run the game loop
    final_moves, best_move = game_loop(num_disks)
    
    #Once the game loop is broken, the game is won
    print("\n\n\nYOU WIN!!!")
    print(f"YOU COMPLETED THE GAME IN {final_moves} MOVES!")
    print(f"The best posisble is {best_move}!")


if __name__ == "__main__":
    #Run until the user quits
    while True:
        stacks = []
        left_stack = Stack("Left")
        middle_stack = Stack("Middle")
        right_stack = Stack("Right")
        stacks = [left_stack, middle_stack, right_stack]
        #Setup the game
        start()
        
        should_restart = input("Play again? <y/n>\n")
        if should_restart == "n":
            break