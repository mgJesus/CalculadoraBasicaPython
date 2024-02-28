print("Calculadora")

rodar = 'S' or 's'

while rodar:
    
        operação = input('(1)Soma, (2)Subtração, (3)Divisão, (4)Multiplicação \nOperação:')


        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))

     

        if(operação == '1'):
                print(f'{num1} + {num2} = {num1+num2}') 
                        
        elif(operação == '2'):  
                print(f'{num1} - {num2} = {num1-num2}')

        elif(operação == '3'):
                print(f'{num1} / {num2} = {num1/num2}')

        elif(operação == '4'):
                print(f'{num1} X {num2} = {num1*num2}')

        rodar = input('Deseja continuar?\n')
        
        if rodar.upper() == 'n':
                break

else:   
        print('Obrigado')


