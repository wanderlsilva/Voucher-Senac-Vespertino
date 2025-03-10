def palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s [::-1]

print(palindromo("A base do teto desaba"))