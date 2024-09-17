# testLearn

## Overview

So based on few studies bout testing as a method of learning enchancement (i.e.: "The 'testing' phenomenon: Not gone but nearly forgotten (Journal of Educational Psychology)", "The Power of Testing Memory: Basic Research and Implications for Educational Practice" (Perspectives on Psychological Science), "Testing Improves Performance as Well as Assesses Learning: A Review of the Testing Effect with Implications for Models of Learning" (Journal of Experimental Psychology: Animal Learning and Cognition)) I made this simple program (as a learning tool) which reads a CSV file and displays its contents in a randomized order through a command-line interface. It's designed to work with CSV files that contain two columns (e.g. column A containing names of ideas, concepts, dates etc., and column B containing related definitions or concepts), allowing users to test themselves by reviewing pairs of related information in an interactive manner.

## Features

- Reads data from a 'data.csv' file in the same directory as the program
- Displays content from CSV cells in random order
- Randomly selects which column (A or B) to display first for each pair
- Shows pair number before displaying each pair
- Allows user interaction via keyboard input
- Loops back to the beginning after displaying all pairs
- Simple command-line interface

## Prerequisites

- Python 3.x installed on your system
- A CSV file named 'data.csv' in the same directory as the program

## Usage

1. Ensure you have a 'data.csv' file in the same directory as the program. The CSV file should have two columns, like this:

   ```
   Column A,Column B
   Apple,Red fruit
   Car,Vehicle
   Python,Programming language
   ```

2. Run the program from the command line:

   ```
   python csv_display.py
   ```

3. Follow the on-screen instructions:
   - Press Enter to display the next cell
   - Press 'q' and Enter to quit the program

## How It Works

1. The program reads the 'data.csv' file.
2. It shuffles the order of the pairs.
3. For each pair, it randomly decides which column to display first.
4. It displays the content of the first chosen cell and waits for user input.
5. After the user presses Enter, it displays the content of the other cell in the pair.
6. This process continues until all pairs have been displayed or the user quits.
7. If all pairs are displayed, the program starts over with a new random order.

## Error Handling

- If 'data.csv' is not found in the current directory, an error message will be displayed.
- If the CSV file is empty or doesn't contain valid data, an error message will be shown.

## Customization

You can modify the `testLearn.py` file to change the behavior of the program. For example, you could:

- Change the name of the CSV file it looks for
- Modify the display format of the pairs
- Add additional user commands

## License

This program is open-source and free to use, modify, and distribute.

---

Enjoy using it!
