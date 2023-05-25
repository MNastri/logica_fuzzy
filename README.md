# Objetivo
Fazer uma demonstração de um sistema que utiliza lógica fuzzy para transformar 
um conjunto de entradas difusas em uma saida nítida.  
Conteúdo baseado nos vídeos abaixo, bem como a documentação oficial da biblioteca skfuzzy:  
[Aula 01 - Lógica Fuzzy - parte 1](https://www.youtube.com/watch?v=9Oe21TX5lMQ&ab_channel=Jos%C3%A9Ricardo)  
[Aula 02 - Lógica Fuzzy - implementação em python - parte 2](https://www.youtube.com/watch?v=oTj6UppBsRk&t=18s&ab_channel=Jos%C3%A9Ricardo)  
[Aula 03 - Lógica Fuzzy - implementação em Python - parte 3](https://www.youtube.com/watch?v=wfd5eFgU8R0&t=2s&ab_channel=Jos%C3%A9Ricardo)

# Contextualização do problema
Gerar uma nota de 0 a 10 para a compra de um veículo com base nas características
preço de compra e rendimento - quantos kilometros o veículo roda por litro de combustível -
utilizando a lógica fuzzy

# Lógica fuzzy e Lógica clássica
A lógica clássica é uma lógica binária, onde uma relação existe ou não existe, 
enquanto a Lógica fuzzy considera que a relação de uma váriavel pode ser representada
por um grau de intensidade.

A Lógica fuzzy vem do fato que no dia a dia não é possível identificar definitivamente
qual a relação exata entre uma váriavel e um conjunto (um veículo vendido a R$40.000,00 é caro ou barato?).   
Para modelar esses tipos de problema foi necessário criar a lógica fuzzy. 

#### Exemplo lógica clássica
se o preço do veículo é maior que ou igual a 80.000 então ele é caro, senão é barato.  

#### Exemplo lógica difusa
se o preço do veículo é 80.000 então ele é 0% barato 33% médio 66% caro.

# Instalação  
`pip install -r requirements.txt`  

# Utilização
Executar o arquivo `main.py` passando o preço e o rendimento do veículo.

### Passo-a-Passo
Abra o terminal no diretório que está o arquivo `main.py` e invoque o script  
`python -m main preco rendimento --exibir-graficos`

### argumentos
preco = "preço do veículo"  
rendimento = "km/l que o carro rende"  
`--exibir-graficos`[OPCIONAL] Exibir gráficos das funções de pertencimento