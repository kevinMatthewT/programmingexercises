def calc_new_height():
    w=eval(input("Enter the current width: "))
    h = eval(input("Enter the current height: "))
    w2=eval(input("Enter the desired width: "))
    h2=(w/h)*w2
    h3=round(h2,0)
    print("The corresponding height is:",h3)
    print(h3)

print(calc_new_height())
