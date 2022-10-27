import math


def Szescian():
    a = input("podaj bok \n: ")
    a = float(a)
    print("\nPole =",6*a**2,"cm^2")
    print("Objętość =",a**3,"cm^3")

def Prostopadloscian():
    a = input("podaj bok a \n: ")
    a = float(a)
    b = input("podaj bok b \n: ")
    b = float(b)
    c = input("podaj bok c \n: ")
    c = float(c)
    print("\nPole =",(2*a*b) + (2*a*c) + (2*b*c),"cm^2")
    print("Objętość =",a*b*c,"cm^3")

def Graniastoslup():
    Pp = input("podaj Pole Podstawy \n: ")
    Pp = float(Pp)
    Pb = input("podaj Pole Boczne \n: ")
    Pb = float(Pb)
    H = input("podaj Wysokość \n: ")
    H = float(H)
    print("\nPole =",2*Pp + Pb,"cm^2")
    print("Objętość =",Pp*H,"cm^3")

def Ostroslup():
    Pp = input("podaj Pole Podstawy \n: ")
    Pp = float(Pp)
    Pb = input("podaj Pole Boczne \n: ")
    Pb = float(Pb)
    H = input("podaj Wysokość \n: ")
    H = float(H)
    print("\nPole =",Pp + Pb,"cm^2")
    print("Objętość =",(Pp*H)/3,"cm^3")

def Walec():
    r = input("podaj Promień podstawy \n: ")
    r = float(r)
    H = input("podaj Wysokość \n: ")
    H = float(H)
    print("\nPole =",(2*math.pi*r) + (2*math.pi*H),"cm^2")
    print("Objętość =",(math.pi*r**2*H)/3,"cm^3")

def Stozek():
    r = input("podaj Promień podstawy \n: ")
    r = float(r)
    l = input("podaj bok l \n: ")
    l = float(l)
    H = input("podaj Wysokość \n: ")
    H = float(H)
    print("\nPole =",(math.pi*r **2) + (2*math.pi*l),"cm^2")
    print("Objętość =",math.pi*r**2*H,"cm^3")

def Kula():
    r = input("podaj Promień podstawy \n: ")
    r = float(r)
    print("\nPole =",4*math.pi*r**2,"cm^2")
    print("\nObjętość =",(4/3)*math.pi*r**3,"cm^3")

#=============================================================================

def Kwadrat():
    a = input("podaj bok \n: ")
    a = float(a)
    print("\nPole =",a**2,"cm^2")
    print("Obwód =",4*a,"cm")

def Prostokat():
    a = input("podaj bok a \n: ")
    a = float(a)
    b = input("podaj bok b \n: ")
    b = float(b)
    print("\nPole =",a*b,"cm^2")
    print("Obwód =",(a*2)+(b*2),"cm")

def Rownoleglobok():
    a = input("podaj Bok a \n: ")
    a = float(a)
    b = input("podaj Bok b \n: ")
    b = float(b)
    h = input("podaj Wysokość \n: ")
    h = float(h)
    print("\nPole =",a*h,"cm^2")
    print("Obwód =",(a+b)*2,"cm")

def Trapez():
    a = input("podaj Bok a \n: ")
    a = float(a)
    b = input("podaj Bok b \n: ")
    b = float(b)
    c = input("podaj Bok c \n: ")
    c = float(c)
    d = input("podaj Bok d \n: ")
    d = float(d)
    h = input("podaj Wysokość \n: ")
    h = float(h)
    print("\nPole =",((a+b)*h)/2,"cm^2")
    print("Obwód =",a+b+c+d,"cm")
                
def Trojkat():
    a = input("podaj podaj Bok a \n: ")
    a = float(a)
    b = input("podaj podaj Bok b \n: ")
    b = float(b)
    c = input("podaj podaj Bok c \n: ")
    c = float(c)
    h = input("podaj Wysokość \n: ")
    h = float(h)
    print("\nPole =",a*h/2,"cm^2")
    print("Obwód =",a+b+c,"cm")

def Trojkat_Rownoboczny():
    a = input("podaj podaj Bok a \n: ")
    a = float(a)
    print("\nPole =",a**2*3**(1/2)/4,"cm^2")
    print("Obwód =",a*3,"cm")

def Kolo():
    r = input("podaj Promień podstawy \n: ")
    r = float(r)
    print("\nPole =",math.pi*(r**2),"cm^2")
    print("Obwód =",2*math.pi*r,"cm")

def Romb():
    a = input("podaj Bok a \n: ")
    a = float(a)
    h = input("podaj Wysokość \n: ")
    h = float(h)
    print("\nPole =",a*h,"cm^2")
    print("Obwód =",a*4,"cm")

while True:
    wybor=input("A=Figury 3d  B=Figury 2d C=Dodatkowe wzory \n: ")

    if wybor == "A":
        wybor1 = input("A = sześcian | B = Prostopadłościan | C = Graniastosłup | D = Ostrosłup | E = Walca | F = Stożka | G = Kuli \n: ")
        if wybor1 == "A":
            Szescian()

        if wybor1 == "B":
            Prostopadloscian()

        if wybor1 == "C":
            Graniastoslup()

        if wybor1 == "D":
            Ostroslup()

        if wybor1 == "E":
            Walec()

        if wybor1 == "F":
            Stozek()    

        if wybor1 == "G":
            Kula()

    if wybor == "B":
        wybor1 = input("A = Kwadrat | B = Prostokąt | C = Równoległobok | D = Trapez | E = Trójkąt | F = Trójkąt równoboczny | G = Koło | H = Romb \n: ")

        if wybor1 == "A":
            Kwadrat()
        if wybor1 == "B":
            Prostokat()
        if wybor1 == "C":
            Rownoleglobok()
        if wybor1 == "D":
            Trapez()
        if wybor1 == "E":
            Trojkat()
        if wybor1 == "F":
            Trojkat_Rownoboczny()
        if wybor1 == "G":
            Kolo()
        if wybor1 == "H":
            Romb()