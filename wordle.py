import requests
import random
from collections import Counter

def get_words_from_api():
    try:
        url = "https://api.datamuse.com/words"
        params = {"sp": "?????"}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        print(f"Error in request: {e}")
        return []
    
    words = response.json()
    return [word['word'] for word in words if len(word['word']) == 5]

def get_user_guess():
    while True:
        guess = input("Take your guess (5 letters only): ")
        if len(guess) != 5 or not guess.isalpha():
            print("Guesses must be 5 letters long and contain only letters.")
        else:
            return guess.lower()  # Convert guess to lowercase to handle case-insensitivity

def get_feedback(guess, solution):
    feedback = []
    
    # Count occurrences of letters in guess and solution
    guess_counts = Counter(guess)
    solution_counts = Counter(solution)
    
    # First, find correct letters and update guess_counts
    for g, s in zip(guess, solution):
        if g == s:
            feedback.append(g)
            guess_counts[g] -= 1  # Decrement count since it's a correct guess
            if guess_counts[g] <= 0:
                del guess_counts[g]  # Remove letter from guess_counts if count is zero
        else:
            feedback.append('_')
    
    # Now check for misplaced letters and give feedback
    for i in range(len(feedback)):
        if feedback[i] == '_' and guess[i] in solution_counts and guess_counts.get(guess[i], 0) > 0:
            feedback[i] = '?'  # or any other symbol you'd like to use for misplaced letters
            guess_counts[guess[i]] -= 1  # Decrement count since it's identified as misplaced
            if guess_counts[guess[i]] <= 0:
                del guess_counts[guess[i]]  # Remove letter from guess_counts if count is zero
    
    return feedback

def main_game_loop():
    five_letter_words = get_words_from_api()
    if not five_letter_words:
        print("Couldn't fetch words. Please try again later.")
        return

    solution = random.choice(five_letter_words)
    print("Welcome to Wordle! You have 6 attempts to guess the right 5-letter word!")

    for guesses in range(1, 7):
        print(f"Attempt {guesses}")
        user_guess = get_user_guess()
        feedback = get_feedback(user_guess, solution)
        
        if feedback == list(solution):
            print("Winner!")
            return
        else:
            print(f"Result: {' '.join(feedback)}")
    
    print(f"Loser! The word was {solution}")

if __name__ == "__main__":
    main_game_loop()  # This starts the game



# import tkinter as tk
# from tkinter import messagebox
# import requests
# import random
# from collections import Counter

# class WordleGame(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Wordle Game")
#         self.geometry("400x400")

#         self.label = tk.Label(self, text="Welcome to Wordle! Guess the right 5-letter word!")
#         self.label.pack()

#         self.attempt_label = tk.Label(self, text="Attempt 1")
#         self.attempt_label.pack()

#         self.entry = tk.Entry(self)
#         self.entry.pack()

#         self.button = tk.Button(self, text="Guess", command=self.on_guess)
#         self.button.pack()

#         self.result_label = tk.Label(self, text="")
#         self.result_label.pack()

#         # Initialize your game here...
#         self.five_letter_words = self.get_words_from_api()
#         self.solution = random.choice(self.five_letter_words)
#         self.attempts = 1

#     def get_words_from_api(self):
#         try:
#             url = "https://api.datamuse.com/words"
#             params = {"sp": "?????"}
#             response = requests.get(url, params=params)
#             response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
#         except requests.RequestException as e:
#             messagebox.showinfo(f"Error in request: {e}")
#             return []
        
#         words = response.json()
#         return [word['word'] for word in words if len(word['word']) == 5]
#         # ... (same as your existing function)
#         # Replace 'print' statements with 'messagebox.showerror' or 'messagebox.showinfo' to display errors or info

#     def on_guess(self):
#         guess = self.entry.get().lower()
#         if len(guess) != 5 or not guess.isalpha():
#             messagebox.showinfo("Error", "Guesses must be 5 letters long and contain only letters.")
#             return
        
#         feedback = self.get_feedback(guess, self.solution)

#         if feedback == list(self.solution):
#             messagebox.showinfo("Winner!", "Congratulations, You Win!")
#             self.reset_game()
#         else:
#             self.result_label.config(text=f"Result: {' '.join(feedback)}")
#             self.attempts += 1
#             self.attempt_label.config(text=f"Attempt {self.attempts}")
#             if self.attempts > 6:
#                 messagebox.showinfo("Loser!", f"The word was {self.solution}")
#                 self.reset_game()

#     def get_feedback(self, guess, solution):

#         feedback = []
        
#         # Count occurrences of letters in guess and solution
#         guess_counts = Counter(guess)
#         solution_counts = Counter(solution)
        
#         # First, find correct letters and update guess_counts
#         for g, s in zip(guess, solution):
#             if g == s:
#                 feedback.append(g)
#                 guess_counts[g] -= 1  # Decrement count since it's a correct guess
#                 if guess_counts[g] <= 0:
#                     del guess_counts[g]  # Remove letter from guess_counts if count is zero
#             else:
#                 feedback.append('_')
        
#         # Now check for misplaced letters and give feedback
#         for i in range(len(feedback)):
#             if feedback[i] == '_' and guess[i] in solution_counts and guess_counts.get(guess[i], 0) > 0:
#                 feedback[i] = '?'  # or any other symbol you'd like to use for misplaced letters
#                 guess_counts[guess[i]] -= 1  # Decrement count since it's identified as misplaced
#                 if guess_counts[guess[i]] <= 0:
#                     del guess_counts[guess[i]]  # Remove letter from guess_counts if count is zero
        
#         return feedback

#     def reset_game(self):
#         # You can add logic here to start a new game
#         # For example, select a new word, reset the attempts counter, etc.
#         self.attempts = 1
#         self.attempt_label.config(text=f"Attempt {self.attempts}")
#         self.solution = random.choice(self.five_letter_words)
#         self.result_label.config(text="")
#         self.entry.delete(0, tk.END)

# if __name__ == "__main__":
#     app = WordleGame()
#     app.mainloop()