import csv
import random
import os

def read_csv(filename):
    pairs = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                pairs.append(row)
    return pairs

def display_instructions():
    print("\nAvailable keys:")
    print("Enter - Display next cell")
    print("q - Quit program")
    print("\nPress Enter to start...")
    input()

def main():
    filename = 'data.csv'
    if not os.path.exists(filename):
        print(f"Error: {filename} not found in the current directory.")
        return

    pairs = read_csv(filename)
    if not pairs:
        print("Error: No valid data found in the CSV file.")
        return

    display_instructions()

    while True:
        random.shuffle(pairs)
        for index, (a, b) in enumerate(pairs, 1):
            if random.choice([True, False]):
                a, b = b, a

            print(f"\n{index}. {a}")
            user_input = input()

            if user_input.lower() == 'q':
                print("Quitting program. Goodbye!")
                return

            print(f"   {b}")
            user_input = input()

            if user_input.lower() == 'q':
                print("Quitting program. Goodbye!")
                return

        print("\nAll questions have been displayed. Starting over...")

if __name__ == "__main__":
    main()