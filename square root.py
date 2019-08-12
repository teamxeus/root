#program to find the square root
root = 1.0
value = eval(input("Enter a number:"))
diff = root * root - value
while diff > 0.0001 or diff < -0.0001:
    root = (root + value / root) / 2.0
    diff = root * root - value
print("The square root of ",value," is ",root)
delay = input("Press enter to exit")
