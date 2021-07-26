print('Projeto Detetive')

pgt1 = input("Você telefonou para a vítima?\n").upper().strip()
if pgt1 != var1 and pgt1 != var2:
  print(var3)
pgt2 = input(" Você esteve no local do crime?\n").upper().strip()
if pgt2 != var1 and pgt2 != var2:
  print(var3)
pgt3 = input(" Você mora perto da vítima?\n").upper().strip()
if pgt3 != var1 and pgt3 != var2:
  print(var3)
pgt4 = input(" Você devia para a vítima?\n").upper().strip()
if pgt4 != var1 and pgt4 != var2:
  print(var3)
pgt5 = input(" Você já trabalhou com a vítima?\n").upper().strip()
if pgt5 != var1 and pgt5 != var2:
  print(var3)
pgt1_2 = 0
pgt2_2 = 0
pgt3_2 = 0
pgt4_2 = 0
pgt5_2 = 0

var1 = 'SIM'
var2 = 'NÃO'
var3 = 'RESPOSTA INVÁLIDA'


if pgt1 == var1:
    pgt1_2 = 1
elif pgt1 == var2:
  pgt1_2 = 0
if pgt2 == var1:
    pgt2_2 = 1
elif pgt2 == var2:
  pgt2_2 = 0
if pgt3 == var1:
    pgt3_2 = 1
elif pgt3 == var2:
  pgt3_2 = 0
if pgt4 == var1:
    pgt4_2 = 1
elif pgt4 == var2:
  pgt4_2 = 0
if pgt5 == var1:
    pgt5_2 = 1
elif pgt5 == var2:
  pgt5_2 = 0

soma = pgt1_2+pgt2_2+pgt3_2+pgt4_2+pgt5_2

if soma == 0:
  print('Inocente')
elif soma == 2:
  print('Suspeito')
if soma == 3:
  print('Cúmplice')
if soma == 4:
  print('Cúmplice')
elif soma == 5:
  print('Assassino')