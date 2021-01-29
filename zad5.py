def fkwota():
    global kwota
    try:
        kwota = float(input("Podaj kwotę do przeliczenia: "))
    except ValueError:
        print("Nie podałeś kwoty lub błędny zapis!")
        exit()

def przelicz(a, b, y, z):
    print("\nWybierz sposób przeliczania: ")
    print("1)", a,"na", b)
    print("2)", b,"na", a)
    sp = input("\nWybierz sposób: ")
    if sp in ('1', '2'):
        if sp == '1':
            print("\nPrzeliczamy", a, "na", b)
            fkwota()
            y(kwota)
        elif sp == '2':
            print("\nPrzeliczamy", b, "na", a)
            fkwota()
            z(kwota)
    else:
        print("Wybrałeś niepoprawną opcję")

#kurs walut na dzień 26.01.2021 (20:00-21:00)
def THB(x):
    y = round(x * 0.033, 2)
    return print(x, "THB to", y, "USD")

def UTHB(x):
    y = round(x * 29.94, 2)
    return print(x, "USD to", y, "THB")

def BTC(x):
    y = round(x * 32237.9, 2)
    return print(x, "BTC to", y, "USD")

def UBTC(x):
    y = round(x * 0.000031, 7)
    return print(x, "USD to", y, "BTC")

def BTN(x):
    y = round(x * 0.014, 2)
    return print(x, "BTN to", y, "USD")

def UBTN(x):
    y = round(x * 72.87, 2)
    return print(x, "USD to", y, "BTN")

def MRO(x):
    y = round(x * 0.028, 2)
    return print(x, "MRO to", y, "USD")

def UMRO(x):
    y = round(x * 36.02, 2)
    return print(x, "USD to", y, "MRO")

def ETH(x):
    y = round(x * 1339.62, 2)
    return print(x, "ETH to", y, "USD")

def UETH(x):
    y = round(x * 0.00075, 7)
    return print(x, "USD to", y, "ETH")

print("Przelicznik walut")
print("Wybierz walutę z pośród dostępnych: ")
print("1) Baht Tajski (THB) - Dolary amerykańskie (USD)")
print("2) Bitcoin (BTC) - Dolary amerykańskie (USD)")
print("3) Ngultrum bhutański (BTN) - Dolary amerykańskie(USD)")
print("4) Ugija mauretańska (MRO) - Dolary amerykańskie (USD)")
print("5) Ethereum (ETH) – Dolary amerykańskie (USD)")

waluta = input("Wybierz walutę: ")
if waluta in ('1', '2', '3', '4', '5'):
    kwota = 0
    if waluta == '1':
        przelicz("THB", "USD", THB, UTHB)
    elif waluta == '2':
        przelicz("BTC", "USD", BTC, UBTC)
    elif waluta == '3':
        przelicz("BTN", "USD", BTN, UBTN)
    elif waluta == '4':
        przelicz("MRO", "USD", MRO, UMRO)
    elif waluta == '5':
        przelicz("ETH", "USD", ETH, UETH)
else:
    print("Wybrałeś niepoprawną opcję")