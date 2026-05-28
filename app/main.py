import os
from datetime import datetime


# Essa função cria o arquivo log.txt;
# Depois escreve a data e hora atual nesse arquivo.
# Além disso, ela printa "Olá, Mundo!" no terminal para
# verificar se o programa está sendo executado corretamente.
def create_archive():
    print("Olá, Mundo!")
    file = "log.txt"
    now = datetime.now()

    # Utilizo o bloco 'with' para garantir que o arquivo seja fechado
    # e salvo corretamente pelo sistema operacional, mesmo que ocorra um erro
    # durante a escrita.
    # Uso o encoding 'utf-8' para que palavras com acento,
    # como "Olá", não quebrem se o log for lido em um sistema Linux
    # futuramente.
    # O modo 'a' (append) foi escolhido para adicionar novos registros no final
    # do arquivo, protegendo o histórico de execuções anteriores.
    with open(file, "a", encoding="utf-8") as arquivo:
        arquivo.write("\nOlá, mundo!\n")
        arquivo.write("Este é um arquivo de texto criado em Python.\n")
        arquivo.write(f'Dia de hoje: {now.strftime("%d/%m/%Y")}\n')
        arquivo.write(f'Hora atual [HH:MM:SS]-> {now.strftime("%H:%M:%S")}\n')
        arquivo.write(f'Hora atual [AM/PM] -> {now.strftime("%I:%M %p")}\n')


# Essa função tem o propósito de deletar o arquivo,
# para testes eventuais e não ser necessário deletar à mão.
def delete_archive():
    arquivo = "log.txt"
    try:
        os.remove(arquivo)
        print("Arquivo deletado com sucesso!")
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")


create_archive()
# delete_archive()
