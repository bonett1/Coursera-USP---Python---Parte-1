# Oii, Pedro aqui! 👋
## Hoje vim mostrar um pouco do meu conhecimento em Python.
Há alguns dias atrás eu finalizei meu curso 'Introdução à Ciência da Computação com Python Parte 1' da USP. 🚀

Este curso foi dado pelo professor Fabio Kon, que inclusive tem uma didática ótima, e com ele aprendi desde como instalar o python no meu PC, até condicionais, variáveis, repetições while e for, funções e manipulação de listas em python. 
Além disso, o Fabio explicou sobre boas práticas em python, a importância de realizar testes automáticos e também como utilizar o depurador.

### Projeto Final
Este projeto reúne todos os conteúdos vistos no durante o curso. E consistia em um programa detector de plágio, onde os autores que escreveram textos plagiados estão infectados por uma doença chamada COH-PIAH.
Foi dado algumas funções prontas com base na biblioteca 're' que facilitaram o desenvolvimento do projeto. Por meio das assinaturas de cada autor foi possível detectar de quem é cada texto, e com base em uma assinatura padrão de pessoas infectadas foi possível detectar quais dos autores estavam infectados.

ℹ️ As assinaturas consistem em traços linguísticos como tamanho médio de palavra, relação Type-Token, razão Hapax Legomana, tamanho médio de sentença, complexidade de sentença, tamanho médio de frase.

#### Meu objetivo era criar 3 funções:

- compara_assinatura(as_a, as_b):
> Esta função compara a assinatura padrão (de uma pessoa infectada) com as assinaturas de outros textos.

- calcula_assinatura(texto):
> Esta função calcula as assinaturas dos textos dados, serão dados textos no 'input' onde serão convertidos em assinaturas, uma lista com os traços linguísticos daquele texto e posteriormente será comparada com a função compara_assinatura(as_a, as_b)

- avalia_textos(textos, ass_cp):
> Esta função irá availiar os textos dados no 'input', então ela irá "chamar" as outras duas funções que eu criei para poder avaliar os textos dados com a assinatura padrão.

#### Prévia do código que fiz:
https://github.com/bonett1/Coursera-USP---Python---Parte-1/assets/118580493/805f19fe-5632-4b74-9812-b63b8b697f37

#### Veja o código completo: [código_completo ](https://github.com/bonett1/Coursera-USP---Python---Parte-1/blob/e2bb10235729ef61b139cda3256ad05c2860f914/coh_piah.py)

## Obrigado pela sua atenção 😊
Se você chegou a ler até aqui, MUITO OBRIGADO, mesmo, seu tempo é muito importante e agradeço por gastá-lo vendo um projeto meu.

Estou apenas começando uma jornada de ser um Cientista de Dados, e Python será muito importante para este meu objetivo, me siga para mais conteúdos e projetos de um estudante de Data Science.

Tchau.
