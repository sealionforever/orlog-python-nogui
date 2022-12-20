# Needed to create random numbers to simulate dice roll
import random

# Initialise player health to 15
player1_health = 15
player2_health = 15

# Initialise player god coins to 0
player1_tokens = 0
player2_tokens = 0

# Initialise game over boolean
game_over = False

# Repeat everything until one player is dead
while not game_over:

    # Console graphics
    print("\n------------------------------")

    # Initialise values for the roll
    player1_axe_damage = 0
    player2_axe_damage = 0
    player1_arrow_damage = 0
    player2_arrow_damage = 0
    player1_gain_tokens = 0
    player2_gain_tokens = 0
    player1_steal_tokens = 0
    player2_steal_tokens = 0


    # Generate random numbers between 1 and 6 for each player.
    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)

    # Resolve rolled actions
    match player1_roll:
        case 1:
            player1_value = "Axe"
            player1_axe_damage += 1
        case 2:
            player1_value = "*Arrow*"
            player1_arrow_damage += 1
            player1_gain_tokens += 1
        case 3:
            player1_value = "Helmet"
            player2_axe_damage -= 1
        case 4:
            player1_value = "*Shield*"
            player2_arrow_damage -= 1
            player1_gain_tokens += 1
        case 5:
            player1_value = "Hand"
            player1_steal_tokens += 1
        case 6:
            player1_value = "Axe"
            player1_axe_damage += 1
    
    match player2_roll:
        case 1:
            player2_value = "Axe"
            player2_axe_damage += 1
        case 2:
            player2_value = "*Arrow*"
            player2_arrow_damage += 1
            player2_gain_tokens += 1
        case 3:
            player2_value = "Helmet"
            player1_axe_damage -= 1
        case 4:
            player2_value = "*Shield*"
            player1_arrow_damage -= 1
            player2_gain_tokens += 1
        case 5:
            player2_value = "Hand"
            player2_steal_tokens += 1
        case 6:
            player2_value = "Axe"
            player2_axe_damage += 1

    # Display rolls in console
    print("\nPlayer 1 rolled: ", player1_value)
    print("Player 2 rolled: ", player2_value)


    # Gain tokens
    player1_tokens += player1_gain_tokens
    player2_tokens += player2_gain_tokens

    # Display tokens in console
    print("\nPlayer 1 gains tokens: ", player1_gain_tokens, " tokens")
    print("Player 2 gains tokens: ", player2_gain_tokens, " tokens")
    print("Player 1 total: ", player1_tokens, " tokens")
    print("Player 2 total: ", player2_gain_tokens, " tokens")


    # Clean up negative damage
    if player1_axe_damage < 0:
        player1_axe_damage = 0
    if player1_arrow_damage < 0:
        player1_arrow_damage = 0
    if player2_axe_damage < 0:
        player2_axe_damage = 0
    if player2_arrow_damage < 0:
        player2_arrow_damage = 0
    
    # TODO: first do axe damage, then do arrow damage
    # Deal damage in order (if player 2 gets killed, game ends immediately)
    player2_health -= player1_axe_damage + player1_arrow_damage
    if player2_health <= 0:
        player2_health = 0
        game_over = True
        print("\nPlayer 1 has killed the other player!")
        break;
    
    if player1_axe_damage + player1_arrow_damage <= 0:
        player1_damage_value = "no"
    else:
        player1_damage_value = player1_axe_damage + player1_arrow_damage
    print("\nPlayer 1 deals ", player1_damage_value, " damage to the other player.")
    
    player1_health -= player2_axe_damage + player2_arrow_damage
    if player1_health <= 0:
        player1_health = 0
        game_over = True
        print("Player 2 has killed the other player!")
        break;
    
    if player2_axe_damage + player2_arrow_damage <= 0:
        player2_damage_value = "no"
    else:
        player2_damage_value = player2_axe_damage + player2_arrow_damage
    print("Player 2 deals ", player2_damage_value, " damage to the other player.")

    print("\nHealth status")
    print("Player 1 health: ", player1_health)
    print("Player 2 health: ", player2_health)
    

    # TODO: Issue when one has 0 tokens and both steal...
    # Steal tokens
    if player2_tokens > 0:
        player2_tokens -= player1_steal_tokens
        player1_tokens += player1_steal_tokens
    if player1_tokens > 0:
        player1_tokens -= player2_steal_tokens
        player2_tokens += player2_steal_tokens


    # Selection: based on comparison of the values, take the appropriate path through the code.
    if player1_health > player2_health:
        print("Player 1 is winning.")
    elif player2_health > player1_health:
        print("Player 2 is winning.")
    else:
        print("It's a draw")

    input("\nPress enter to roll again.")  # Wait for user input to proceed.

print("\n### Game Over ###")
print("Player 1 health:", player1_health)
print("Player 1 tokens:", player1_tokens)
print("Player 2 health:", player2_health)
print("Player 2 tokens:", player2_tokens)