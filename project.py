import time
import random

texts = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a popular programming language",
    "Typing speed and accuracy are essential skills",
    "Practice regularly to improve your typing skills",
    "Consistency is key to mastering typing"
]

def typing_test(text):
    print("Type the following text:")
    print(text)
    start_time = time.time()
    typed_text = input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    accuracy = calculate_accuracy(text, typed_text)
    
    # words per minute (wpm)
    wpm = calculate_wpm(typed_text, elapsed_time)
    
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"WPM: {wpm:.2f}")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    
    return elapsed_time, accuracy, wpm

def calculate_accuracy(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()
    
    correct_words = sum(1 for i in range(min(len(original_words), len(typed_words))) if original_words[i] == typed_words[i])
    return (correct_words / len(original_words)) * 100

def calculate_wpm(typed_text, elapsed_time):
    num_words = len(typed_text.split())
    return (num_words / elapsed_time) * 60

def save_results(name, elapsed_time, accuracy, wpm):
    with open("typing_test_results.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Time Elapsed: {elapsed_time:.2f} seconds\n")
        file.write(f"Accuracy: {accuracy:.2f}%\n")
        file.write(f"WPM: {wpm:.2f}\n")
        file.write("-" * 40 + "\n")

def runcode():
    print("Typing Speed Test")
    print("-----------------")
    name = input("Enter your name: ")
    
    text = random.choice(texts)
    elapsed_time, accuracy, wpm = typing_test(text)
    
    save_results(name, elapsed_time, accuracy, wpm)
    print("Your results have been saved!")
def main():
    while True:
        runcode()
        user_response = input("\nWould you like to take the typing test again? (yes/no): ").strip().lower()
        
        if user_response != 'yes':
            print("Thank you for participating! Goodbye!")
            break  
if __name__ == "__main__":
    main()
