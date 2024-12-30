# Le counters for males and females
M = 0
F = 0

while True:
    # Le Display prompt und input name
    print("Name:")
    Name = input()

    # Le Display prompt und input gender
    print("Gender ('M' or 'F'):")
    Gender = input().strip().upper()

    # Validate if gender input is cap
    while Gender not in ['M', 'F']:
        print("Invalid gender entered. Enter again.")
        Gender = input().strip().upper()

    # Le update stuff
    if Gender == 'M':
        M += 1
    elif Gender == 'F':
        F += 1

    # Ask users if they want to goon or be walter white
    print("Enter another set of data? ('Y' or 'N'):")
    Ans = input().strip().upper()

    # Validate if the answer is skibidi cappin'
    while Ans not in ['Y', 'N']:
        print("Invalid answer entered. Enter again.")
        Ans = input().strip().upper()

    # Terminate if the answer is 'N' 
    # if answer is 'Y' go back to ohio
    if Ans == 'N':
        break

# Display le scoreboard
print("Number of Males:", M)
print("Number of Females:", F)
