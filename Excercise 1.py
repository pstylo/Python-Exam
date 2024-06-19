"""Exercise 1:
Write a Python program to construct the following pattern, using a nested for loop.
(red: output)
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* """

# increasing part
for i2 in range(1,6):
    print(" * " * i2)

#decreasing part
for i in range(4,0,-1):
    print(" * " * i)

print()

#nested loop

total_lines = 9

#outer loop for each line
for i in range(total_lines):
    #determine the number of stars for the current line
    if i < 5:
        num_stars = i + 1 #for the first 5 lines( 0 to 4
    else:
        num_stars = total_lines - i

    for j in range(num_stars):
        print("* ", end = " ")

    print()
