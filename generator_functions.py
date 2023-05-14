import csv
import random

def gerar_pessoas(n_pessoas):
    with open('./output/guests.csv', 'w', newline='') as csvfile:
        fieldnames = ['Id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for pessoa in range(n_pessoas):
            writer.writerow({'Id': pessoa+1, 'name': f'Guest{pessoa+1}'})

def gerar_conexoes(n_pessoas, min_conexoes, max_conexoes, ind_reciprocidade):
    with open('./output/connections.csv', 'w', newline='') as csvfile:
        fieldnames = ['Id', 'pessoa_1', 'pessoa_2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        #criar e preencher lista de pessoas
        pessoas = []
        for pessoa in range(n_pessoas):
            pessoas.append(f'Guest{pessoa+1}')

        #criar dict com o limite de conexoes partindo do usuario
        conexoes_restantes = {}
        for pessoa in pessoas:
            conexoes_restantes[pessoa] = random.randint(min_conexoes, max_conexoes)

        #para cada pessoa
        #criar uma populacao sem a pessoa
        #random.sample entre min e max conexoes
        #registrar conexoes e talvez reciprocidade
        #a toda conexao de saida, reduzir o valor no dict de conexoes
        #comecar novo ciclo usando a populacao sem as duas
        #  populacao total
        #  populacao amostra (sem anteriores nem atual)
        
        pessoas_amostra = pessoas.copy()
        id_count = 1
        for pessoa_1 in pessoas:
            print(pessoa_1)
            print(pessoas_amostra)
            print(conexoes_restantes)
            
            if pessoa_1 in pessoas_amostra:
                pessoas_amostra.remove(pessoa_1)
            else:
                continue
            
            print(pessoas_amostra)
            for pessoa_teste_conexoes in pessoas_amostra:
                if conexoes_restantes[pessoa_teste_conexoes] <= 0:
                    pessoas_amostra.remove(pessoa_teste_conexoes)
            print(pessoas_amostra)
            print(len(pessoas_amostra))
            reciprocidade = ind_reciprocidade/100
            
            if conexoes_restantes[pessoa_1] > len(pessoas_amostra):
                conexoes_escolhidas = random.sample(pessoas_amostra, len(pessoas_amostra))
            else:
                conexoes_escolhidas = random.sample(pessoas_amostra, conexoes_restantes[pessoa_1])

            for pessoa_2 in conexoes_escolhidas:
                #conexao
                writer.writerow({'Id': id_count,
                                'pessoa_1': pessoa_1,
                                'pessoa_2': pessoa_2})
                conexoes_restantes[pessoa_1] -= 1
                id_count += 1
                #conexao reciproca
                if round(random.random(), 4) < reciprocidade:
                    writer.writerow({'Id': id_count,
                                'pessoa_1': pessoa_2,
                                'pessoa_2': pessoa_1})
                    conexoes_restantes[pessoa_2] -= 1
                    id_count += 1