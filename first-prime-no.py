
num = 2

while True:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("First prime number is:", num)
        break

    num = num + 1
