def ftemp():
    global temp
    try:
        temp = float(input("Podaj wartość temperatury do przeliczenia: "))
    except ValueError:
        print("Nie podałeś wartości temperatury lub błędny zapis!")
        exit()

def ctf(x):
    f = x * 1.8 + 32
    if f <= 32:
        return print(x, "°C to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze zamarza")
    elif f >= 212:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(f, 2), "°F")

def ftc(x):
    c = (x - 32) / 1.8
    if c <= 0:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze zamarza")
    elif c >= 100:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(c, 2), "°C")

def ktf(x):
    f = x * 1.8 - 459.67
    if f <= 32:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze zamarza")
    elif f >= 212:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(f, 2), "°F, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(f, 2), "°F")

def ftk(x):
    k = (x + 459.67) * 5 / 9
    if k <= 273.15:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze zamarza")
    elif k >= 373.15:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°F to po przeliczeniu", '%+d' % round(k, 2), "K")

def ktc(x):
    c = x - 273.15
    if c <= 0:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze zamarza")
    elif c >= 100:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(c, 2), "°C, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "K to po przeliczeniu", '%+d' % round(c, 2), "°C")

def ctk(x):
    k = x + 273.15
    if k <= 273.15:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze zamarza")
    elif k >= 373.15:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(k, 2), "K, woda w tej temperaturze paruje")
    else:
        return print('%+d' % x, "°C to po przeliczeniu", '%+d' % round(k, 2), "K")

print("Przelicznik temperatur")
print("\nWybierz sposób zamiany")
print("1)Celsjusze na Farenheity")
print("2)Farenheity na Celsjusze")
print("3)Kelwiny na Farenheity")
print("4)Farenheity na Kelwiny")
print("5)Kelwiny na Celsjusze")
print("6)Celsjusze na Kelwiny")

opcja = input("\nWybierz sposób: ")
if opcja in ('1', '2', '3', '4', '5', '6'):
    temp = 0
    if opcja == '1':
        ftemp()
        ctf(temp)
    elif opcja == '2':
        ftemp()
        ftc(temp)
    elif opcja == '3':
        ftemp()
        ktf(temp)
    elif opcja == '4':
        ftemp()
        ftk(temp)
    elif opcja == '5':
        ftemp()
        ktc(temp)
    elif opcja == '6':
        ftemp()
        ctk(temp)
else:
    print("Wybrałeś złą opcje")