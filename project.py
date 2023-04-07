print('╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮')
print('             CONVERSOR BINÁRIO/DECIMAL                                ')
print('╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯')
print(' --------------------------------------------------\n')
print('        OPÇÃO 1               BINARIO P/ DECIMAL \n')
print('        OPÇÃO 2               DECIMAL P/ BINARIO \n')
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+++++++++=+=+=+=+=+=')
print('----------------------------------------------------')

opt = int(input('> '))

if(opt == 1):
  vec = str(input('Insira o número binário: '))
  
  num = [] # Guarda o input da string separada
  n = [] # int de num
  num2 = [] # Guarda as potências
  resp = [] # Guarda valores do 1
  
  for c in range(len(vec)):
    num.append(int(vec[c]))

    if(1 not in num and 0 not in num):
      print('Erro ao validar número')
      break
    else: 
      continue
      
  i=len(num)-1
  
  while(i>=0):
    num2.append(pow(2, i))
    i-=1

  result = 0
  for c in range(len(num)):
    if(num[c] == 1):
      result += num2[c]
    else:
      c+=1
  print('\nRESPOSTA:\n    > {}'.format(result))
  
elif(opt == 2):
  dec = int(input('Insira o número decimal: '))
  resto = 0
  restos = []
  r = []
  
  quociente = 0

  while(1):
    quociente = dec // 2
    resto = dec % 2
    restos.append(resto)
    dec = quociente
    if(quociente == 0):
      break
      
  i = len(restos) - 1
  
  while(i>=0):
    r.append(str(restos[i]))
    i-=1

  s = ''.join(r)
  print('\nRESPOSTA:\n    > {}'.format(s))  # imprime "Python 3.7"
else:
  print('ERRO')
  
  



