# crie um arquivo separado com as funções para resolver para uma das solicitações:
# 1. Calcule a média.
# 2. Calcule a mediana.
# 3. Calcule a moda.
# 4. Calcule a variância.
# 5. Calcule o desvio padrão.
# 6. Calcule a amplitude.


import Myfunctions as mf

produtos = {'Arroz' : 19.90,
            

'Feijão' : 8.90,

'Açúcar' : 4.50,

'Café' : 10.90,

'Óleo de Soja' : 5.50,

'Macarrão' : 3.49,

'Molho de Tomate' : 2.99,

'Sal Refinado' : 2.80,

'Leite' : 4.30,

'Queijo Mussarela' : 14.90,

'Presunto' : 13.00,

'Salsicha' : 7.90,

'Papel' : 4.70,

'Sabão em Pó' : 11.90,

'Detergente' : 2.00,

'Amaciante' : 6.90,

'Sabonete' : 1.90,

'Shampoo' : 7.90,

'Condicionador' : 9.50,

'Papel Higiênico' : 19.90,

'Frango' : 13.90,

'Carne' : 29.90,

'Batata Doce' : 6.00,

'Cebola' : 4.50,

'Tomate' : 7.00,

'Alface' : 5.50,

'Laranja' : 3.90,

'Maçã' : 7.90,

'Pão de Forma' : 6.50,

'Manteiga': 8.50}

valores = []

for values in produtos.values():
    valores.append(values)

media_val = mf.Media(valores)
mediana_val = mf.Mediana(valores)
moda_val = mf.Moda(valores)
variancia_val = mf.Variancia(valores)
desvio_padrao_val = mf.Desvio_padrao(valores)
amplitude_val = mf.Amplitude(valores)

print(f'''Dados sobre o valor dos produtos listados
Média dos valores:{media_val:0.2f}
Mediana dos valores:{mediana_val}
O valor que mais se repete:{moda_val}
Variância dos valores:{variancia_val:0.3f}
Desvio padrão dos valores:{desvio_padrao_val:0.3f}
Diferença do menor valor ao maior(Amplitude):{amplitude_val}''')
