def MB(x):
    mb = x * 1000000 / 1024 / 1024
    return print("Rzeczywista pojemność dysku wynosi:", round(mb, 2), "MB")

def GB(x):
    gb = x * 1000000000 / 1024 / 1024 / 1024
    return print("Rzeczywista pojemność dysku wynosi:", round(gb, 2), "GB")

def TB(x):
    tb = x * 1000000000000 / 1024 / 1024 / 1024 / 1024
    return print("Rzeczywista pojemność dysku wynosi:", round(tb, 2), "TB")

print("Kalkulator pojemności rzeczywistej dysku")
print("Wybierz jakiego rzędu pojemności jest twój dysk")
print("1) MB - megabajty")
print("2) GB - gigabajty")
print("3) TB - terabajty")
rodzaj = input("Wybierz opcje: ")
try:
    wielkosc = float(input("Podaj wielkość dysku podaną przez producenta: "))
except ValueError:
    print("Nie podałeś wielkości dysku!")
    exit()
if rodzaj in ('1', '2', '3'):
    if rodzaj == '1':
        MB(wielkosc)
    elif rodzaj == '2':
        GB(wielkosc)
    elif rodzaj == '3':
        TB(wielkosc)
else:
    print("Wybrałeś niepoprawną opcję")