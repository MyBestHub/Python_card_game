import random
my_highscore = 0 
computer_highscore = 0 
fun_list = ["Boooyah!", "Not bad...", "You are improving!", "Keep going!"]

while True:
    print("Select one of the 3 cards, the highest number win!" )
    print("Your score is: ", my_highscore)
    print("The computer score is: ", computer_highscore, "\n")
    print("Type A for the first card (ﾉಥ益ಥ）ﾉ")
    print("Type B for the second card ʕノ•ᴥ•ʔノﾉ")
    print("Type C for the third card  ( ͡ᵔ ͜ʖ ͡ᵔ )")
    print("Type 1 to leave the game")
    selection = input("Selection picked: ")
     

    
    
    if selection == "A":
        my_card = random.randint(1, 10)
        computer_card = random.randint(2, 8)
        print("\nYour number is", my_card)
        print("The computer number is", computer_card)
    if selection == "B":
        
        my_card = random.randint(1, 10)
        computer_card = random.randint(1, 7)
        print("\nYour number is", my_card)
        print("The computer number is", computer_card)
        
    if selection == "C":
        
        my_card = random.randint(3, 10)
        computer_card = random.randint(2, 10)
        print("\nYour number is", my_card)
        print("The computer number is", computer_card)
    
    if selection != "A" and selection != "B" and selection != "C":
        print("Type A, B or C only")
    
    if my_card > computer_card and selection == "A" or my_card > computer_card and selection == "B" or my_card > computer_card and selection == "C":
        my_highscore = my_highscore +1   
        print("Your score: ", my_highscore,  "    ",  random.choice(fun_list))
            
    if computer_card > my_card and selection == "A" or computer_card > my_card and selection == "B" or computer_card > my_card and selection == "C":
        computer_highscore = computer_highscore + 1   
        print("Computer score: ", computer_highscore,  "    ",  random.choice(fun_list))

    if computer_highscore == 7:
        print("\nThe computer won!\n")
        break
    if my_highscore == 7:
        print("\nI beat the computer!\n")
        break

    if selection == "1":
        break

    
        
