#soma simples
try:
        v1 = float (input('Informe o valor a ser calculado: ',))
        v2 = float (input ('Informe o valor a ser calculado: ',))
except:
        print ('****************')
        print ('Não deve ser inseridos numeros diferentes de inteiros')
        print ('****************')
        exit()
soma = v1 + v2 
resultado = soma
print ('O resultado soma é: ', resultado)        
