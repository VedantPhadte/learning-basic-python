numbers = [5,3,4,2]

for count in numbers:
    print("x"*count)

#or

for x_count in numbers:
    output = ''
    for y_count in range(x_count):
        output += "x"
    print(output)