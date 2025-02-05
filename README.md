# App Preço de Ações

## Descrição do Projeto
Este projeto é um aplicativo interativo desenvolvido em Python utilizando a biblioteca Streamlit. O objetivo é permitir a visualização e análise da evolução dos preços de ações listadas no índice IBOVESPA. Com ele, é possível:

- Filtrar as ações para análise.
- Visualizar os preços das ações ao longo do tempo em um gráfico interativo.
- Avaliar a performance de cada ativo.
- Analisar a performance total de uma carteira de investimentos.

## Funcionalidades
- **Carregamento de dados:**
  - Leitura de títulos do arquivo `IBOV.csv`.
  - Obtenção de histórico de preços das ações utilizando a biblioteca `yfinance`.

- **Interface interativa:**
  - Filtros para selecionar as ações desejadas.
  - Escolha do período de análise através de um controle deslizante.

- **Gráficos e análises:**
  - Visualização dos preços das ações selecionadas em um gráfico de linhas.
  - Cálculo de performance individual dos ativos.
  - Cálculo da performance total da carteira de investimentos.

## Instalação
1. Clone este repositório:
   ```bash
   git clone git@github.com:aironsg/Analisador-de-acoes.git
   ```

2. Certifique-se de que o Python 3.7 ou superior está instalado.

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## Arquivos Necessários
- `IBOV.csv`: Arquivo contendo os códigos das ações do índice IBOVESPA no formato CSV. Cada código deve estar na coluna "Código" e separado por ponto e vírgula.

## Como Executar
1. Execute o aplicativo utilizando o comando:
   ```bash
   streamlit run main.py
   ```

2. Acesse o aplicativo no navegador pelo link fornecido (geralmente `http://localhost:8501`).

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Framework:** Streamlit
- **Bibliotecas:**
  - `yfinance`: Para obter os dados históricos das ações.
  - `pandas`: Para manipulação de dados tabulares.

## Estrutura do Código
### 1. Constantes
- `DATE_INITIAL_HISTORY`: Data inicial do período de histórico das ações.
- `DATE_FINAL_HISTORY`: Data final do período (atualmente configurado como a data atual).

### 2. Funções Principais
- `loading_data(enterprises)`: Carrega os preços históricos de uma lista de ações utilizando o `yfinance`.
- `loading_tickers_locks()`: Lê os códigos das ações do arquivo `IBOV.csv` e os formata para serem utilizados com o `yfinance`.

### 3. Interface do Usuário
- Sidebar para selecionar as ações e o período de análise.
- Gráfico interativo de linhas mostrando a evolução dos preços das ações.
- Exibição da performance individual e total dos ativos.

## Melhorias Futuras
- Adicionar opção para exportar os dados analisados em formato CSV.
- Implementar comparativos com índices de mercado.
- Integrar notificações sobre movimentações relevantes no mercado.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias.


---
**Autor:** Airon

Este foi o meu primeiro projeto utilizando o streamlit.