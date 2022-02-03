from types import prepare_class
import os

#variaves=[]
#valores=[]
"""
Os Arrays variaves e valores estão preenchidos para ficar melhor de testar a base de inferencia dada

Mas, caso queiram testar outra base, basta comentar eles dois e descomentar as duas variaveis acima desse comentário
"""
variaves = ['rendimento_alto','rendimento_medio','rendimento_baixo',
            'conceda_emprestimo_sim', 'conceda_emprestimo_nao',
            'e_bacharel_ou_superior_sim', 'e_bacharel_ou_superior_nao',
            'tem_emprego_sim', 'tem_emprego_nao',
            'continua_a_investigar_sim',
            'referencias_sim', 'referencias_nao']
valores = ['alto','medio','baixo','sim','nao','sim','nao','sim','nao','sim','sim','nao']
se=[]
entao=[]
regras=[]
baseFatos = ['referencias_sim=sim','e_bacharel_ou_superior_nao=nao']
objetivo = ['rendimento_alto=alto']

def buscarObjetivo(lista):
  for i in lista:
    if objetivo[0] == i:
      print(f'Objetivo Localizado')
      print(f'base de fatos -- {baseFatos}')
      #POSSO LIMPAR TUDO??

def remove_repetidos(lista):
    l = []    
    for i in lista:
      if i not in l:
        i = i.replace(" ", "")
        l.append(i)
    return l

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
  while True:
    a = input(f' Selecione o operador desejado\n 1 - and\n 2 - entao\n')
    if a == '1':
      return 'and'
    if a == '2':
      return 'entao'
    else:
      print(f'Operador Invalido, tente novamente')
      
def criarRegras():
  regra = ''
  i = 1
  while True:
    regraEntao = True if regra[-6:-1].replace(" ", "") != 'entao' else False
    print(f'regraaa - {regra.replace(" ", "")}')
    print(f'regraaa 5 ultimo - {regra[-6:-1].replace(" ", "")}')

    a = input(f"Digite o nome da {i}ª variável: ").lower()
    indice = buscarVariavel(a)
    if indice != -1:
      regra+=f' {variaves[indice]} = {valores[indice]} '
    else:
      print(f'Variavel não existe')
      criarRegras()    
    if regraEntao:
      operador = selecionarOperadores()
      se.append(regra)
      regra+=f'/{operador}/'
      i+=1
    else:
      e = f' {variaves[indice]} = {valores[indice]} '
      regras.append(regra)
      entao.append(e)
      i+=1
      os.system('cls') 
      print(f'Regra Criada com sucesso: {regra}')
      return menu()

def encadeamentoProgressivo():
  for r in regras:
    tempListSe=[]
    tempListEntao=[]
    temp = r.split("/entao/")
    tempListSe.append(temp[0].split("/and/"))
    tempListSe = remove_repetidos(tempListSe[0])
    tempListEntao.append(temp[1].split("/and/")[-1])
    tempListEntao = remove_repetidos(tempListEntao)
    
    if set(baseFatos).intersection(tempListSe) and len(set(baseFatos).intersection(tempListSe)) == len(tempListSe):
      baseFatos.append(tempListEntao[0])
      buscarObjetivo(baseFatos)

    
def encadeamentoRegressivo():
   for i in objetivo:
     for j in entao:
       if i == j:
         baseFatos.append(i)
         a = entao.index(i)
         if len(objetivo) == 0:
           print(f'Encadeamento Regressivo Feito com sucesso, nova base de fatos {baseFatos}')
         else:
          objetivo.remove(a)
          b = se[i].split("/and/")
          for i in b:
            i.replace(" ", "")
            objetivo.append(i)
   
   if(len(objetivo)!=0):
     print(f'Encadeamento Regressivo feito, entranto não encontramos correspodencia para o/os objetivo(s): {objetivo}')      

def menu():
  while True:
    print(f'Escolha a Opção desejada\n'
            '1 - Criar Variaves\n' 
            '2 - Add Valores Variaves\n'
            '3 - Criar Regras\n'
            '4 - Encadeamento Para frente\n'
            '5 - Encadeamento para trás\n'
            '6 - Encademanento misto\n')
    a = input("Entre com a opção desejada: ").lower()
    if a == '1':
      criarVariveis()
    elif a == '2':
      addValoresVariveis()
    elif a == '3':
      criarRegras()
    elif a == '4':
      encadeamentoProgressivo()
    elif a == '5':
      encadeamentoRegressivo()
    elif a == '6':
      encadeamentoProgressivo()
      encadeamentoRegressivo()

def main():
  menu()

if __name__ == '__main__':
    main()