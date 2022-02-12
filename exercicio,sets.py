presentes = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira',
    'espanador', 'espátula', 'estante', 'faqueiro',
    'frigideira', 'funil', 'halter', 'liquidificador',
    'notebook', 'panela', 'peneira', 'playstation',
    'rádio', 'smartphone', 'sofá', 'tablet', 'teclado',
    'televisão', 'vassoura', 'webcam', 'xbox',
}

loja1 = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira', 'estante',
    'frigideira', 'funil', 'liquidificador', 'notebook', 'panela',
    'playstation', 'smartphone', 'teclado', 'televisão'}
loja2 = {
    'cafeteira', 'escumadeira', 'espanador', 'frigideira', 'funil',
    'halter', 'peneira', 'playstation', 'sofá', 'tablet', 'televisão',
    'vassoura', 'webcam', 'xbox'}
loja3 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}
loja4 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}

# Relação de presentes encontrados em cada loja

presentes_na_loja1 = []
presentes_na_loja2 = []
presentes_na_loja3 = []
presentes_na_loja4 = []

#produtos exclusivos de cada loja

exclusivos1 = []
exclusivos2 = []
exclusivos3 = []
exclusivos4 = []


# 1.Quais produtos são oferecidos em ao menos uma loja?
print("_____________________________") 
print("Produtos oferecidos em ao menos uma loja: ")    
print("") 

for produto in presentes:
  if produto in loja1 or produto in loja2 or produto in loja3 or produto in loja4:  
    presentes_na_loja1.append(produto)

    
print((presentes_na_loja1))
print("")
   

# 2.Quais produtos são oferecidos em todas as lojas?
print("")
print("_____________________________")  
print("Produtos que são oferecidos em todas as lojas: ")    
print("") 

for produto2 in presentes: 
  if produto2 in loja1 and produto2 in loja2 and produto2 in loja3 and produto2 in loja4:
    presentes_na_loja2.append(produto2)
  
print(presentes_na_loja2)
print("") 

print("_____________________________") 
# 3.Quais produtos não são encontrados em nenhuma loja?
print("") 
print("Produtos que não são encontrados em nenhuma loja: ")    
print("") 

for produto3 in presentes:
  if produto3 not in loja1 and produto3 not in loja2 and produto3 not in loja3 and produto3 not in loja4:
    presentes_na_loja3.append(produto3)
    print(presentes_na_loja3)
print("_____________________________") 
print("") 

# 4. Quais produtos são exclusivos de cada loja?
print("")
print("*****************************")   
print("PRODUTOS EXCLUSIVOS: ")    
print("*****************************") 
  


print("")  

# LOJA 1
for produto4 in presentes:
  if produto4  in loja1 and produto4 not in loja2 and produto4 not in loja3 and produto4 not in loja4:
    exclusivos1.append(produto4)

if len(exclusivos1) != 0 and len(exclusivos1) != 1:
  print("LOJA 1: ", len(exclusivos1),"produtos exclusivos")
  
elif len(exclusivos1) == 1:
  print("LOJA 1: ", len(exclusivos1),"produto exclusivo.")

elif len(exclusivos1) ==0:
  print("LOJA 1: NÃO POSSUI ITENS EXCLUSIVOS")



print("") 

# LOJA 2
      
for produto5 in presentes:
  if produto5 in loja2 and produto5 not in loja1 and produto5 not in loja3 and produto5 not in loja4:
    exclusivos2.append(produto5)
if len(exclusivos2) != 0 and len(exclusivos2) != 1:
  print("LOJA 2: ", len(exclusivos2),"produtos exclusivos")
  
elif len(exclusivos2) == 1:
  print("LOJA 2: ", len(exclusivos2),"produto exclusivo.")

elif len(exclusivos2) ==0:
  print("LOJA 2: NÃO POSSUI ITENS EXCLUSIVOS")
    
    

       
 

print("") 

# LOJA 3

for produto6 in presentes:
  if produto6 in loja3 and produto6 not in loja1 and produto6 not in loja2 and produto6 not in loja4:
      exclusivos3.append(produto6)

if len(exclusivos3) != 0 and len(exclusivos3) != 1:
  print("LOJA 3: ", len(exclusivos3),"produtos exclusivos")
  
elif len(exclusivos3) == 1:
  print("LOJA 3: ", len(exclusivos3),"produto exclusivo.")

elif len(exclusivos3) ==0:
  print("LOJA 3: NÃO POSSUI ITENS EXCLUSIVOS")
    
print("")

# LOJA 4
for produto7 in presentes:
  if produto7 in loja4 and produto6 not in loja1 and produto7 not in loja2 and produto7 not in loja3:
      exclusivos4.append(produto7)
 
if len(exclusivos4) != 0 and len(exclusivos4) != 1:
  print("LOJA 4: ", len(exclusivos4),"produtos exclusivos")
  
elif len(exclusivos2) == 1:
  print("LOJA 4: ", len(exclusivos4),"produto exclusivo.")

elif len(exclusivos4) ==0:
  print("LOJA 4: NÃO POSSUI ITENS EXCLUSIVOS") 
  






print("")
exclusivosgeral =set( exclusivos1 + exclusivos2 + exclusivos3 + exclusivos4)


print("OS itens exclusivos são:", exclusivosgeral)


# 5. Se for possível escolher duas lojas para cobrir o maior número de presentes, 
# qual é a quantidade de presentes possíveis para cobrir dessa forma?



temloja12 = set(presentes_na_loja1 + presentes_na_loja2)


temloja13 = set(presentes_na_loja1 + presentes_na_loja3)


temloja14 = set(presentes_na_loja1 + presentes_na_loja4)


temloja23 = set(presentes_na_loja2 + presentes_na_loja3)


temloja24 = set(presentes_na_loja2 + presentes_na_loja4)




print("")
print("*****************************")   
print("MELHORES LOJAS: ")    
print("*****************************") 

if len(temloja12) > len(temloja13) and len(temloja12) > len(temloja14) and len(temloja12) > len(temloja24):
  print("*****************************") 
  print("As lojas 1 e 2 possuem o maior número de presentes")
  print("*****************************") 
if len(temloja13) > len(temloja12) and len(temloja13) > len(temloja14) and len(temloja13) > len(temloja24):
  print("*****************************") 
  print("As lojas 1 e 3 possuem o maior número de presentes")  
  print("*****************************") 
if len(temloja14) > len(temloja12) and len(temloja14) > len(temloja14) and len(temloja14) > len(temloja24):
  print("*****************************") 
  print("As lojas 1 e 4 possuem o maior número de presentes")  
  print("*****************************") 





print("A loja 1 tem ", len(presentes_na_loja1), "itens.") 
print("")
print("")   
print("A loja 2 tem ", len(presentes_na_loja2), "itens.") 
print("")
print("")
print("A loja 3 tem ", len(presentes_na_loja3), "itens.") 
print("")
print("")
print("A loja 4 tem ", len(presentes_na_loja4), "itens.") 
print("")
print("")           

print("Na loja 1 e loja 2 temos" , len(temloja12), "presentes.São eles: " , temloja12)
print("Na loja 1 e loja 3 temos" , len(temloja13), "presentes.São eles: " , temloja13)
print("Na loja 1 e loja 4 temos" , len(temloja14), "presentes.São eles: " , temloja14)
print("Na loja 2 e loja 3 temos" , len(temloja23), "presentes.São eles: " , temloja23)
print("Na loja 2 e loja 4 temos" , len(temloja24), "presentes.São eles: " , temloja24)

