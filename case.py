# assume que nao tem espaços em path/to/image.png
import sqlite3 as sql
import requests
import csv
import matplotlib.pyplot as plt

nome_csv = 'data/dict.csv'
nome_db = 'data/database.db'


def mostrar(territorios, caminho):
    nomes, dimensoes = zip(*territorios)
    plt.bar(nomes, dimensoes)
    plt.savefig(caminho, bbox_inches='tight')
    # plt.show()
    plt.close()

def buscar(territorio):
    id = nome2id.get(territorio, territorio)
    nome = id2nome.get(territorio, territorio)

    query = db.execute(f'SELECT nome, dimensao FROM territorios WHERE id={id}')
    resultado = query.fetchone()

    # se nao esta na base local, busca no IBGE e insere na base
    if resultado is None: 
        resposta_ibge = requests.get(f'https://servicodados.ibge.gov.br/api/v3/malhas/estados/{id}/metadados')
        if resposta_ibge.status_code == 200:
            data = resposta_ibge.json()
            dimensao = float(data[0]['area']['dimensao'])
            db.execute(f'INSERT INTO territorios VALUES ({id}, "{nome}", {dimensao})')
            con.commit()
            resultado = (nome, dimensao)
        else:
            print('Id não encontrado na base local nem no IBGE')

    return resultado

def dimensao(territorio, grafico):
    territorio = buscar(territorio)
    print(f'Nome: {territorio[0]} | Dimensão: {territorio[1]}km2 | Grafico: {grafico}')
    mostrar([territorio], grafico)

def comparar(territorios, grafico):
    territorios = list(map(buscar, territorios))

    for territorio in territorios:
        print(f'{territorio[0]}: {territorio[1]}km2', end=' | ')
    print(f'Diferença: {territorios[0][1] - territorios[1][1]}km2 | Grafico: {grafico}')
    mostrar(territorios, grafico)
    
def ler_entrada():
    entrada = input()
    if entrada == 'sair': 
        return [entrada] 
    return entrada.split()
    

if __name__ == '__main__':
    
    # abre o banco de dados como "db"
    con = sql.connect(nome_db)
    db = con.cursor()
    
    # consome o csv e constroi um dict mapeando nomes para ids
    nome2id, id2nome = {}, {}
    with open(nome_csv, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            nome2id[linha[1]] = linha[0]
            id2nome[linha[0]] = linha[1]
    
    # loop principal do programa
    while True:
        comando = ler_entrada()
        if comando[0] == 'dimensao':
            dimensao(comando[1], comando[2])
        elif comando[0] == 'comparar':
            comparar(comando[1:-1], comando[-1])
        elif comando[0] == 'sair':
            break
        else:
            print('comando não reconhecido')