# Como Rodar a Aplicação

1. Clonar o repositório: https://github.com/lmrissi/desafio-dev.git
2. Abrir o terminal na pasta do projeto e subir o docker:
````
docker-compose up --build
````

Após executar este comando, o docker realizará a instação das dependências do projeto, posteriormente criará uma instância do banco de dados, realizará as migrações e a importação dos dados default a partir de uma fixture. Quando todos os processos forem finalizados, o servidor estará disponível.

Para executar os testes da aplicação é necessário que o docker esteja rodando e executar os seguintes comandos em um novo terminal:
````
docker-compose exec web bash
````
````
python manage.py test
````

# API

A camada de API conta com dois enpoints:
1. api/upload:
Este endpoint é responsável fazer o parse do arquivo que foi importado pelo usuário e salvar os dados formatados no banco de dados. Quando a importação é feita com sucesso, o enpoint redireciona o usuário para a view de listagem de transações.
2. api/list:
Este endpoint é responsável por realizer a busca dos dados de cnabs no banco de dados e retornar os dados de transações e o total do balanço de cada loja.

# Front-end

Esta é a camada da aplicação responsável por renderizar os templates e os arquivos estáticos. Os arquivos de template foram criados utilizando HTML, CSS e Javascript. 

A interação entre as páginas estáticas e a camada de API foi feita utilizando a biblioteca JQuery a partir de requisições assíncronas (Ajax). A página de upload possui uma requisição do tipo POST para enviar o arquivo importado para o endpoint 'api/upload', já a página de listagem carrega os dados de transações dinamicamente buscando os dados no endpoint 'api/list'.

O front-end disponibiliza duas urls:

1. /: Página de upload do arquivo cnab.
2. /list: Página responsável por renderizar a listagem das transações.