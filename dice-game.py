# Needed to create random numbers to simulate dice roll
import random

# Initialise player health to 20
player1_health = 20
player2_health = 20

# Initialise player god coins to 0
player1_tokens = 0
player2_tokens = 0

# Repeat everything in this block 10 times
for i in range(10):

    # Generate random numbers between 1 and 6 for each player.
    player1_roll = random.randint(1, 5)
    player2_roll = random.randint(1, 5)

    # Initialise values for the roll
    player1_axe_damage = 0
    player2_axe_damage = 0
    player1_arrow_damage = 0
    player2_arrow_damage = 0
    player1_gain_tokens = 0
    player2_gain_tokens = 0
    player1_steal_tokens = 0
    player2_steal_tokens = 0

    # Resolve rolled actions
    match player1_roll:
        case 1:
            player1_value = "Axe"
            player1_axe_damage += 1
        case 2:
            player1_value = "Arrow"
            player1_arrow_damage += 1
        case 3:
            player1_value = "Helmet"
            player2_axe_damage -= 1
        case 4:
            player1_value = "Shield+"
            player2_arrow_damage -= 1
            player2_gain_tokens += 1
        case 5:
            player1_value = "Hand+"
            player1_steal_tokens += 1
            player1_gain_tokens += 1
    
    match player2_roll:
        case 1:
            player2_value = "Axe"
            player2_axe_damage += 1
        case 2:
            player2_value = "Arrow"
            player2_arrow_damage += 1
        case 3:
            player2_value = "Helmet"
            player1_axe_damage -= 1
        case 4:
            player2_value = "Shield+"
            player1_arrow_damage -= 1
            player2_gain_tokens += 1
        case 5:
            player2_value = "Hand+"
            player2_steal_tokens += 1
            player2_gain_tokens += 1

    # Summarize damage
    if player1_axe_damage < 0:
        player1_axe_damage = 0
    if player1_arrow_damage < 0:
        player1_arrow_damage = 0
    if player2_axe_damage < 0:
        player2_axe_damage = 0
    if player2_arrow_damage < 0:
        player2_arrow_damage = 0
    
    # Deal Damage
    player1_health -= player2_axe_damage + player2_arrow_damage
    player2_health -= player1_axe_damage + player1_arrow_damage

    # Gain tokens
    player1_tokens += player1_gain_tokens
    player2_tokens += player2_gain_tokens

    # TODO: Issue when one has 0 tokens and both steal...
    # Steal tokens
    if player2_tokens > 0:
        player2_tokens -= player1_steal_tokens
        player1_tokens += player1_steal_tokens
    if player1_tokens > 0:
        player1_tokens -= player2_steal_tokens
        player2_tokens += player2_steal_tokens

    # Display the damage values
    if player1_axe_damage + player1_arrow_damage > 0:
        player1_damage_value = "some"
    else:
        player1_damage_value = "no"

    if player2_axe_damage + player2_arrow_damage > 0:
        player2_damage_value = "some"
    else:
        player2_damage_value = "no"

    print("Player 1 rolled: ", player1_value, " and takes", player1_damage_value, "damage.")
    print("Player 2 rolled: ", player2_value, " and takes", player2_damage_value, "damage.")
    print("Player 1:\n    health ", player1_health, "\n    tokens ", player1_tokens)
    print("Player 2:\n    health ", player2_health, "\n    tokens ", player2_tokens)

    # Selection: based on comparison of the values, take the appropriate path through the code.
    if player1_health > player2_health:
        print("Player 1 is winning.")
    elif player2_health > player1_health:
        print("Player 2 is winning.")
    else:
        print("It's a draw")

    input("Press enter to continue.")  # Wait for user input to proceed.

print("### Game Over ###")
print("Player 1 health:", player1_health)
print("Player 1 tokens:", player1_tokens)
print("Player 2 health:", player2_health)
print("Player 2 tokens:", player2_tokens)