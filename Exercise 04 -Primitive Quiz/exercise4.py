print("Welcome lets test ur knowledge of Capitals!")
#contains dictionary of countries and their capitals
caps = {'France':'paris','Germany':'berlin','Italy':'rome','Spain':'madrid','Portugal':'lisbon',
        'Austria':'vienna','Albania':'tirana','Greece':'athens','Netherlands':'amsterdam','Belgium':'brussels'}

for c in caps:
    a = input(f"\nWhat is the capital of {c}? ").lower()
    print("Correct!" if a == caps[c] else "Incorrect. It is:", caps[c].capitalize())
