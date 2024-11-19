
---

# Typing Speed Test

This is a Python-based typing speed test application that evaluates your typing speed and accuracy. It calculates your **Words Per Minute (WPM)** and **accuracy** percentage based on the text you type. Your results are saved to a file for future reference.

## Features

- **Typing Accuracy**: Measures the percentage of correctly typed words.
- **Typing Speed (WPM)**: Calculates your typing speed in words per minute.
- **Timed Test**: Tracks the time it takes to type a given sentence.
- **Result Storage**: Saves your test results (name, WPM, accuracy, and time) to a file for later review.
- **Multiple Attempts**: You can take multiple tests and compare your results.

## Requirements

- Python 3.x

## Installation

1. Ensure that Python 3 is installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).
2. Clone or download this repository to your local machine.

## How to Run

1. Navigate to the directory where the script is saved.
2. Open a terminal/command prompt.
3. Run the script by typing:

   ```bash
   python typing_speed_test.py
   ```

4. The program will prompt you to enter your name and provide a sentence to type. Once you finish typing the sentence, it will show your WPM, accuracy, and the time it took to complete the test.
5. Your results will be saved in a file named `typing_test_results.txt`.

## Test Results

The program will save the following information in the results file:

- **Name**: Your name (entered at the beginning of the test)
- **Time Elapsed**: The time you took to type the sentence (in seconds)
- **Accuracy**: Percentage of correct words typed
- **WPM**: Your typing speed in words per minute

### Example of Result in `typing_test_results.txt`:

```
Name: John Doe
Time Elapsed: 30.52 seconds
Accuracy: 95.00%
WPM: 40.50
----------------------------------------
```

## How It Works

1. **Start the Test**: The program selects a random sentence from a list and asks you to type it.
2. **Type the Sentence**: After typing the sentence, the program records the time and compares your input with the original sentence to calculate the accuracy.
3. **Calculate WPM**: The program calculates the number of words typed per minute based on the time it took you to complete the test.
4. **Display Results**: Once you finish typing, your results (accuracy, WPM, and time) are displayed on the screen.
5. **Save Results**: Your results are saved to a file named `typing_test_results.txt` for reference.

## Example Interaction

```
Typing Speed Test
-----------------
Enter your name: Alice
Type the following text:
Python is a popular programming language
Alice: Python is a popular programming language
Accuracy: 100.00%
WPM: 45.67
Time elapsed: 30.12 seconds
Your results have been saved!

Would you like to take the typing test again? (yes/no): no
Thank you for participating! Goodbye!
```

## How to Quit

To exit the program at any point, simply type `no` when asked if you want to take the test again.

## Contributing

If you would like to contribute to this project (bug fixes, improvements, etc.), feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:

- The script assumes you have basic knowledge of running Python scripts. If you encounter any issues or errors, ensure that Python is properly installed on your machine and that you’re running the script in an appropriate environment.
