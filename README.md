# Bagels - A Deductive Logic Game 🕵️‍♂️🎲

Bagels is a fun Python-based deductive logic game where you try to guess a secret number based on clues.

## How to Play

- The computer thinks of a **3- or 4-digit number** with no repeated digits.
- You have a limited number of guesses (default: 10).
- After each guess, you receive clues:
  - **Fermi** 🔹: One digit is correct and in the right position.
  - **Pico** 🟡: One digit is correct but in the wrong position.
  - **Bagels** ⚪: No digit is correct.
- You can type `"quit"` at any time to exit the game.

**Example:**

Secret number: `248`  
Your guess: `843`  
Clues: `Fermi Pico`  

---

## Features

- Input validation to ensure correct guesses
- Color-coded clues for better readability
- Emoji feedback for wins and losses
- Quit option to exit anytime
- Easy to run in terminal/command prompt

---

## How to Run

```bash
python bagels.py
