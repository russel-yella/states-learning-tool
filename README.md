# US States Turtle Game 🐢

A Python game where the user guesses U.S. states on a blank map.  
Inspired by the "100 Days of Python" course, it demonstrates Python basics, `pandas`, and `turtle` graphics.

---

## Features

- Interactive guessing game with a visual map
- Displays the state name on the map when guessed correctly
- Keeps track of correctly guessed states
- Exports a CSV of states that were **not guessed** when the user exits
- Uses `pandas` to manage state data from a CSV

---

## How to Run

1. Make sure Python is installed (>= 3.7 recommended)
2. Install dependencies:

```bash
pip install pandas


us-states-turtle-game/
│
├── main.py                 # Game code
├── 50_states.csv           # CSV with state coordinates
├── blank_states_img.gif     # Map image
├── states_to_learn.csv      # Generated CSV with missing states
└── README.md               # Project documentation
