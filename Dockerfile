# O docker vai ler esse arquivo e criar o container
# a partir das instruções abaixo

# Ele vai usar a seguinte imagem como interpretador, não sendo necessário
# baixar instâncias. Assim, ele configura o ambiente.
# Usei o python 3.12-slim para facilitar o processamento na criação do container
FROM python:3.12-slim

# Defino qual o espaço de trabalho/onde vai ser executado
WORKDIR /app

# O que copiar para dentro do container
# O 1° '.' significa a pasta atual do windows
# O 2° '.' significa a pasta /app do container
# Sintaxe: copy source dest
COPY . .

# Comando que o container vai executar logo após ser ligado
CMD ["python", "app/main.py"]
