def Generator(x):
    temp = ""
    j = 0

    while j < len(x):
        flag = 0
        count = 1
        digit = x[j]

        while flag == 0:
            if j + 1 < len(x):
                if x[j + 1] == x[j]:
                    j = j + 1
                    count = count + 1
                else:
                    flag = 1
            else:
                flag = 1

        temp = temp + str(count) + digit
        j = j + 1
    
    return temp


print("LOOK AND SAY SERIES GENERATOR")

x = input("Number you want to start the series with:    ")
y = int(input("Length of the series:    "))

for i in range(y):
    x = Generator(x)
    print(x)


    



