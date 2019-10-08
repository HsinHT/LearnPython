import random

secret = random.randint(1,10)
flag = True

print('----------------------------------------')
while flag:
        temp = input("guess number (0-9):")
        guess = int(temp)

        if guess == secret:
                print("guess right")
                flag = False
        else:
                if guess > secret:
                        print("guess number too big")
                else:
                        print("guess number too small")
print('----------------------------------------')
print("Game end")
