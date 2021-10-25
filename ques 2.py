#ques 2
def calc_weight_on_planet(weight_Earth,gravity=23.1):
    weight=(weight_Earth/9.8)*gravity
    return weight

w=calc_weight_on_planet(120,23.1)
print(w)