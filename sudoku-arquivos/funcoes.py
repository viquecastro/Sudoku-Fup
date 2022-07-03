# 01 - Função para a organização e print da grade do jogo 
# apartir de uma lista de coordenadas e valores:
def montarGrade(c):
  grade = [[' '] * 9 for x in range(9)]
  # Referências das colunas da grade (A,B,...,'I') aos índices das colunas da matriz 'grade':
  colunas = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'a':0, 'b':1, 
  'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8}

  # Verificação do conteúdo da jogada e inserção do valor na matriz 'grade':
  for x in c:
    try:
      grade[int(x[2]) -1][int(colunas[x[0]])] = x[4]
    except:
      print(f"A Jogada '{x}' é inválida!")
  
  # Print da grade formatada:
  print("     A   B   C    D   E   F    G   H   I    ")
  print('  ++---+---+---++---+---+---++---+---+---++  ')


  for i in range(9):
    print(str(i + 1) + f' || {grade[i][0]} | {grade[i][1]} | {grade[i][2]} || {grade[i][3]} |'
    f' {grade[i][4]} | {grade[i][5]} || {grade[i][6]} | {grade[i][7]} | {grade[i][8]} || ' + str(i+1))

    if i == 2 or i == 5:
      print("  ++===+===+===++===+===+===++===+===+===++ ")
    else:
      print('  ++---+---+---++---+---+---++---+---+---++ ')

  print("     A   B   C    D   E   F    G   H   I    ")



# 02 - Função para a retirada de possíveis espaços existentes na 'jogada' que poderiam 
# dificultar a verificação dos valores:
def organizarEntradas(data):
  if str(type(data)) == "<class 'str'>":
    return data.replace(" ", "")
  elif str(type(data)) == "<class 'list'>":
    for i in range(len(data)):
      data[i] = data[i].replace(" ", "")
    return data


# 03 - Função que acessa um arquivo e retorna uma lista com as jogadas/dicas contidas nele:
def acessarArquivo(arq):
    l = []
    data = open(arq, 'r')
    for valor in data:
        valor = valor.strip()
        l.append(valor)
    return l

# 04 - Função que verifica se as jogadas contidas em uma lista ou inseridas pelo jogador
# estão dentro das regras do jogo:

def matriz(lin, col, val):
  m = [[val] * col for _ in range(lin)]
  return m

def verificador(col,lin,valor):
  
#VERIFICAR OS QUADRADOS 3X3
  passe = False
  if lin-1 <= 2 and col-1 <=2:
    for i in range(3):
      for j in range(3):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 <= 2 and col-1 > 2 and col-1 <= 5:
    for i in range(3):
      for j in range(3,6):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 <=2 and col-1 >= 6:
    for i in range(3):
      for j in range(6,9):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 3 and lin-1 <= 5 and col-1 <= 2:
    for i in range(3,6):
      for j in range(3):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 3 and lin-1 <= 5 and col-1 >=3 and col-1 <= 5:
    for i in range(3,6):
      for j in range(3,6):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 3 and lin-1 <= 5 and col-1 >= 6:
    for i in range(3,6):
      for j in range(6,9):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >=6 and col-1 <=2:
    for i in range(6,9):
      for j in range(3):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 6 and col-1 >= 3 and col-1 <= 5:
    for i in range(6,9):
      for j in range(3,6):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break
  elif lin-1 >= 6 and col-1 >= 6:
    for i in range(6,9):
      for j in range(6,9):
        if a[i][j] == valor :
          print("Jogada impossibilitada pelo quadrado 3x3")
          passe = True
          break

  if lin-1 < 0 or col-1 < 0 or valor <= 0 or lin-1 > 9 or col-1 > 9 or valor > 9:
    
    print("Jogada impossibilitada")
    passe = True
 
  while passe == False:

    a[lin-1][col-1] = valor
    
  #VERIFICAR AS LINHAS
    for j in range(9):
      if a[lin-1][col-1] == a[lin-1][j] and j!= col-1 and a[lin-1][col-1] > 0:
        a[lin-1][col-1] = " "
        print("Jogada impossibilitada pela linha")
        print("Tente novamente")
        break
  #VERIFICAR AS COLUNAS

    for i in range(9):
      if a[lin-1][col-1] == a[i][col-1] and i != lin-1 and a[lin-1][col-1] > 0:
        a[lin-1][col-1] = ""
        print("Jogada impossibilitada pela coluna")
        print("Tente novamente")
        break
    passe = True

a = matriz(9,9,"")
repetidor = True
while repetidor:
  x = input()
  v = x.replace(":",",")
  v = list(v.split(","))
  v[0] = int(v[0])
  v[1] = int(v[1])
  v[2] = int(v[2])
  v = verificador(v[0],v[1],v[2])

  for i in range(9):
    for j in range(9):
      print(f"[{a[i][j]:^3}]", end="")
    print("")

# 05 - Função que verifica se uma jogada coincide com uma pista:


# 06 - Função que verifica se uma jogada é válida:
def validar(jogadaa):
    col=['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
    jogadaa=input()
    jogada=jogadaa.replace(':',',')
    jogada=jogada.split(',',2)
#transformando as celulas da lista nos seus respectivos tipos corretos
    j=jogada[0].upper()
    i=int(jogada[1])
    k=int(jogada[2])
#condições pra validar a jogada
    if type(j)!=str or type(i)!=int or type(k)!=int or j not in col or i>9 or i<1 or k>9 or k<1:
        print('Jogada Inválida.Entre um novo valor.') 
        return validar
    else:
        print('Jogada Válida.')

# 07 - Função que deleta uma jogada requerida pelo jogador:
def d(m,n):
    matriz(9,9,' ')
    
    if type(matriz[n][m]) == str:
        print('Uma pista não pode ser apagada')
    else:
        matriz[n][m] = ' '
        
 
 # 08 - Função que converte os números da coluna em letras:
  def num_letra(valor):
    col={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9}

    for c in col:
        if valor==col[c]:
            print(c)


 # 09 - Função que converte letras da coluna em números:
  def letra_num(valor):
    col=['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I']
    valor = valor.upper()
    for i in range(10):
        if valor == col[i-1]:
            print(i)



