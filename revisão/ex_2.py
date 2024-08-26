"""
Um Professor precisa sortear bombons para diversos alunos. 
esses alunos serão sorteador randômmicamente.
o número deve corresponder ao número do diário.
"""

import random

# looping - iteração - repetição - laço 

while True:
    # pedrão snake_case (pep-8)
    sorteio_turma = random.randint(1,27)
    print (sorteio_turma)
    resposta = input ("Deseja sortear outro numero ? (s/n)").strip().lower()

    if resposta != "s":
        print ("Encerrando o Sorteio")
        break