# Conversor de Imagem para Tons de Cinza e Preto e Branco - DIO

Este projeto é um simples script em Python que permite carregar uma imagem PNG, convertê-la para tons de cinza e preto e branco, e salvar essas versões convertidas como novas imagens na mesma pasta.

## Funcionalidades

- **Carregar uma imagem PNG**: O script solicita ao usuário o nome de um arquivo PNG na mesma pasta do script.
- **Conversão para Tons de Cinza**: A imagem carregada é convertida para tons de cinza.
- **Conversão para Preto e Branco**: A imagem é convertida para um formato preto e branco usando um limiar (default é 128).
- **Salvar as Imagens**: O script salva as imagens convertidas como arquivos PNG na mesma pasta do script.

## Requisitos

Este script não utiliza bibliotecas externas como o Pillow e trabalha diretamente com a manipulação dos dados da imagem em formato binário simples. **Nenhuma biblioteca adicional é necessária** para rodar o código.

## Como Usar

1. **Certifique-se de que o arquivo PNG está na mesma pasta do script**.
2. Execute o script.
3. Quando solicitado, digite o nome do arquivo PNG (incluindo a extensão).
4. O script carregará a imagem, aplicará as conversões para tons de cinza e preto e branco, e salvará as imagens convertidas na mesma pasta.

### Exemplo de uso:

```bash
Digite o nome do arquivo PNG (incluindo extensão): imagem.png
Imagem 'imagem.png' carregada com sucesso!
Imagem em tons de cinza salva como 'imagem_tons_cinza.png'.
Imagem em preto e branco salva como 'imagem_preto_branco.png'.
```
