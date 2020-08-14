# servicos

O serviço 1 poderá ser gerado a partir do fonte my_proj\servico_um através do terminal.
Comando: python my_proj\servico_um.py

* O serviço 1 vai gerar números pares aletatóriamente no valor entre 0 e 1000.
* Foi colocado um limite para não ficar gerando dados o tempo todo

O serviço 2 poderá ser gerado a partir do fonte my_proj\servico_dois através do terminal.
Comando: python my_proj\servico_dois.py

* O serviço 1 vai gerar números impares aletatóriamente no valor entre 0 e 1000.
* Foi colocado um limite para não ficar gerando dados o tempo todo

O serviço 3 e 4 devem ser gerados a partir do Django.
Utilizar o comando manage.py runserver
caminho: localhost/servico

Ao clicar no botão processar, o sistema vai buscar os valores na base adicionados na tabela servico_um e servico_dois e vai multiplicar os valores.
Após multiplicar os valores o sistema vai publicar os 100 números processados para o serviço 4.

Os número serão publicados na tela do serviço 4.
