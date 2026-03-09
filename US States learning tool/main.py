import turtle
import pandas

# Setup screen and map
IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Load state data
df = pandas.read_csv("50_states.csv")
data_dict = df.set_index("state").to_dict(orient="index")

guessed_states = []

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Main game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/50 States Correct",
        "Enter a state"
    )

    # Handle Cancel
    if answer_state is None:
        break

    answer_state = answer_state.title()

    # Exit game and save missing states
    if answer_state == "Exit":
        missing_states = [state for state in data_dict if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    # Correct guess
    if answer_state in data_dict and answer_state not in guessed_states:
        coords = data_dict[answer_state]
        writer.goto(coords["x"], coords["y"])
        writer.write(answer_state)
        guessed_states.append(answer_state)

# Close on click
screen.exitonclick()
