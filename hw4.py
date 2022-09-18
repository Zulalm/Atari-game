
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
bottom = []
widths = []
frame = [widths,bottom]
score = 0
action = ""
for i in range(x):
    width = []
    for n in range(y):
        width.append("*")
    widths.append(width)
for k in range(g):
    width_empty = []
    for n in range(y):
        width_empty.append(" ")
    widths.append(width_empty)
for l in range(y):
    bottom.append(" ")
if y % 2 == 0:
    bottom[(y // 2) - 1] = "@"
else:
    bottom[y // 2] = "@"
time = 0
youWon = False
if x == 0:
    youWon = True
while youWon == False:
    if time != 0 and time % 5 == 0:
        if not "*" in widths[-1]:
            widths.pop()
            width_empty = []
            for n in range(y):
                width_empty.append(" ")
            widths.insert(0, width_empty)
        else: break

    for m in frame:
        if m == bottom:
            for row in m:
                print(row, end="")
            print()
        else:
            for item in m:
                for el in item:
                    print(el, end="")
                print()
    print("-"*72)
    action = input("Choose your action!\n")
    action = action.lower()

    if action != "exit":
        time +=1
    if action == "left":
        if bottom.index("@") != 0:
            a = bottom.index("@")
            bottom[a] = " "
            bottom[a-1] = "@"
        else: pass
    if action == "right":
        if bottom.index("@") != len(bottom)-1:
            a = bottom.index("@")
            bottom[a] = " "
            bottom[a+1] = "@"
        else: pass
    if action == "fire":

        distanceInX = len(widths) - 1
        while distanceInX >= 0:
            if widths[distanceInX][bottom.index("@")] == " ":
                widths[distanceInX][bottom.index("@")] = "|"
                for m in frame:
                    if m == bottom:
                        for row in m:
                            print(row, end="")
                        print()
                    else:
                        for item in m:
                            for el in item:
                                print(el, end="")
                            print()
                print("-" * 72)
                widths[distanceInX][bottom.index("@")] = " "
            else: break
            distanceInX -= 1
        for m in range(len(widths)):
            if frame[0][len(widths)-m-1][bottom.index("@")] != " ":
                frame[0][len(widths)-m-1][bottom.index("@")] = " "
                score += 1
                break
        youWon = True
        for ast in widths:
            for asteroid in ast:
                if asteroid != ' ':
                    youWon = False
                    break
        if youWon:
            break
    if action == "exit":
        for m in frame:
            if m == bottom:
                for row in m:
                    print(row, end="")
                print()
            else:
                for item in m:
                    for el in item:
                        print(el, end="")
                    print()
        print("-" * 72)
        break
if action != "exit":
    if youWon:
        print("YOU WON!")
        for m in frame:
            if m == bottom:
                for row in m:
                    print(row, end="")
                print()
            else:
                for item in m:
                    for el in item:
                        print(el, end="")
                    print()
        print("-" * 72)
    if youWon == False:
        print("GAME OVER")
        for m in frame:
            if m == bottom:
                for row in m:
                    print(row, end="")
                print()
            else:
                for item in m:
                    for el in item:
                        print(el, end="")
                    print()
        print("-" * 72)
print("YOUR SCORE:",score)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
