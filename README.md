# Sistema de Consulta de Países (CLI)

**Uma ferramenta de linha de comando rápida e interativa para consultar dados demográficos, geográficos e econômicos de qualquer país do mundo.**

Esta aplicação foi desenvolvida em Python para consumir a [REST Countries API v3.1](https://restcountries.com/). O projeto foca em performance, resiliência na extração de dados e usabilidade, servindo como uma interface leve para obter informações globais diretamente pelo terminal.

## Funcionalidades Principais

* **Busca Otimizada (Single Request):** O banco de dados de países é baixado integralmente para a memória RAM apenas uma vez ao iniciar o programa, garantindo pesquisas instantâneas e evitando bloqueios por excesso de requisições (Rate Limiting) na API.
* **Pesquisa Bilíngue:** Suporta buscas parciais tanto pelo nome comum do país em Inglês quanto em Português (ex: pesquisar por "Korea" ou "Coreia" retornará resultados válidos).
* **Sistema de Desempate Automático:** Caso a pesquisa retorne múltiplos países (ex: pesquisar por "Guine"), o sistema gera dinamicamente um menu para o usuário escolher o país exato antes de exibir as informações.
* **Programação Defensiva (Segurança de Dados):** Utiliza métodos seguros de extração de chaves (`.get()` encadeados) e tipagem segura (`isinstance`), impedindo que o programa sofra falhas caso a API retorne dados nulos ou em formatos inesperados.
* **Menu de Navegação Interativo:** Submenu que permite ao usuário filtrar apenas as informações que deseja ler sobre o país selecionado.

## Informações Disponíveis

Ao selecionar um país, você pode visualizar os seguintes dados:
1. Capital
2. População (com formatação de milhar)
3. Área Territorial (km²)
4. Região e Sub-região
5. Idiomas Oficiais
6. Moedas (Nome e Símbolo)
7. Fusos Horários

## Pré-requisitos

Para rodar este projeto, você precisará do [Python 3.6+](https://www.python.org/downloads/) instalado na sua máquina e da biblioteca `requests`.

## Instalação e Execução

1. Clone este repositório ou baixe o arquivo do código fonte.
2. Abra o terminal na pasta do projeto.
3. Instale as dependências necessárias executando:
   ```bash
   pip install requests
   ```
   
Inicie o programa:
   ```bash
   python/3 countries.py
   ```

## Exemplo de Uso

========================================
   SISTEMA DE CONSULTA DE PAISES
========================================
Digite o nome do pais (ex: Brasil)
Ou digite '0' para sair.

Pesquisa: sul

Foram encontrados 3 paises:
[1] Coreia do Sul
[2] África do Sul
[3] Ilhas Geórgia do Sul e Sandwich do Sul
[0] Cancelar

Qual deles voce deseja? Digite o numero: 1

--- PAÍS SELECIONADO: COREIA DO SUL ---
Escolha qual informacao voce deseja ver:
1. Capital
2. Populacao
...
Tratamento de Erros Implementado

Timeout de Conexão: O programa aguarda até 8 segundos pela resposta da API. Se o servidor estiver instável, a conexão é encerrada de forma limpa.

HTTP Errors: Implementação de raise_for_status() para capturar códigos HTTP de erro (ex: 404, 500).

Dados Ausentes: Se um país não possuir Forças Armadas, Moeda ou Capital oficial (como a Antártida), o sistema exibe mensagens de "Dado indisponível" em vez de gerar exceções (KeyError).

API Utilizada
REST Countries - Endpoint de países para dados globais.
