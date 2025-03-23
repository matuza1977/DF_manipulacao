Nesta tarefa, você criará um DataFrame usando diferentes tipos de entrada e realizará operações básicas para entender melhor a estrutura do DataFrame.

    import pandas as pd

    data = {
        'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'Idade': [25, 30, 35, 40],
        'Cidade': ['São Petersburgo', 'Nova York', 'Praga', 'Pafos']
    }

    print(pd.DataFrame(data))
Saída:

          Nome  Idade          Cidade
    0    Alice     25  São Petersburgo
    1      Bob     30        Nova York
    2  Charlie     35            Praga
    3    David     40            Pafos
    
Trabalhando com colunas
Você deve usar o operador de indexação [] para selecionar colunas, realizar indexação booleana ou fatiar linhas.

coluna_idade = df['Idade']  # Seleciona uma única coluna, o resultado é Series
print(coluna_idade)
Saída:

    0    25
    1    30    
    2    35
    3    40
    
Nome: Idade, dtype: int64

        colunas_nome_idade = df[['Nome', 'Idade']]  # Seleciona múltiplas colunas, o resultado é DataFrame
        print(colunas_nome_idade)
Saída:

          Nome  Idade
    0    Alice     25
    1      Bob     30
    2  Charlie     35
    3    David     40
    
    linhas_1_a_2 = df[1:3]  # Seleciona linhas por número, o resultado é DataFrame
    print(linhas_1_a_2)
    
Saída:

          Nome  Idade    Cidade
    1      Bob     30  Nova York
    2  Charlie     35      Praga
    
Lembre-se de que aplicar o operador [] diretamente em um DataFrame é usado principalmente para seleção de colunas e fatiamento básico de linhas. Para seleção de linhas mais avançada ou seleção simultânea de linhas e colunas, você deve usar as funções .loc[] e .iloc[] fornecidas pelo Pandas.

Indexação booleana

    linhas_idade_gt_30 = df[df['Idade'] > 30]  # Seleciona linhas onde os valores na coluna 'Idade' são maiores que 30

    print(linhas_idade_gt_30)
    
Saída:

          Nome  Idade  Cidade
    2  Charlie     35  Praga
    3    David     40 Pafos
    
Seleção por função
Agora vem a parte divertida e desafiadora: passar uma função para indexação. Isso pode ser muito útil quando você está encadeando operações e o índice possui valores diferentes. É muito comum em operações de agrupamento, que veremos mais adiante no curso.

Aqui está um exemplo de passar uma função que filtra as linhas onde os valores na coluna Idade são maiores que 30:

        def filtro_idade(dataframe):
            return dataframe['Idade'] > 30

linhas_idade_gt_30 = df[filtro_idade]  # Seleciona linhas onde os valores na coluna 'Idade' são maiores que 30
print(linhas_idade_gt_30)
Saída:

          Nome  Idade  Cidade
    2  Charlie     35  Praga
    3    David     40 Pafos 
    
Você também pode criar uma função que retorna uma função de filtro:

        def criar_filtro(coluna, limite):
            def _filtro(dataframe):
        return dataframe[coluna] > limite
        return _filtro

filtro_idade = criar_filtro('Idade', 30)
linhas_idade_gt_30 = df[filtro_idade]  # Seleciona linhas onde os valores na coluna 'Idade' são maiores que 30
Tarefa
Adicione uma nova coluna chamada Custo mensal ao DataFrame com os seguintes valores: [50000, 800000, 200000, 500000].
Calcule o Custo anual em milhares e adicione esta coluna ao DataFrame.
 Hint 
Você pode operar com as colunas como se fossem apenas números. Além disso, use o tipo int64 para a coluna `Custo anual em milhares`.


/Users/chris/py_env_numpy/.venv/bin/python /Users/chris/DF_manipulacao/main.py 

          Name  Age              City  Custo mensal  Custo anual em milhares
    0    Alice   25  Saint Petersburg         50000                      600
    1      Bob   30          New York        800000                     9600
    2  Charlie   35            Prague        200000                     2400
    3    David   40            Paphos        500000                     6000

Process finished with exit code 0
