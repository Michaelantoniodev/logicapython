#calculos de horas extras a receber de acordo com horas a mais trabalhadas

'''As horas extras são calculadas a 60% do valor da hora do trabalhador

'''

nomeFuncionario = str (input('Digite seu nome: ', ))
valorHoraTrabalhada = float (input('Digite o valor de sua hora: ', ))
numHoraExtra = float (input ('Digite quantas horas foram trabalhadas a mais: ',))
horasDoMes = float (input('Quantas horas foram tralhadas no mês sem HE: ', ))
resultado = valorHoraTrabalhada * horasDoMes
extraAReceber = ((valorHoraTrabalhada * 1.60) * numHoraExtra )
total = resultado + round (extraAReceber,2)
#valores a recber

print ('O valor a receber foi baseado num calculo de que a hora é acrescida de 60% a mais do seu salário')
print ('Seu salário total sem as horas extras ficou em: ', resultado)
print ('O valor das horas extras acumuladas foi de: ', round (extraAReceber,2))
print (' A soma do salário mais horas extras ficou em: ', total )