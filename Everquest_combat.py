# EverQuest-Style Combat Simulator

# Import the random library so we can generate random damage and randomly select enemies
import random

# ---------------- FUNCTIONS ----------------

# Function to create a random enemy, with 10% chance for a named mob
def create_enemy():
    chance = random.randint(1, 10)  # 1 in 10 chance for named mob
    if chance == 1:
        enemy_name = "Fippy Darkpaw"
        enemy_hp = 50  # Stronger HP
        enemy_min_dmg = 5
        enemy_max_dmg = 10
    else:
        normal_enemies = ["a gnoll", "an orc pawn", "a skeleton"]
        enemy_name = random.choice(normal_enemies)
        enemy_hp = 30  # Normal HP
        enemy_min_dmg = 3
        enemy_max_dmg = 8
    return enemy_name, enemy_hp, enemy_min_dmg, enemy_max_dmg

# Function for the player's attack
def player_attack():
    return random.randint(3, 8)

# Function for the enemy's attack
def enemy_attack(min_dmg, max_dmg):
    return random.randint(min_dmg, max_dmg)

# Function to generate healing amount
def player_heal():
    return random.randint(2, 9)

# Function to check if someone has won
def check_winner(player_hp, enemy_hp, enemy_name):
    if player_hp <= 0:
        print("\nYou have been defeated! LOADING PLEASE WAIT.....\n")
        return True
    elif enemy_hp <= 0:
        print("\nYou defeated", enemy_name + "!")
        return True
    else:
        return False

# ---------------- MAIN GAME ----------------

# Player starting health
player_hp = 30

# Create enemy
enemy_name, enemy_hp, enemy_min, enemy_max = create_enemy()

# EverQuest-style intro message
print("You enter the West Commonlands...")
print("Suddenly,", enemy_name, "attacks you!")
print()

# Main combat loop
while True:

    print("***************************")
    print("*** Your HP:", player_hp, "***")
    print("***", enemy_name, "HP:", enemy_hp, "***")
    print("***************************\n")

    # Ask player what they want to do
    print("Choose an action:")
    print("1. Attack")
    print("2. Heal")

    choice = input("Enter 1 or 2: ")

    print("\n-------------------------------------------")

    # Player attack
    if choice == "1":
        print()
        damage = player_attack()
        enemy_hp -= damage
        print("-- You hit", enemy_name, "for", damage, "damage! --")

    # Player heal
    elif choice == "2":
        print()
        heal = player_heal()
        player_hp += heal
        print("-- You heal for", heal, "HP! --")

    else:
        print("\n*** INVALID CHOICE! ***\nPlease enter 1 to Attack or 2 to Heal.\n")
        continue

    print()

    # Check if enemy died
    if check_winner(player_hp, enemy_hp, enemy_name):
        break

    # Enemy attacks
    damage = enemy_attack(enemy_min, enemy_max)
    player_hp -= damage
    print("--", enemy_name, "hits you for", damage, "damage! --")
    print()

    # Check if player died
    if check_winner(player_hp, enemy_hp, enemy_name):
        break
    
    # Clear break between turns
    print("-------------------------------------------\n")