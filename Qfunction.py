def quadratic():
    from math import sqrt
    a = int(input("input first coefficient?")) #can also put float if you want a decimal number
    b = int(input("input second coefficient?"))
    c = int(input("input third coefficient?"))
    print()
    formula = b**2 - 4*a*c #b squared-4ac
    b_value = sqrt(formula) #value of the discriminant
    positive_value = (-b + b_value)/ (2*a) # there is a positve value and a negative value for answer
    if positive_value >= 0:
        pass
    negative_value = (-b - b_value)/ (2*a)
    if negative_value <= 1:
        pass

    print("Positive value of the quadratic equation is {0}, and the negative value is {1}".format(positve_value,negative_value))
print(quadratic())

#if an error comes up that says math domain error, it is bc the value of the discrimant is negative. 
#The value of the discrimant has to be greater than zero bc you cant do the squareroot of a negative integer

input()