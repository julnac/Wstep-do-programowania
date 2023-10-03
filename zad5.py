user_input = input("Podaj dowolne dane: ")
try:
    user_input = int(user_input)
except ValueError:
    try:
        user_input = float(user_input)
    except ValueError:
        pass
print("Typ wprowadzonych danych to:", type(user_input))
