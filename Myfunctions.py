import statistics as st

lista = [2,4,3,1,7,5,6]

def Amplitude(lista):
    amplitude = max(lista) - min(lista)
    return amplitude

def Variancia(lista):
    variancia = st.variance(lista)
    return variancia

def Desvio_padrao(lista):
    desviototal = st.stdev(lista)
    return desviototal

def Media(lista):
    media = sum(lista) / len(lista)
    return media

def Mediana(lista):
    mediana = st.median(lista)
    return mediana

def Moda(lista):
    moda = st.mode(lista)
    return moda

def Menor(lista):
    menor = min(lista)
    return menor 

def Maior(lista):
    maior = max(lista)
    return maior
