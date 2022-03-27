# import arcade

# arcade.draw_circle_filled(30, 20, 20, arcade.color.AIR_SUPERIORITY_BLUE)
# arcade.draw_rectangle_filled(20, 20, 20, 20, arcade.color.ALABAMA_CRIMSON)

# arcade.draw_circle_filled()


filename = input("File: ") # calling a file
braces = []
balanced = True

with open(filename, "r") as fileIn:
    for brace in fileIn: # read each line
        brace = brace.strip()
        if(brace == "(") or (brace == "[") or (brace == "{"):
            braces.append(brace)
        else:
            if len(braces) == 0: # ) } ] got recieved, so it's not balanced
                balanced = False
                break
            prev_brace = braces.pop()
            if ((brace == "}") and (prev_brace != "{")) or ((brace == ")") and (prev_brace != "(")) or ((brace == "]") and (prev_brace != "[")):
                balanced = False
                break

if len(braces) != 0 or (not balanced): # left overs and balance is False
    print("Not balanced") # used "not"
else:
    print("Balanced")
