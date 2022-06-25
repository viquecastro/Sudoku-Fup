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

a = matriz(9,9,0)


def verificador(col,lin,valor):
  
  a[lin][col] = valor
  
  if a[lin][col] <= 0 or a[lin][col] > 9:
      jogada = True
      while jogada:
        print("Jogada impossibilitada")
        a[lin][col] = int(input('Digite um novo valor: '))
        if a[lin][col] > 0 and a[lin][col] <= 9:
          jogada = False
  
#VERIFICAR AS LINHAS
  for j in range(col):
    if a[lin][col] == a[lin][j]:
      jogada = True
      while jogada:
        print("Jogada impossibilitada pela linha")
        coluna,linha,val = input("Digite um novo valor: ").split(",")
        coluna = int(coluna)
        linha = int(linha)
        val = int(val)
        a[linha][coluna] = val
        a[lin][col] = a[linha][coluna]
        if a[lin][col] > 0 and a[lin][col] <= 9:
          jogada = False
    
  for j in range(col+1, 9):
    if a[lin][col] == a[lin][j]:
      jogada = True
      while jogada:
        print("Jogada impossibilitada pela linha")
        coluna,linha,val = input("Digite um novo valor: ").split(",")
        coluna = int(coluna)
        linha = int(linha)
        val = int(val)
        a[linha][coluna] = val
        a[lin][col] = a[linha][coluna]
        if a[lin][col] > 0 and a[lin][col] <= 9:
          jogada = False
    
#VERIFICAR AS COLUNAS
  for i in range(lin):
    a[i][col]
    if a[lin][col] == a[i][col]:
      jogada = True
      while jogada:
        print("Jogada impossibilitada pela coluna 1")
        coluna,linha,val = input("Digite um novo valor: ").split(",")
        coluna = int(coluna)
        linha = int(linha)
        val = int(val)
        a[linha][coluna] = val
        a[lin][col] = a[linha][coluna]
        if a[linha][coluna] > 0 and a[linha][coluna] <= 9:
          jogada = False
  for i in range(lin+1, 9):
    a[i][col]
    if a[lin][col] == a[i][col]:
      jogada = True
      while jogada:
        print("Jogada impossibilitada pela coluna 2")
        coluna,linha,val = input("Digite um novo valor: ").split(",")
        coluna = int(coluna)
        linha = int(linha)
        val = int(val)
        a[linha][coluna] = val
        a[lin][col] = a[linha][coluna]
        if a[lin][col] > 0 and a[lin][col] <= 9:
          jogada = False



repetidor = True
while repetidor:
  col,lin,valor = input().split(",")
  col = int(col)
  lin = int(lin)
  valor = int(valor)
  v = verificador(col,lin,valor)

  for i in range(9):
    for j in range(9):
      print(f"[{a[i][j]:^3}]", end="")
    print("")

# 05 - Função que verifica se uma jogada coincide com uma pista:


# 06 - Função que verifica se uma jogada é válida:


# 07 - Função que deleta uma jogada requerida pelo jogador:





