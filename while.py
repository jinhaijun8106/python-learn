num = 23
while 1:
    guess = int(input("Enter an integer "));
    if guess == num:
        print("same");
        break;
    elif guess < num:
        print("the num is bigger");
    else:
        print("the num is smaller");
print("done", guess, num);
print("done, added in mainline", guess, num);
