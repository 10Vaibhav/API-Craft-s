# Quizzler

Quizzler is a simple quiz application with a graphical user interface built using Python and Tkinter. It fetches quiz questions from the Open Trivia Database API and presents them to the user in a True/False format.

## Features

- Fetches quiz questions from the Open Trivia Database API
- Presents questions in a user-friendly GUI
- Keeps track of the user's score
- Provides immediate feedback on answers
- Supports multiple questions in a single quiz session

## Requirements

- Python 3.x
- requests library
- tkinter library


## Files

- `main.py`: The entry point of the application
- `data.py`: Handles fetching quiz data from the API
- `question_model.py`: Defines the Question class
- `quiz_brain.py`: Contains the main quiz logic
- `ui.py`: Implements the graphical user interface


## How It Works

1. The app fetches questions from the Open Trivia Database API.
2. Questions are converted into Question objects.
3. A QuizBrain manages the quiz logic (tracking questions, score, etc.).
4. The GUI (QuizInterface) displays questions and handles user input.
5. Users answer by clicking True or False buttons.
6. The app provides immediate feedback and moves to the next question.
7. After all questions are answered, the final score is displayed.


## Contributing

Contributions, issues, and feature requests are welcome.
