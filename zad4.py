# Pobranie danych od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

# Obliczenia
suma = liczba1 + liczba2
roznica = liczba1 - liczba2
iloczyn = liczba1 * liczba2
iloraz = liczba1 / liczba2

# Zaokrąglenie w dół
suma = int(suma)
roznica = int(roznica)
iloczyn = int(iloczyn)
iloraz = int(iloraz)

# Wyświetlenie wyników
print(f"Suma: {suma}, Różnica: {roznica}, Iloczyn: {iloczyn}, Iloraz: {iloraz}")
