# EverQuest-Style Combat Simulator

## Name
Ralfi Bradford

## Project Description
This project is a simple text-based combat simulator inspired by EverQuest. The player fights one randomly selected enemy in turn-based combat. Most enemies are normal enemies such as a gnoll, an orc pawn, or a skeleton, but there is also a small random chance to encounter a stronger named enemy, Fippy Darkpaw. The player can choose to attack or heal until either the player or the enemy is defeated.

This project was designed to practice basic Python programming concepts including variables, functions, if/else statements, loops, and I chose to use Random as my new python library.

## How I Tested My Project
I tested the program by running it multiple times and trying different inputs. I tested:
- Entering `1` to make sure attacking worked correctly
- Entering `2` to make sure healing worked correctly
- Entering invalid inputs such as letters, `0`, and `3` to make sure the invalid choice message appeared
- Running the program several times to make sure different enemies appeared
- Running the program multiple times to confirm the named enemy, Fippy Darkpaw, could appear randomly
- Checking that combat ended correctly when either the player or the enemy reached 0 HP
- Checking that healing worked and did not make the game crash

## Reflection
Overall, I learned how to combine several beginner Python concepts into one working project. I practiced using variables to store health and damage values, functions to organize repeated actions, if/else statements to control combat choices, and loops to keep the game running until the battle ended. This project helped me understand how individual programming concepts can work together in a complete program.

The new Python concept I explored was the `random` library. I used `random.choice()` to select random enemies and `random.randint()` to create random damage and healing amounts. One challenge I faced was balancing the combat so the player would not always win too easily. I fixed that by adjusting enemy health and damage values and adding a stronger named enemy. Another challenge was making the output easier to read, which I improved by adding spacing, separators, and clearer combat formatting.