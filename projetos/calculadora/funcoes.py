def soma (a,b):
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    else:
        soma= a+b
        return soma

def subtracao (a,b):
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    else:
        subtracao= a-b
        return subtracao

def divisao(a,b):
    try:
        a=float(a)
        b=float(b)
    except ValueError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    else:
        try:
            divisao= a/b
            return divisao
        except ZeroDivisionError:
            print(f"O input 'b' não pode ser 0, recebido {b} tipo (b)")

def multiplicacao(a,b):
    try:
        a=float(a)
        b=float(b)
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    else:
        multiplicacao= a*b
        return multiplicacao