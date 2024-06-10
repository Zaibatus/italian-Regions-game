import turtle
from turtle import Turtle, Screen
import pandas

FONT = ("Courier", 13, "bold")

screen = Screen()
screen.title("Italian Regions Game")
image = "italia_muta.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Regions_of_Italy.csv")
regions = data.Region.to_list()
print(regions)

regions_guessed = []
regions_missed = []

while len(regions_guessed) < 20:
    answer_region = screen.textinput(title=f"{len(regions_guessed)}/20 Regions Correct", prompt="What's another region name?").title()

    if answer_region == "Exit":
        for region in regions_missed:
            if region not in regions_guessed:
                regions_missed.append(region)
        new_data = pandas.DataFrame(regions_missed)
        new_data.to_csv("regions_to_learn.csv")
        break
    elif answer_region in regions:
        regions_guessed.append(answer_region)
        t = Turtle()
        t.penup()
        t.hideturtle()
        region_data = data[data.Region == answer_region]
        t.goto(int(region_data.x), int(region_data.y))
        t.write(answer_region, align="center", font=FONT)




screen.exitonclick()
