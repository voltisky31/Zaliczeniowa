def inp(x):
    if len(x) == 0:
        return True
    else:
        return False

def pytanie(x, y):
    global pkt
    if inp(x) is True:
        pkt += 0
    elif (x).lower() in (y):
        pkt += 1
    return 0

wybor = input("Dzień dobry uczniu! Czy chcesz rozpocząć test z wiedzy informatycznej?(Tak): ")
if inp(wybor) is True:
    print("Przerwałeś test")
else:
    if wybor.lower() in ('tak'):
        pkt = 0

        print("Czy lubisz koty?")
        print("A) Uwielbiam!")
        print("B) Tak")
        print("C) Nie")
        print("D) Psy lepsze")
        pyt1 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt1, "b")
        print()

        print("Czy lubisz koty?")
        print("A) Uwielbiam!")
        print("B) Tak")
        print("C) Nie")
        print("D) Psy lepsze")
        pyt2 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt2, "a")
        print()

        pyt3 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt3, "c")
        print()

        pyt4 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt4, "b")
        print()

        pyt5 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt5, "b")
        print()

        pyt6 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt6, "b")
        print()

        pyt7 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt7, "b")
        print()

        pyt8 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt8, "b")
        print()

        pyt9 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt9, "b")
        print()

        pyt10 = input("Wybierz A, B, C lub D: ")
        pytanie(pyt10, "b")
        print()

        if pkt > 4 or pkt == 0:
            print("Otrzymałes: ", pkt, "punktów")
        elif pkt >= 2:
            print("Otrzymałes: ", pkt, "punkty")
        elif pkt >= 1:
            print("Otrzymałes: ", pkt, "punkt")

        if pkt == 10:
            print("Jesteś najlepszy! Ocena celująca (100%)")
        elif pkt >=9:
            print("Gratulacje! Ocena bardzo dobra (90% - 99%)")
        elif pkt >=7:
            print("Nieźle Ci poszło! Ocena dobra (70% - 89%)")
        elif pkt >=5:
            print("Stać Cię na więcej! Ocena dostateczna (50% - 69%)")
        elif pkt >=3:
            print("Strzelałeś? Ocena dopuszczająca (30% - 49%)")
        else:
            print("Nie udało się! Ocena niedostateczna (<30%)")
    else:
        print("Przerwałeś test")