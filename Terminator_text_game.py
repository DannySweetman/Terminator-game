import random
import time

# Define character and terminator stats
player_health = 100
terminator_health = 150
inventory = []


def print_delay(message, delay=1):
    """Helper function to print text with a delay"""
    print(message)
    time.sleep(delay)


def fight():
    global player_health, terminator_health
    print_delay("You have engaged the Terminator in a fight!")

    while player_health > 0 and terminator_health > 0:
        try:
            action = input("Choose your action (attack/heal/run): ").strip().lower()
        except EOFError:
            print("Error in input. Please try again.")
            continue

        if action == "attack":
            damage = random.randint(10, 30)
            terminator_health -= damage
            print_delay(f"You hit the Terminator for {damage} damage! Terminator health is now {terminator_health}.")

            if terminator_health <= 0:
                print_delay("You defeated the Terminator!")
                return "win"

            # Terminator retaliates
            terminator_damage = random.randint(15, 35)
            player_health -= terminator_damage
            print_delay(f"The Terminator hits you for {terminator_damage} damage! Your health is now {player_health}.")

            if player_health <= 0:
                print_delay("The Terminator has defeated you...")
                return "lose"

        elif action == "heal":
            if "medkit" in inventory:
                player_health += 20
                inventory.remove("medkit")
                print_delay("You used a medkit and restored 20 health!")
                print_delay(f"Your health is now {player_health}.")
            else:
                print_delay("You don't have a medkit!")

        elif action == "run":
            print_delay("You managed to escape!")
            return "escape"

        else:
            print_delay("Invalid action! Choose attack, heal, or run.")

    return "lose"


def start_game():
    global player_health, terminator_health
    print_delay("Welcome to the Terminator Adventure Game!")
    print_delay("You are on the run from a ruthless Terminator!")

    while player_health > 0:
        print_delay("\nYou find yourself in a dark alley. What will you do?")
        print("Options: [hide, search, run, fight]")

        try:
            choice = input("Enter your choice: ").strip().lower()
        except EOFError:
            print("Error in input. Please try again.")
            continue

        if choice == "hide":
            print_delay("You hide quietly and the Terminator walks past you.")

        elif choice == "search":
            item_found = random.choice(["medkit", "ammo", "nothing"])
            if item_found == "medkit":
                print_delay("You found a medkit! This could come in handy.")
                inventory.append("medkit")
            elif item_found == "ammo":
                print_delay("You found some ammo! It might give you an advantage.")
            else:
                print_delay("You found nothing of use.")

        elif choice == "run":
            if random.choice([True, False]):
                print_delay("You managed to escape to a safer area.")
            else:
                print_delay("The Terminator catches up to you!")
                outcome = fight()
                if outcome == "win":
                    print_delay("Congratulations! You have defeated the Terminator!")
                    break
                elif outcome == "lose":
                    print_delay("Game Over. The Terminator has terminated you.")
                    break
                elif outcome == "escape":
                    print_delay("You managed to escape, but the Terminator is still hunting you.")

        elif choice == "fight":
            outcome = fight()
            if outcome == "win":
                print_delay("Congratulations! You have defeated the Terminator!")
                break
            elif outcome == "lose":
                print_delay("Game Over. The Terminator has terminated you.")
                break

        else:
            print_delay("Invalid choice. Try again.")


start_game()