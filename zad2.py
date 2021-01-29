def fkwota():
    global num1
    try:
        num1 = float(input("\nPodaj kwotę brutto: "))
    except ValueError:
        print("Nie podałeś kwoty lub błędny zapis!")
        exit()

def emerytalne(x):
    return round(x * 0.0976, 2)

def rentowe(x):
    return round(x * 0.065, 2)

def wypadkowe(x):
    return round(x * 0.0167, 2)

def fundusz_pracy(x):
    return round(x * 0.0245, 2)

def fgsp(x):
    return round(x * 0.001, 2)

def lacznie():
    y = emerytalne(num1) + rentowe(num1) + wypadkowe(num1) + fundusz_pracy(num1) + fgsp(num1)
    return y
num1 = 0
print("Kalkulator kosztów pracodawcy")
fkwota()

print("\nKoszt ubezpieczenia emerytalnego", format(emerytalne(num1), '.2f')," PLN")
print("Koszt ubezpieczenia rentowego", format(rentowe(num1), '.2f')," PLN")
print("Koszt ubezpieczenia wypadkowego", format(wypadkowe(num1), '.2f')," PLN")
print("Koszt składki na Fundusz Pracy", format(fundusz_pracy(num1), '.2f')," PLN")
print("Koszt składki na Fundusz Gwarantowanych Świadczeń Pracowniczych: ", format(fgsp(num1), '.2f'), " PLN")
print("\nPłaca pracownika wynosi: ", format((num1), '.2f')," PLN, opłaty na pracownika to: ", format(lacznie(), '.2f')," PLN,")
print("a łączna kwota przeznaczona na pracownika to: ", lacznie() + num1," PLN.")