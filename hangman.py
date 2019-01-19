import random








citylist =["delhi","mumbai","ahemdabad","indore","raipur","khandwa","jhansiisnotacity"]


choice='y'
while(choice=="y"):
    city = random.choice(citylist)
    print(city)
    life = 6
    output = []
    for x in range(len(city)):
        output.append("_")

    while (life != 0):
        alpha = input("Enter any alphabet\n")
        poslist = []
        i = 0

        for x in city:
            i += 1
            if x == alpha:
                poslist.append(i - 1)

        if len(poslist) == 0:
            life -= 1
            print("Ohh, guess again")
        else:
            for x in poslist:
                output[int(x)] = alpha

        print(*output)
        print(str(life) + " lives left\n")
        x = "_"
        if x not in output:
            break

    if life > 0:
        print("You Win")
    else:
        print("You lose")
        print("The city was "+ city)

    choice=input("Do you want to play again (y/n)??")







