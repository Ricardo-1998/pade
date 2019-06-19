from sympy import *
import matplotlib.pyplot as plt
import numpy as np

from sympy.interactive import printing;
printing.init_printing(use_latex=True);
from IPython.display import display, Latex

x = Symbol('x')
flag = True




def factorial(num):
    fact = 1
    if(num!=0):
        for i in range(1,num+1): 
            fact = fact * i
    return fact

def derivada(funcion,x,orden):
    valor = {x:0}
    param = diff(funcion,x,orden)
    return param.evalf(subs=valor)

def Maclaurin(funcion,x,N):
    arreglo = []
    orden = N
    for i in range(0,N):
        variable = derivada(funcion,x,orden)
        varible =  variable/factorial(i)
        arreglo.append(variable)
    return arreglo

def verificarNum(num):
    if(num < 0 and num%2!=0):
        return True
    else:
        return False
def creandoMatriz(num):
    arreglo = []
    matriz = []
    aux = 0
    while(aux<=num):
        for i in range(0,num+1):
            arreglo.append('h')
        matriz.append(arreglo)
        arreglo=[]
        aux=aux+1
    return matriz
        
def main():
    ayuda = []
    flag= True
    m=0
    n=0
    while(flag):
        m = int(input('Ingrese m: '))
        if(m < 0 and m%2!=0):
            m = int(input('Ingrese m(debe ser positivo y entero): '))
        else:
            flag = False
    
    flag = True
    while(flag):
        n = int(input('Ingrese n: '))
        if(n < 0 and n%2!=0):
            n = int(input('Ingrese n(debe ser positivo y entero): '))
        else:
            flag = False

    N = m+n
    funcion = input('Ingrese funcion: ')
    ayuda = Maclaurin(funcion,x,N)

    q=1
    p=ayuda[0]
    
    b =creandoMatriz(N+1)
    
    for i in range(1,N):
        for j in range(1,i-1):
            if(j<=n):
                b[i][j]=0
        if(i<=n):
            b[i][i]=1
        num = 1
        for j in range(i+num,N):
            b[i][j]=0
            num=num+1
        for j in range(1,i):
            if(j<=m):
                b[i][n+j]= -ayuda[i-j]
        num2=1
        for j in range(n+i+num2,N):
            b[i][j]=0
    
              
        b[i][N+1]=ayuda[i]
    

main()
    
    
    

