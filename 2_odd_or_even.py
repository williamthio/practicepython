num = int(input("Number: "))
check = int(input("Check: "))

if num % 4 == 0:
    print("{} is a multiple of 4".format(num))
elif num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

if num % check == 0:
    print("{} divides evenly by {}".format(num, check))
else:
    print("{} does not divides evenly by {}".format(num, check))
