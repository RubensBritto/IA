"""
BASE DE INFERENCIA 
R1: SE Dor de cabeça = Sim ENTÃO Receitar analgésico

R2: SE Dor de cabeça = Sim E Garganta inflamada = Sim E Tosse = Sim
ENTÃO Diagnostico = Gripe

R3: SE Cansaço = Sim E Dor de cabeça = Sim
ENTÃO Diagnóstico = Mononucleose infecciosa

R4: SE Cansaço = Sim E Garganta inflamada = Sim
ENTÃO Diagnóstico = Amigdalite

R5: SE Cansaço = Sim ENTÃO Diagnóstico = Estresse
------------------------------------------------------
R6: SE Falta de Ar = Sim E Tosse = Sim E Febre = Sim ENTÃO Diagnostico = Covid

R7: SE Febre = Sim E Dores Musculares = Sim E Manchas Vermelhas = Sim 
ENTÃO Diagnostico = Dengue

R8: SE Febre = Sim E Dores Musculares = Sim ENTÃO Diagnostico = Virose

R9: SE Febre = Sim E Dores Musculares = Sim E Dor de Cabeça Diagnostico = Chikungunya

R10:Se Febre = Sim e Dores Musculares = Sim E Nauseas = Sim ENTAO Diagnostico = Febre Amarela 
"""

dorHead = False
receitarAnal = False
gargantaInf = False
tosse = False
gripe = False
cansaco = False
mononucleose = False
amigdalite = False
estresse = False
faltaAr = False
febre = False
dorMuscular = False
manchaCorpo = False
covid = False
virose = False
dengue = False
chink = False
nausea = False
feb_ye = False

def baseInf():
  global dorHead
  dorHead = True 

if __name__ == '__main__':
  baseInf()

  for i in range(0,10):

    if receitarAnal:
      print(f'Receitar analgésico - Sim')
      break
    if dorHead:
      receitarAnal = True
    
    if dorHead and gargantaInf and tosse:
      gripe = True
      print(f'Diagnostico - Gripe')
    
    if cansaco and dorHead:
      mononucleose = True
      print(f'Diagnostico - Mononucleose Infecciosa')
    
    if cansaco and gargantaInf:
      amigdalite = True
      print(f'Diagnostico - Amigdalite')
    
    if cansaco:
      estresse = True
      print(f'Diagnostico - Estresse')

    if faltaAr and tosse and febre:
      covid = True
      print(f'Diagnostico - Covid')

    if febre and dorMuscular and manchaCorpo:
      dengue = True
      print(f'Diagnostico - Dengue')

    if febre and dorMuscular:
      virose = True
      print(f'Diagnostico - Virose')

    if febre and dorHead and dorMuscular:
      chink = True
      print(f'Diagnostico - Chinkunguya')
    if febre and nausea and dorMuscular:
      feb_ye = True
      print(f'Diagnostico - Febre Amarela!')
  else:
    print(f'Diagnostico indefinido!')
