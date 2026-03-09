import turtle
import pandas
IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US states")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


df= pandas.read_csv("50_states.csv")
data_dict = df.set_index("state").to_dict(orient="index")
print(data_dict)

guessed_states = []

while len(guessed_states) < 50:

   answer_state = screen.textinput(f"You have Guessed {len(guessed_states)}/50", "Enter a state").title()

   if answer_state == "Exit":
         missing_states = [state for state in data_dict if state not in guessed_states]
         pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
         break

   if answer_state in data_dict and answer_state not in guessed_states:
      coords = data_dict[answer_state]

      writer = turtle.Turtle()
      writer.hideturtle()
      writer.penup()
      writer.goto(coords["x"], coords["y"])
      writer.write(answer_state)

      guessed_states.append(answer_state)


screen.exitonclick()







