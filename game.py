import random
import math

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

x = random.randint(lower, upper)

total_chance = math.ceil(math.log(upper - lower + 1,2))
print("/n/you've only ", total_chance, " chance to guess the integer!/n")

count = 0
flag = False


while count < total_chance:
    count += 1

    guess = int(input("your guess number is: "))

    if x == guess:
        print("Congratulations you did it in ", count, "try")
        flag = True
        break
    elif x < guess:
        print("your guess is too small")
    elif x<guess:
        print("your guess is too high")


if not flag:
    print("\nThe number is %d", x)
    print("\tBetter Luck Next time!")