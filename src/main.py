def calculate(entrada) -> float:
    copia = ""
    for letra in entrada:
        if letra != " ":
            copia += letra

    parte1 = ""
    parte2 = ""
    i = 0
    operador = None
    while i < len(copia):
        if (copia[i] in ["+", "-", "*", "/"]):
            operador = copia[i]
            i += 1
            break
        else:
            parte1 += copia[i]
            i += 1

    while i < len(copia):
        parte2 += copia[i]

    term1 = int(parte1)
    term2 = int(parte2)
    if operador == "+":
        return term1+term2
    elif operador == "-":
        return term1-term2
    elif operador == "*":
        return term1*term2

    elif operador == "/":
        if term2 == 0:
            return "Error"
        else:
            return term1 / term2

    pass