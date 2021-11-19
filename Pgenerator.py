import string, random
#string : module that provide a colection of string CONSTANTS 


l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

#shuffle (take a list and shuffle it, دالة تتخلط)
random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)

def main():
    passwordLenght = input("how many characters? \n ")   

    #Handling Error Inputs
    while True:
        try:
            passwordLenght = int(passwordLenght)
            if passwordLenght < 6 or passwordLenght > 20 :
                passwordLenght = input("Please enter a number between 6 and 20 \n")

            else: 
                break

        except:
            passwordLenght = input("please enter a valid number!\n") 
            
    #part1 40% of the characters   part2 10% of the characters 
    part1 = int(round(passwordLenght*(40/100)))
    part2 = int(round(passwordLenght*(10/100)))


    password = []

    for i in range(part1):
        password.append(l1[i])
        password.append(l2[i])

    for i in range(part2):
        password.append(l3[i])
        password.append(l4[i])


    random.shuffle(password)

    password = "".join(password[0:])


    print(password)


main()