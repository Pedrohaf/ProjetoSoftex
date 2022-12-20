# Modulo 2 atv 1

### metodos http
    * GET
        - O método GET solicita a representação de um recurso específico. Requisições utilizando o método GET devem retornar apenas dados.
            - exemplo: 
               ' GET /index.html '
    * HEAD
        - O método HEAD solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta.
            - exemplo: 
               ' HEAD /index.html '
    * POST
        - O método POST é utilizado para submeter uma entidade a um recurso específico, frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.
            - exemplo: 
                '   POST / HTTP/1.1
                    Host: foo.com
                    Content-Type: application/x-www-form-urlencoded
                    Content-Length: 13

                    say=Hi&to=Mom    '

    * PUT
        - O método PUT substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.
            - exemplo: 
                PUT /new.html HTTP/1.1
                Host: example.com
                Content-type: text/html
                Content-length: 16
                <p>New File</p>

    * DELETE
        - O método DELETE remove um recurso específico.
            - exemplo:
                HTTP/1.1 200 OK
                Date: Wed, 21 Oct 2015 07:28:00 GMT
                <html>
                <body>
                    <h1>Arquivo removido.</h1>
                </body>
                </html>


    * CONNECT 
        - O método CONNECT estabelece um túnel para o servidor identificado pelo recurso de destino.
            - exemplo: 
                CONNECT server.exemplo.com:80 HTTP/1.1
                Host: server.exemplo.com:80
                Proxy-Authorization: basic aGVsbG86d29ybGQ=

    * OPTIONS
        O método OPTIONS é usado para descrever as opções de comunicação com o recurso de destino.
            - exemplo:
                HTTP/1.1 200 OK
                Allow: OPTIONS, GET, HEAD, POST
                Cache-Control: max-age=604800
                Date: Thu, 13 Oct 2016 11:45:00 GMT
                Expires: Thu, 20 Oct 2016 11:45:00 GMT
                Server: EOS (lax004/2813)
                x-ec-custom-error: 1
                Content-Length: 0

    * TRACE
        - O método TRACE executa um teste de chamada loop-back junto com o caminho para o recurso de destino.
            - exemplo:
                TRACE /index.html


    * PATCH 
        - O método PATCH é utilizado para aplicar modificações parciais em um recurso.
            - exemplo 
                PATCH /file.txt HTTP/1.1
                Host: www.example.com
                Content-Type: application/example
                If-Match: "e0023aa4e"
                Content-Length: 100
                [descrição das mudanças]

## o que é WSDL
 - WSDL é uma notação XML para descrever um serviço da web. Uma definição WSDL indica a um cliente como compor uma solicitação de serviço da web e descreve a interface que é fornecida pelo provedor de serviços da web.

IBM® Integration Bus suporta o WSDL 1,1, conforme definido no documento a seguir emitido pelo World Wide Web Consortium (W3C): Linguagem de Descrição de Serviços Web (WSDL) 1,1. IBM Integration Bus o suporte para WSDL também adere ao perfil do Web Services Interoperability Organization (WS-I) Basic profile 1,1; veja Web Services Interoperability Organization (WS-I).

Uma definição WSDL é dividida em seções separadas que especificam a interface lógica e os detalhes físicos de um serviço da web. Os detalhes físicos incluem informações de terminal, como número da porta HTTP e informações de ligação que especifica como a carga útil SOAP é representada e qual transporte é utilizado.