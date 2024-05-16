import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

'''FUNÇÂO CRIADA POR MIM'''
def compara_assinatura(as_a, as_b):

    # Diferença absoluta entre cada elemento das assinaturas
    diferenca_wal = abs(as_a[0] - as_b[0])
    diferenca_ttr = abs(as_a[1] - as_b[1])
    diferenca_hlr = abs(as_a[2] - as_b[2])
    diferenca_sal = abs(as_a[3] - as_b[3])
    diferenca_sac = abs(as_a[4] - as_b[4])
    diferenca_pal = abs(as_a[5] - as_b[5])

    # Soma das diferenças absolutas
    soma_diferencas = diferenca_wal + diferenca_ttr + diferenca_hlr + diferenca_sal + diferenca_sac + diferenca_pal

    # Grau de similaridade (menor valor indica maior similaridade)
    grau_similaridade = soma_diferencas / 6

    #retorna o grau de similaridade arredondado (2 casas decimais)
    return round(grau_similaridade, 2)

'''FUNÇÂO CRIADA POR MIM'''
def calcula_assinatura(texto):

    # Separar o texto em sentenças e frases (funções não definidas no código)
    sentencas = separa_sentencas(texto)
    #definindo listas para armazenar as frases e palavras
    lista_frases = []
    lista_palavras = []

    #loop para separar sentencas em frases
    for sentenca in sentencas:
        lista_frases.extend(separa_frases(sentenca))

    # loop para separar frases em palavras
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))

    #definindo variáveis para armazenar a qtd de caracteres somados
    soma_caracteres = 0
    soma_caracteres_sentenca = 0

    #definindo a quantidade de campos dessas listas em variáveis, como boa prática
    qtd_palavras = len(lista_palavras)
    qtd_sentenca = len(sentencas)
    qtd_frases = len(lista_frases)

    # Calcular o tamanho total de caracteres em todas as palavras
    for palavra in lista_palavras:
        soma_caracteres += len(palavra)

    # Calcular o tamanho total de caracteres em todas as sentenças
    for sentenca in sentencas:
        soma_caracteres_sentenca += len(sentenca)

    # Calcular as características da assinatura:
    # Tamanho médio de palavra (wal)
    wal = soma_caracteres / qtd_palavras

    # Relação Type-Token (ttr)
    ttr = n_palavras_diferentes(lista_palavras) / qtd_palavras

    # Razão Hapax Legomana (hlr)
    hlr = n_palavras_unicas(lista_palavras) / qtd_palavras

    # Tamanho médio de sentença (sal)
    sal = soma_caracteres_sentenca / qtd_sentenca

    # Complexidade média da sentença (sac)
    sac = qtd_frases / qtd_sentenca

    # Tamanho médio de frase (pal)
    pal = soma_caracteres / qtd_frases

    return [wal, ttr, hlr, sal, sac, pal]

'''FUNÇÂO CRIADA POR MIM'''
def avalia_textos(textos, ass_cp):

    similaridades = []

    # Calcular a similaridade de cada texto com o texto infectado
    for i, texto in enumerate(textos):
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_texto, ass_cp)
        similaridades.append((i + 1, similaridade))

    # Encontrar o texto com a menor similaridade (maior probabilidade de infecção)
    texto_infectado = min(similaridades, key=lambda item: item[1])[0]

    return texto_infectado