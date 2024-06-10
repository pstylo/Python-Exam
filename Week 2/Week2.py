"""Task 1:  (if, else, elif ….)
Write a program that asks the employee for a number between 0 and 7. The number is to serve as a
substitute for a day:
0 = Monday, 1 = Tuesday, ........, 7 = Sunday
The program should then display a message (depending on the input!) on the screen to the
employee, whether he
a) "You have to work ...!
b) "Enjoy the time now ...!
c) "Wrong input...!"
(for Monday to Friday)
(for Saturday and Sunday)
(for wrong number)"""




Day = int(input("Enter a number between 0 to 7: 0 ,0 = Monday, 1 = Tuesday, ........, 7 = Sunday: "))


if Day == 0 or Day == 1 or Day == 2 or Day == 3 or Day == 4:
        print("You have to work")
elif Day == 5 or Day == 6:
        print("Enjoy the time")
else:
        print("Wrong input")


"""Write a Python program to convert temperatures to and from celsius, fahrenheit. 
Python: Centigrade and Fahrenheit Temperatures : 
The centigrade scale, which is also called the Celsius scale, was developed by Swedish astronomer 
Andres Celsius. In the centigrade scale, water freezes at 0 degrees and boils at 100 degrees. The 
centigrade to Fahrenheit conversion formula is: 
Fahrenheit and centigrade are two temperature scales in use today. The Fahrenheit scale was 
developed by the German physicist Daniel Gabriel Fahrenheit . In the Fahrenheit scale, water freezes 
at 32 degrees and boils at 212 degrees. """

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (5/9) * (fahrenheit -32)


print(f"The temperature in Celsius is {celsius} degrees")


