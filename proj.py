#inicio da atividade 3                                  #Programa para empresa de limpeza!
#função metragem_limpeza()                              
def metragem_limpeza(): # nome da funçao
  while True:       #inicio do laço da função
    print(40*'-'+'   '+'Menu 1 - 3 Metragem M²'+'   '+40*'-') # print do menu de escolhas
    try:
      metragem = int(input('** Digite a Metragem do local (M²) **: ')) # usuario entra com a metragem
      if (metragem >= 30) and (metragem <= 299):     # calculo entre 30 e 299
        print('É necessário contratar 1 pessoa para a limpeza') #print quantidade de pessoas necessarias
        return 60 + 0.3 * metragem    # valor retornado com a escolha da metragem
      elif (metragem >= 300) and (metragem <= 699): # calculo entre 300 e 699
        print('É necessário contratar 2 pessoa para a limpeza')
        return 120 + 0.5 * metragem  # valor retornado com a escolha da metragem
      elif (metragem <30) or (metragem > 699):#caso o usuario digite um valor menor que 30 ou maior que 700 aparece a mensagem a seguir:
        print('NÃO ACEITAMOS CASAS COM METRAGEM MENOR QUE 30M² OU MAIOR QUE 700M²')
        continue # volta para o inicio
    except ValueError: #caso o usuarioo digite uma letra ou um numero com casas decimais aparece a mensagem a seguir :
        print('FAVOR INFORMAR A METRAGEM M² CORRETA')

#fim da função

#função tipo_limpeza()
def tipo_limpeza(): # nome da funçao
  while True:       #inicio do laço da função
    print(40*'-'+'   '+'Menu 2 - 3 Tipo'+'          '+40*'-')   # print do menu de escolhas
    tipo = input('** Digite o Tipo de Limpeza ** \n'+
                 50*'- '+'\n'+
                 'B– Básica - Indicada para sujeiras semanais ou quinzenais \n'+ #print opção limpeza basica
                 50*'- '+'\n'+
                 'C–Completa- Indicada para sujeiras antigas e/ou não rotineiras \n'+#print opção limpeza completa
                 50*'- '+'\n'+
                 '>>> ')    #usuario informa o tipo da limpeza
    tipo = tipo.upper() #transforma letras minusculas em maiusculas
    tipo = tipo.strip() #elimina espaçamentos
    if tipo == 'B':
      print('Você escolheu o tipo de limpeza B - Básica') # print da escolha B
      return 1.00     # valor retornado com a escolha do tipo
    elif tipo =='C':
      print('Você escolheu o tipo de limpeza C - Completa')  # print da escolha C
      return 1.30     # valor retornado de acordo com a escolha do tipo
    else:
      tipo !='B' and tipo !='C' # caso o usuario digite algo diferente de B ou C
      print('OPÇÃO INVALIDA !')
      continue #em caso de opção invalida volta para o inicio


#Fim da função

#função adicional_limpeza()
def adicional_limpeza(): # nome da funçao
  acumulador = 0
  while True: # começo do laço
    try:
      print(40*'-'+'   '+ 'Menu 3 - 3 Adicional'+'     ' +40*'-') ## print do menu de escolhas
      adicional = int(input('** Dígite o adicional da limpeza: ** \n'+
                             50*'- '+'\n'+
                            '0- Não quero adicionais (encerrar)\n'+ # 0 = sem adicional encerrar o programa
                             50*'- '+'\n'+
                            '1- Passar 10 peças de roupas  R$ : 10.00 \n'+ # 1 = adicionar 10 peças de roupas para passar
                             50*'- '+'\n'+
                            '2- Limpeza de 1 forno micro-ondas R$ : 12.00 \n'+ # 2 = adicionar 1 forno micro-ondas para limpeza
                             50*'- '+'\n'+
                            '3- Limpeza de 1 geladeira R$ : 20.00\n'+ # 3 = adiciona 1 geladeira na limpeza
                             50*'- '+'\n'+
                            '>>> '))
      if adicional == 0:  # 0 = sem adicional encerrar o programa e retorna o acumulador
        return acumulador
      elif adicional == 1:  # 1 = adiciona 10 peças de roupas para passar e retorna acumulador + 10.00
        acumulador = acumulador + 10 #pega o valor acumulado e adiciona + 10
        continue # volta para o menu adicionais
      elif adicional == 2:
        acumulador = acumulador + 12 #pega o valor acumulado e adiciona + 12
        continue# volta para o menu adicionais
      elif adicional == 3:
        acumulador = acumulador + 20 #pega o valor acumulado e adiciona + 20
        continue # volta para o menu adicionais
      else:
        adicional > 0 and adicional < 3 # se numeros menor q 0 e maior que 3 print opção invalida !
        print('OPÇÃO INVALIDA !')
        continue # volta para o menu adicionais
    except ValueError :
      print('OPÇÃO INVALIDA !')
      continue # volta para o menu adicionais

#fim da função

#inicio do programa:

print(28*'-'+'Bem vindo a loja de limpeza do Cristian De Oliveira'+ 29*'-') # print inicial do programa
metragem = metragem_limpeza() # variavel 1 metragem
print(metragem)
tipo = tipo_limpeza() # variavel 2 tipo
print(tipo)
adicional = adicional_limpeza() # variavel 3 adicional
print(adicional)
total = ( metragem * tipo ) + adicional  # variavel da soma do total
print(100*'*')
print(' (Total R$ : {:.2f} )         ( Metragem R$ : {:.2f} * Tipo R$ : {:.2f} + Adicional R$ : {:.2f} )'.format(total,metragem,tipo,adicional)) # print total detalhado
print(100*'*')
