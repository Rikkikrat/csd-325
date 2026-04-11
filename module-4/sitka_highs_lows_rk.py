# -------------------------------------------------------------
# Name: Rikki Kratochvil
# Date: 04/08/2026
# Assignment: Sitka Weather Menu Program
# Description:
# Allows the user to view high temperatures, low temperatures,
# or both from a CSV weather file. The program continues running
# until the user chooses to exit.
# -------------------------------------------------------------

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

import os

BASE_DIR = os.path.dirname(__file__)
FILENAME = os.path.join(BASE_DIR, 'sitka_weather_2018_simple.csv')


def get_weather_data():
    """Load dates, highs, and lows from the file."""
    dates, highs, lows = [], [], []

    with open(FILENAME) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])

                dates.append(date)
                highs.append(high)
                lows.append(low)

            except ValueError:
                continue

    return dates, highs, lows


def plot_data(dates, highs=None, lows=None, title="Sitka Weather Data"):
    """Plot high, low, or both temperature sets."""
    fig, ax = plt.subplots()

    if highs is not None:
        ax.plot(dates, highs, c='red', label='High Temperatures')

    if lows is not None:
        ax.plot(dates, lows, c='blue', label='Low Temperatures')

    plt.title(title, fontsize=20)
    plt.xlabel('')
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)")
    plt.legend()
    plt.grid(True)

    plt.show()


def display_menu():
    """Show menu choices."""
    print("\n--- Sitka Weather Menu ---")
    print("Highs  - View high temperatures")
    print("Lows   - View low temperatures")
    print("Both   - View highs and lows")
    print("Exit   - Quit program")


def get_valid_choice():
    """Force valid user input."""
    valid_choices = ['highs', 'lows', 'both', 'exit']

    while True:
        choice = input("Enter choice (Highs, Lows, Both, Exit): ").strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please type Highs, Lows, Both, or Exit.")


def try_again():
    """Ask user if they want to continue."""
    while True:
        answer = input("\nWould you like to return to the menu? (yes/no): ").strip().lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            print("\nExiting program... Goodbye!")
            sys.exit()
        else:
            print("Please enter yes or no.")


def main():
    dates, highs, lows = get_weather_data()

    while True:
        display_menu()
        choice = get_valid_choice()

        if choice == 'highs':
            plot_data(dates, highs=highs,
                      title="Daily High Temperatures - 2018")
            if not try_again():
                break

        elif choice == 'lows':
            plot_data(dates, lows=lows,
                      title="Daily Low Temperatures - 2018")
            if not try_again():
                break

        elif choice == 'both':
            plot_data(dates, highs=highs, lows=lows,
                      title="Daily High and Low Temperatures - 2018")
            if not try_again():
                break

        elif choice == 'exit':
            print("\nExiting program... Goodbye!")
            sys.exit()


if __name__ == "__main__":
    main()