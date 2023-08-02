# Treasure Island Project

print("Welcome to Treasure island ")
print ("Your mision is to find the treasure")

path = input("Enter your direction? L, R: \n")

if path == "R":
    print(f'Sorry you choice is  {path}, GAME OVER!!!')
elif path == "L":
    current_wave = input("Enter the water direction? S, W \n")
    if current_wave == "S":
            print(f'Sorry you choice is  {current_wave}, GAME OVER')
    elif current_wave == "W":
            color_type = input("Enter the color type you want to choose from: R, B, Y \n")
            if  color_type == "B":
                print(f'You choice is  {color_type}, GAME OVER')
            elif color_type == "R":
                print(f'You choice is {color_type}, GAME OVER')
            else:
                            
                print(f'You choice is {color_type}, YOU WIN')



