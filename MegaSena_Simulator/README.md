# Gerador de Números da Mega Sena

### Simulador de criação de jogos de seis números para Mega Sena, de duas formas de sintaxe, a correta e a fácil de entender.

- Neste projeto tive de importar a biblioteca ```Random```;
- No primeiro código, eu criei um array e fui adicionando número um a um;
- Após concatenei um texto junto dos números do array, buscando-os um a um no array através de seus índices;

- Já no segundo código, utilizei a função ```random.sample(range(1,61), 6)```, 
criando um array de seis dígitos no intervalo/range de 1 a 60;
- Utilizei o ```sorted``` em ```sorted(random.sample(range(1, 61), 6))``` para ordenar os números na lista;
- Por fim imprimi a lista completa utilizando ```*numeroSorteado1```, concatenado com a string inicial.
