# Rikki Kratochvil
# March 22, 2026
# Assignment 1.3 - Bottles of Beer Countdown
# Purpose: Ask the user for the number of bottles and count down the song.

def countdown_song(bottle_count):
    """Count backwards from the given number of bottles to 1."""
    
    while bottle_count > 1:
        print(f"{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer.")
        
        if bottle_count - 1 == 1:
            print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
        else:
            print(f"Take one down, pass it around, {bottle_count - 1} bottles of beer on the wall.\n")
        
        bottle_count -= 1

    # Special ending when only 1 bottle remains
    if bottle_count == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down, pass it around, no more bottles of beer on the wall.\n")


def main():
    """Main program function."""
    
    print("Welcome to the Bottles of Beer Countdown Program!")
    
    # Get the starting number of bottles from the user
    starting_bottles = int(input("How many bottles of beer are on the wall? "))

    # Pass the user input to the countdown function
    countdown_song(starting_bottles)

    # Return to main program and remind user to buy more beer
    print("Time to buy more beer!")


# Run the main function
main()