import sys

ref_arquivo = open("/home/ednilson/projects/estudos/pi/imagem.ppm", "r")
gravar_arquivo = open("/home/ednilson/projects/estudos/pi/imagemTeste.ppm", "w")
tamanho_arquivo = 0
linhas_arquivos = []
width = 0
height = 0
typefile = ""

for linha in ref_arquivo:
      linhas_arquivos.append(linha.replace('\n',''))
      tamanho_arquivo = tamanho_arquivo + 1

typefile = linha[0]

width = linhas_arquivos[2][0]
height = linhas_arquivos[2][1]

i=0

while(i < len(linhas_arquivos)):
  linha = linhas_arquivos[i] 
  linha_clean = linha.split()
  linha_to_print = ""
  j = 0
  if(i> 3):
    while(j < len(linha_clean)):
      if(j==0):
        linha_to_print  = str(255-int(linha_clean[j]))
      elif((j)%int(3) == 0):
        linha_to_print = linha_to_print + "   " + str(255-int(linha_clean[j]))
      else:
        linha_to_print = linha_to_print + " " + str(255-int(linha_clean[j]))
      j = j + 1
    gravar_arquivo.write(linha_to_print + "\n")   
  else:
      gravar_arquivo.write(linha + "\n")

  i  = i + 1
