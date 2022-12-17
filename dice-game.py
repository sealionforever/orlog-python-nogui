# Needed to create random numbers to simulate dice roll
import random

# Initialise player scores to 0
player1_score = 0
player2_score = 0

# Repeat everything in this block 10 times
for i in range(10):

    # Generate random numbers between 1 and 6 for each player.
    player1_roll = random.randint(1, 5)
    player2_roll = random.randint(1, 5)

    match player1_roll:
        case 1:
            player1_value = "Axe"
        case 2:
            player1_value = "Arrow"
        case 3:
            player1_value = "Helmet"
        case 4:
            player1_value = "Shield"
        case 5:
            player1_value = "Hand"
    
    match player2_roll:
        case 1:
            player2_value = "Axe"
        case 2:
            player2_value = "Arrow"
        case 3:
            player2_value = "Helmet"
        case 4:
            player2_value = "Shield"
        case 5:
            player2_value = "Hand"

    # Display the values
    print("Player 1 rolled: ", player1_value)
    print("Player 2 rolled: ", player2_value)

    # Selection: based on comparison of the values, take the appropriate path through the code.
    if player1_roll > player2_roll:
        print("player 1 wins.")
        player1_score = player1_score + 1  # This is how we increment a variable
    elif player2_roll > player1_roll:
        print("player 2 wins")
        player2_score = player2_score + 1
    else:
        print("It's a draw")

    input("Press enter to continue.")  # Wait for user input to proceed.

print("### Game Over ###")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)