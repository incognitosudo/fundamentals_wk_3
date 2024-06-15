import random

diamonds = ["AD", "2D", "3D"] #["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds: #iterates as long as diamond lists is not empty
    user_input = input("Press enter to pick a card or type 'Q' to quit: ")

    if user_input == "": 
        
        random_choice = random.choice(diamonds)
        print("Card picked: ", random_choice)
        hand.append(random_choice)
        diamonds.remove(random_choice)
        print("Your hand has: ", hand)
        if not diamonds:
            print("There are no more cards to pick")
    
    elif user_input == "Q" or user_input =="q":
        print("Thanks for playing!")
        break

    else:
        print("Invalid try again.")
