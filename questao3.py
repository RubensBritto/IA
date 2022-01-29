import os
#os.system('clear') 

variaves = []
valores = []
se=[]
entao=[]
regras=[]


def buscarVariavel(a):
  if a in variaves:
    return variaves.index(a)
  else:
    return -1

def criarVariveis():
  while True:
    a = input("Entre com o nome da variavel OU DIGITE not PARA FINALIZAR: ").lower()
    if a == "not":
      break
    else:
      variaves.append(a)

def addValoresVariveis():
  for i in range(len(variaves)):
    a = input(f'Entre com o valor da variavel: {variaves[i]} ').lower()
    if a == "not":
      break
    else:
      valores.append(a)

def selecionarOperadores():
  a = input(f' Selecione o operador desejado\n 1 - or\n 2 - and\n 3 - entao\n')
  if a == '1':
    return 'or'
  elif a == '2':
    return 'and'
  elif a == '3':
    return 'entao'
  else:
    print(f'Operador Invalido, tente novamente')
    selecionarOperadores()
      
def criarRegras():
  regra = ''
  i = 1
  while True:
    regraEntao = True if regra[-5:] != 'entao' else False

    a = input(f"Digite o nome da {i}ª variável: ").lower()
    indice = buscarVariavel(a)
    if indice != -1:
      regra+=f'{variaves[indice]}={valores[indice]}'
    else:
      print(f'Variavel não existe')
    
    if regraEntao:
      operador = selecionarOperadores()
      se.append(regra)
      regra+=f'{operador}'
      i+=1
    else:
      e = f'{variaves[indice]}={valores[indice]}'
      regras.append(regra)
      entao.append(e)
      i+=1
      os.system('cls') 
      print(f'Regra Criada com sucesso: {regra}')
      return menu()

def menu():
  print(f'Escolha a Opção desejada\n'
          '1 - Criar Variaves\n' 
          '2 - Add Valores Variaves\n'
          '3 - Criar Regras')
  a = input("Entre com a opção desejada: ").lower()
  if a == '1':
    criarVariveis()
  elif a == '2':
    addValoresVariveis()
  elif a == '3':
    criarRegras()

def main():
  menu()

if __name__ == '__main__':
    main()