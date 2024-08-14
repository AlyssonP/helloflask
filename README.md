# Hello Flask

Bem-vindo ao projeto **Hello Flask**! Esta aplicação foi desenvolvida como parte das aulas de Programação Web 2, com o objetivo de aprender e aplicar conceitos de desenvolvimento de API RESTful usando o framework Flask.

## Tecnologias Utilizadas
- Flask
- Sqlite3

## Configuração e Execução
1. **Criar Ambiente Virtual (venv)**:
   - Cria um ambiente virtual isolado para instalar as dependências do projeto sem afetar o sistema global.

   Ubuntu
    ```
    virtualenv venv
    ```

2. **Ativar o Ambiente Virtual**:
   - Ativa o ambiente virtual, permitindo que você instale pacotes e execute a aplicação no contexto desse ambiente.

   Ubuntu
    ```
    source venv/bin/activate
    ```

3. **Instalar Dependências**:
   - Instala as bibliotecas e pacotes listados no arquivo `requirements.txt`, que são necessários para a aplicação.
    ```
    pip install -r requirements.txt
    ```
4. **Executar a Aplicação**:
   - Inicia a aplicação Flask.
   ```
   flask run
   ```