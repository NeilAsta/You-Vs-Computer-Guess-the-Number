import random
import math

num  = int(random.randint(1,10))
hum_count = 0

#print(num)
#human
user_guess = int(input("What do you think the number is between 1 and 10: "))
hum_count += 1

while True:
    if user_guess > num :
        print("too big.")
        user_guess = int(input("What do you think the number is between 1 and 10: "))
        hum_count += 1
    elif user_guess < num :
        print("Ooh too small")
        user_guess = int(input("What do you think the number is between 1 and 10: "))
        hum_count += 1
    else:
        if hum_count == 1:
            print("Wow that's right! It took you "+ str(hum_count) +" try!")
        else:
            print("Wow that's right! it took you "+ str(hum_count) +" tries.")
        break


#plural(like line 21-24)
#compare

#continue?
print("Do you want to play against the computer playing algorythmicly? yes or no? ")
#accept other answers
answer = input()
answer = answer.lower()

if answer == 'no' or 'n' or 'nah' or 'nope':
    print ("have a good day ")
elif answer == 'yes' or 'y' or 'yep' or 'sure':
    print('let\'s go then!')
#computer    
    comp_num = int(random.randint(1,10))
    #print(comp_num)
    comp_count=0
    comp_count += 1
    LB = 1
    UB = 10
    while True:
        if comp_num == num :
            if comp_count == 1:
                print("The computer did it in " + str(comp_count) + " try. ")
            else:
                print("The computer did it in " + str(comp_count) + " tries. ")
            break
        elif comp_num > num:
            #print('too big')
            UB = comp_num
            comp_num = comp_num/2
            comp_num = math.trunc(comp_num)
            comp_count +=1
            while True:
                if comp_num < LB:
                    comp_num = comp_num + 1
                else:
                    break
            #print(comp_count)
        else:
            #print('too small')
            LB = comp_num
            comp_num = comp_num*2
            comp_num = comp_num + 1
            #print(comp_num)
            if comp_num > 10:
                comp_num = UB - 1
            elif comp_num > UB:
                comp_num = UB -1
            else:
                break
            #print(comp_num)
            comp_count += 1
    if comp_count < hum_count:
        print("Bahaha, why am I unsurprised that I am better than you?")
    elif comp_count == hum_count:
        print("I can\'t believe that we\'re equal, I\'ll beat you next time. ")
    else:
        print("Well done, but I'm sure I will beat you next time")
    #round 2?
else:
    print("I think you might have typed something other than Yes or No")
    