def soma (a,b):
    try:
        soma= a+b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    return soma

def subtracao (a,b):
    try:
        subtracao= a-b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    return subtracao

def divisao(a,b):
    try:
        divisao= a-b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    except ZeroDivisionError:
        print(f"O input 'b' não pode ser 0, recebido {b} tipo (b)")
    return divisao

def multiplicacao(a,b):
    try:
        multiplicacao= a-b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser um float ou int, recebido {a}, tipo(a), {b} tipo (b)")
    return multiplicacao