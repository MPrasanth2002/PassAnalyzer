import re

def analyze_password(password):
    if len(password) < 8:
        return "Weak password: Length is less than 8 characters."

    Upper = re.search(r'[A-Z]', password) is not None
    Lower = re.search(r'[a-z]', password) is not None
    Symbol = re.search(r'[\W_]', password) is not None  # checks any non-word character

    if Upper and Lower and Symbol:
        return "Excellent, Your password is Strong"
    elif (Upper + Lower + Symbol) >= 2:
        return "Good, Your password is Moderate"
    else:
        return "OH!! My Bad, Your password is too Weak"

password = input("Enter a password to analyze: ")
result = analyze_password(password)
print(result)
