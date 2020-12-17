def XO(txt):
    aux = txt.lower()
    xs = aux.count('x')
    os = aux.count('o')
    if os == xs:
        return True
    return False
