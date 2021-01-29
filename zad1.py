def fkwota():
    global num1
    try:
        num1 = float(input("Podaj kwotę brutto: "))
    except ValueError:
        print("Nie podałeś kwoty lub błędny zapis!")
        exit()
#zaliczka na PIT jest obliczana zgodnie z wzorem na rok 2017, reszta wartości jest aktualna
def pit():
    num4 = num1 - num2                              #num4 to różnica brutto i wartości ubezpieczeń społecznych (potrzebne do obliczenia pitu)
    num5 = (round(num4, 2) - numx) * 0.18 - 46.33   #num5 to podstawa do obliczenia pitu
    num6 = num5 - num4 * 0.0775                     #num6 to zaliczka na pit
    return round(num6, 2)

def netto():
    num3 = num1 - (round(zdrowotne(num1, num2), 2) + num2 + pit())      #num3 to wartość netto
    return round(num3, 2)

def emerytalne(x):
    return round(x * 0.0976, 2)

def rentowe(x):
    return round(x * 0.015, 2)

def chorobowe(x):
    return round(x * 0.0245, 2)

def zdrowotne(x, y):
    return round((x - y) * 0.09, 2)

print("Kalkulator płacy brutto")                    #Z netto na brutto ciężko przeliczyć pod względem matematycznym, o ile w ogóle się da
wybor1 = input("\nCzy pracujesz w miejscowości gdzie mieszkasz?(tak/nie): ")

if wybor1 in ('tak', 'nie'):
    if wybor1 == 'tak':
        numx = 111.25
    elif wybor1 == 'nie':
        numx = 139.06

if wybor1 in ('tak', 'nie'):
    num1 = 0
    fkwota()
    num2 = emerytalne(num1)+rentowe(num1)+chorobowe(num1)       #num2 to wartość ubezpieczeń społecznych

    print("\nKoszt ubezpieczenia emerytalnego", emerytalne(num1)," PLN")
    print("Koszt ubezpieczenia rentowego", rentowe(num1)," PLN")
    print("Koszt ubezpieczenia chorobowego", chorobowe(num1)," PLN")
    print("Koszt ubezpieczenia zdrowotnego", zdrowotne(num1, num2)," PLN")
    print("Zaliczka na PIT: ", pit(), " PLN")
    print("Kwota w netto", netto(), " PLN")
else:
    print("Wybrałeś niepoprawną opcję")