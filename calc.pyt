numero1= float(input('digite o primeiro numero: '))
numero2= float(input('digite seu segundo numero: '))

calculo=int(input('qual e a sua opcão\n [1]-adicao\n [2]-multiplicacão\n [3]-divisao\n [4]-subtracao\n escolha qual operacão ira fazer de 1 a 4:  '))

if calculo==1:
    resultado=numero1+numero2
    print(f'seu resultado é {resultado}')

elif calculo==2:
    resultado2=numero1*numero2
    print(f'seu resultado é {resultado2}') 

elif calculo==3:
    resultado3=numero1/numero2
    print(f'seu resultado é {resultado3}')

elif calculo==4:
    resultado4=numero1-numero2
    print(f'seu resultado é {resultado4}')        