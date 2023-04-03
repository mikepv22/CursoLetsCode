from funcoes import soma
from funcoes import subtracao
from funcoes import divisao
from funcoes import multiplicacao

def calcule():
    a=float(input("Digite um número: "))
    b=float(input("Digite um número: "))
    op=input('Digite a operação que deseja realizar: ')

    if op=='soma' or op=='+':
        print(soma(a,b))
    elif op=='subtracao' or op=='-':
        print(subtracao(a,b))
    elif op=='divisao' or op=='/':
        print(divisao(a,b))
    elif op=='multiplicacao' or op=='*':
       print( multiplicacao(a,b))
    else:
        print('Operação não encontrada')