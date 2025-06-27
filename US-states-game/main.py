import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
image = "./US-states-game/blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)



states_data = pandas.read_csv("./US-states-game/50_states.csv")
states_data_list = states_data.state.to_list()

guessed_states = []
n = 0
game_is_on = True

while game_is_on == True:
        
    answer_state = my_screen.textinput(f"{n}/50 States Correct", "What's another state?").title()
    
    if answer_state == "Exit":
        break
    
    if answer_state in states_data_list and answer_state not in guessed_states:
        n += 1
        guessed_states.append(answer_state)
        # state_coor = states_data[states_data["state"] == answer_state]
        ind = states_data_list.index(answer_state)
        state_coor_x = states_data.at[ind, "x"]
        state_coor_y = states_data.at[ind, "y"]
        state_writing = turtle.Turtle()
        state_writing.hideturtle()
        state_writing.pu()
        state_writing.goto((state_coor_x, state_coor_y))
        state_writing.write(answer_state)  
        
    if n == 50:
        game_is_on = False     


# missing states csv
remaining_states = [state for state in states_data_list if state not in guessed_states]
# remaining_states = []
# for state in states_data_list:
#     if state not in guessed_states:
#         remaining_states.append(state)

remaining_states_dict = {"state": remaining_states}
df = pandas.DataFrame(remaining_states_dict)
df.to_csv("./US-states-game/missing_states.csv")
# setA = set(states_data_list)
# setB = set(guessed_states)
# remaining_states = setA.difference(setB)



# turtle.mainloop()
