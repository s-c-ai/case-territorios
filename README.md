# Case Técnico - Análise de Dimensão de Territórios

Você deve construir uma solução de análise de dados para auxiliar a análise de territórios brasileiros quanto à sua dimensão.

A sua solução deve ser capaz de responder as seguintes perguntas:

1. Qual a dimensão de um território.

2. Qual a diferença entre as dimensões de dois territórios.

A solução deve ser desenvolvida como uma ferramenta de CLI.

## Para desenvolvimento

Para desenvolver a solução, você deve fazer um fork desse repositório e ao final deve-se solicitar um Pull Request para o repositório. O Pull Request será considerado como "Disponível para revisão".

## Dados Disponíveis

Os dados estão distribuídos em três fontes:

1. SQLite `database.db` que possui os dados de dimensão de alguns territórios já previamente coletados.

2. CSV `dict.csv` com o dicionário do código do território e o nome.

3. API do IBGE com as informações do território disponível no endpoint https://servicodados.ibge.gov.br/api/v3/malhas/estados/{id}/metadados, em que {id} é o id do território.

Mais informações sobre os dados estão disponíveis em data/README.md.

## Resultados necessários

Aqui estão as features que **devem** estar implementadas na solução:

### CLI

O CLI deve conter dois comandos:

1. Informar a dimensão do território e gerar uma imagem com um gráfico de colunas contendo a dimensão e o nome do território.

```bash
>>> dimensao {id} {path/to/image.png}
```

```bash
>>> Nome: {território} | Dimensão: {dimensao}km2 | Grafico: {path/to/image.png}
```

2. Informar a diferença entre dois territórios e gerar uma imagem contendo um gráfico de colunas com as dimensões dos dois territórios e os seus nomes.

```bash
>>> comparar {id1} {id2} {path/to/image.png}
```

```bash
>>> {Territorio1}: {dimensao1}km2 | {Territorio2}: {dimensao2}km2 | Diferença: {diferenca}km2 | Grafico: {path/to/image.png}
```

#### Observações

É necessário que os dados sejam consultados **primeiramente** na `database.db` e, caso não haja dados, deve-se buscar na API.

Utilize o `dict.csv` conforme necessário.

### Features opcionais

1. Aceitar tanto o id quanto o nome do território nos comandos

2. Salvar dados que já foram consultados para não repetir requisições

3. Testes unitários

4. CI com o Github Actions

## O que será avaliado

1. Pensamento crítico

2. Planejamento da solução

3. Claridade e coerência no código

4. Features requisitadas em "Resultados necessários"
