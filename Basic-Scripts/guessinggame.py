import random
def start(limit, chances):
    number = random.randint(1, limit)
  
    while chances > 0:
        guess = int(input())
        if guess == number:
            print("HOORAY YOU WON!!!")
            win = True
            break

        chances -= 1

    if win is not True:
        print("YOU LOSE!!! The number is", number)


if __name__ == "__main__":
    print("Number guessing game")
    limit = int(input("Enter range of number: "))
    chances = int(input("Enter the number of chances: "))
    print("Guess a number (between 1 and your range): ")
    start(limit, chances)