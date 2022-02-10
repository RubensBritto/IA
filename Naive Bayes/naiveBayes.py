import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

#Carregando DataSet
base_credito = pd.read_csv('https://raw.githubusercontent.com/RubensBritto/IA/main/Naive%20Bayes/Risco_Credito.csv')  

# Armezenando os Atributos previsores
X_risco_credito = base_credito.iloc[:,0:4].values
#X_risco_credito

#Armazenando as classes
Y_risco_credito = base_credito.iloc[:,4].values
#print(Y_risco_credito)

#Criação das variavés Label Encoder
label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantia = LabelEncoder()
label_encoder_renda = LabelEncoder()

#Convertendo de categoricos para númericos
X_risco_credito[:,0] = label_encoder_historia.fit_transform(X_risco_credito[:,0])
X_risco_credito[:,1] = label_encoder_divida.fit_transform(X_risco_credito[:,1])
X_risco_credito[:,2] = label_encoder_garantia.fit_transform(X_risco_credito[:,2])
X_risco_credito[:,3] = label_encoder_renda.fit_transform(X_risco_credito[:,3])
#print(X_risco_credito)

#Implemenando o Algoritmo Naive Bayes

#Instanciando o modelo Gaussiano Naive Bayes
naive_risco_credito = GaussianNB()

#Realizando o treinamnento do algoritmo - Gerando uma tabela de probabilidade
naive_risco_credito.fit(X_risco_credito, Y_risco_credito)

#Realizando a previsão de um novo cliente do banco
# Cliente 1: historia boa  (0), divida alta (0), garantias nenhuma  (1), renda acima_35 (2)
# Cliente 2: historia ruim (2), divida alta (0), garantias adequada (0), renda 0_15     (0)

previsao = naive_risco_credito.predict([[0,0,1,2],[2,0,0,0]])

print(f'Cliente 1 deve ser classificado como: {previsao[0]}')
print(f'Cliente 2 deve ser classificado como: {previsao[1]}')