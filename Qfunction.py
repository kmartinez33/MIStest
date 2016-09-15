def quadratic():
    from math import sqrt
    a = int(input("first coefficient?"))
    b = int(input("second coefficient?"))
    c = int(intput("third coefficient?"))
    print()
    formula = b**2 - 4*a*c #b squared-4ac
    b_value = sqrt(formula) #value of the discriminant
    positive_value = (-b + b_value)/ (2*a) # there is a positve value and a negative value for answer
    negative_value = (-b - b_value)/ (2*a)

    print("Positive value of the quadratic equation is {0}, and the negative value is {1}".format(positve_value,negative_value))
    print(quadratic(3))
    print(quadratic(8))
    print(quadratic(-3))

#if an error comes up that says math domain error, it is bc the value of the discrimant is negative. 
#The value of the discrimant has to be greater than zero bc you cant do the squareroot of a negative integer

input()