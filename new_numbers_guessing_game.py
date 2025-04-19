import random
import PySimpleGUI as sg

# Step 1: Generate the number
secret_number = random.randint(1, 100)
tries = 0

# Step 2: Build the GUI layout
layout = [
    [sg.Text("Guess a number between 1 and 100:")],
    [sg.Input(key='-GUESS-')],
    [sg.Button("Submit")],
    [sg.Text("", key='-FEEDBACK-')]
]

window = sg.Window("Number Guesser", layout)

# Step 3: Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Submit":
        try:
            guess = int(values['-GUESS-'])
            tries += 1

            diff = abs(guess - secret_number)

            if guess == secret_number:
                window['-FEEDBACK-'].update(f"You guessed it in {tries} tries!")
                # Optional: write to score file here
            elif diff > 20:
                window['-FEEDBACK-'].update("Cold!")
            elif 10 < diff <= 20:
                window['-FEEDBACK-'].update("Warm!")
            else:
                window['-FEEDBACK-'].update("Hot!")

        except ValueError:
            window['-FEEDBACK-'].update("Please enter a valid number.")

window.close()
