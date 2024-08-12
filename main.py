import turtle
import pandas

screen = turtle.Screen()
screen.title('US State Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
writer = turtle.Turtle()
writer.pu()
writer.speed(0)
writer.hideturtle()

game_on = True
data = pandas.read_csv('50_states.csv')
points = 0
states = data['state']
states_list = []
for i in states:
    states_list.append(i.lower())
print(states_list)

x_coordinates = data['x']
y_coordinates = data['y']
coordinates_list = []
for i in range(0,50):
    coordinates_list.append((x_coordinates[i],y_coordinates[i]))
print(coordinates_list)

while game_on:
    if len(states_list) == 0:
        game_on = False

    if points == 0:
        answer = screen.textinput(title='Guess the state', prompt='Whats another states name?').lower()
    else:
        answer = screen.textinput(title=f'States Guessed {points}/50', prompt='Whats another states name?').lower()

    if answer == 'exit':
        break

    if answer in states_list:
        points += 1
        index = states_list.index(answer)
        location = coordinates_list[index]
        writer.goto(location)
        writer.write(arg=answer.title(), align='center')
        states_list.remove(answer)
        coordinates_list.pop(index)
    else:
        pass

missing_states_dict = {
    'missing': states_list
}

missing_states = pandas.DataFrame(missing_states_dict)
missing_states.to_csv('missing states')
