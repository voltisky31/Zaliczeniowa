from datetime import date, datetime

def noc_wielka(ruk):
    a = ruk % 19
    b = ruk // 100
    c = ruk % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    ksinzyc = f // 31
    slonecznik = f % 31 + 1
    return date(ruk, ksinzyc, slonecznik)

def tera_rok():
    return (datetime.now().year)

def tera_data():
    return (datetime.now().strftime("%Y-%m-%d "))

def uro():
    data_in = input("Podaj datę urodzenia w formacie rrrr-mm-dd: ")
    date = datetime.strptime(data_in, '%Y-%m-%d')
    tygodzien=["Poniedziałek" ,"Wtorek" ,"Środa" ,"Czwartek" ,"Piątek" ,"Sobota" ,"Niedziela"]
    dzien_numer=date.weekday()
    return tygodzien[dzien_numer]

print("Dziś jest: " ,tera_data() )
x = int(input("Podaj rok do określenia daty wielkanocy: "))
print("Wielkanoc w roku" ,x ,"wypada" ,noc_wielka(x))
print("Urodziłeś/aś się w:", uro())