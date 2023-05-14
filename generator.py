from generator_functions import *

# variaveis de processo
# verificacoes
n_pessoas = int(input("Quantas pessoas a serem geradas? >>> "))

print("sobre min_conexoes: ver notas técnicas (no gitignore)")
min_conexoes = int(input("Qual o minimo de conexões? >>> "))

max_conexoes = int(input("Qual o máximo de conexões? >>> "))
if max_conexoes > n_pessoas:
    raise ValueError("Não podem existir mais conexões que pessoas")

ind_reciprocidade = float(input("Qual o ind de reciproc nas conexoes? [Em 0.00%] >>> "))
if ind_reciprocidade > 100:
    #erro só pq realmente pode rolar esse vacilo
    raise ValueError("ind_reciprocidade tem que ser menor ou igual a 100")

min_eventos = int(input("Qual o min de eventos que um user vai se conectar? >>> "))
if min_eventos < 1:
    #erro só pq realmente pode rolar esse vacilo
    raise ValueError("min_eventos tem que ser maior que 1")

print('Nota: max_eventos tipo um simulador de "cansaço" dentro da plataforma')
max_eventos = int(input("Numero maximo de conexoes a eventos? >>> "))
if max_conexoes > n_pessoas:
    raise ValueError("Não pode conectar a mais eventos que existem")

# processos de geraçaõ de arquivos
gerar_pessoas(n_pessoas)
gerar_conexoes(n_pessoas, min_conexoes, max_conexoes, ind_reciprocidade)