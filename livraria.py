livraria = []

# Função para cadastrar novo livro
def Cadastrar():
  titulo = input("Digite o título")
  genero = input("Digite o genero")
  subgenero = input("Digite o genero")
  editora = input("Digite a editora")
  copias = input("Digite a quantidade de cópias")
  preco = input("Digite o preço")
  novo_livro = {'título' : titulo,
                'gênero': genero ,
                'subgênero': subgenero,
                'Editora': editora , 
                ' cópias' : copias, 
                'preço': preco }

  novo_livro["título"] = titulo
  novo_livro["gẽnero"] = genero 
  novo_livro["subgẽnero"] = subgenero
  novo_livro["gẽnero"] = editora
  novo_livro["cópias"] = copias
  novo_livro["preco"] = preco            

# Cada livro cadastrado é um dicionário. Cada dicionário será guardado na lista "livraria"
  livraria.append(novo_livro)

def ConsultarTudo():
  for x in livraria:
    print("")
    for n, j in x.items():
      print('{}: '.format(n) ,'{}'.format(j))

# Exemplos de lvros já cadastrados
livro1 = {'titulo': 'Norwegian Wood' ,
'gênero': 'Drama',
'subgênero': 'Romance',
'Editora': 'Alfaguara' ,
'Cópias' : '200',
'Preço': '49,90' }
livraria.append(livro1)

livro2 = {'Título' :'1Q84 vol 1',
'gênero': 'Ficção' ,
'subgênero': 'Fantasia',
'Editora': 'Alfaguara' ,
'Cópias' : '130',
'Preço': '45,90' }
livraria.append(livro2)

livro3 = {'Título' :'O Semhor dos anéis',
'gênero': 'Fantasia' ,
'subgênero': 'Aventura',
'Editora': 'Martons-Fontes' ,
'Cópias' : '130',
'Preço': '65,00' }
livraria.append(livro3)



livro4 = {'Título' :'Harry Potter',
'gênero': 'Fantasia' ,
'subgênero': 'Aventura',
'Editora': 'Rocco' ,
'Cópias' : '160',
'Preço': '47,00' }
livraria.append(livro4)



# Menu
print("******************")
print("ESCOLHA UMA OPÇÃO:")
print("******************")
print("")
print("1.  CONSULTAR ACERVO GERAL")
print("2.  CADASTRAR NOVO TÍTULO")
print("")
print("")



opt = int(input("Digite o número da opção: "))

if opt ==1:
  ConsultarTudo()
  print(opt)
if  opt ==2:
  Cadastrar()
if opt !=1 and opt  !=2:
  print("Digite um número válido")
