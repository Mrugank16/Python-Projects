import random
again=True

while again:
    print(random.randint(1,6))
    another=input("roll again? (y/n): ")
    if another.lower()=="y":
        continue
    else:
        break
