# ChatUDP

Este é um projeto em Python desenvolvido como parte da disciplina de redes na Universidade Federal de Pernambuco (UFPE). O ChatUDP é uma aplicação de chat simples baseada em sockets UDP, projetada para facilitar a comunicação entre clientes em uma rede local.

## Execução

### Servidor

1. Baixe o arquivo ou clone este repositório com o comando:
    ```
    git clone https://github.com/lcs8/ChatUDP.git
    ```

2. Execute o arquivo `CinChatServUDP.py` para iniciar o servidor responsável pelo gerenciamento do chat. Abra um terminal e digite:
    ```
    python3 CinChatServUDP.py
    ```

3. Siga as instruções exibidas no programa.

### Cliente

1. Distribua o arquivo `CinChatClientUDP.py` para os clientes que desejam se comunicar através do chat.

2. Execute o arquivo `CinChatClientUDP.py` em cada cliente. Abra um terminal e digite:
    ```
    python3 CinChatClientUDP.py
    ```

3. Siga as instruções exibidas no programa.

## Recursos

- **Comunicação em Tempo Real**: Mensagens são enviadas e recebidas em tempo real por meio de sockets UDP.
- **Transferência de Arquivos**: Os clientes podem enviar o conteúdo do arquivo `filename.txt` para todos os participantes da sala de bate-papo. Quaisquer alterações feitas neste arquivo antes do envio serão refletidas na mensagem recebida pelos destinatários.
- **Interface Simples**: Interface de linha de comando fácil de usar tanto para o servidor quanto para o cliente.

## Observações

- Certifique-se de que o script do servidor está em execução antes que os clientes tentem se conectar.
- Os clientes devem especificar o endereço IP e a porta do servidor para entrar na sala de bate-papo.
- O aplicativo suporta apenas o envio de arquivos de texto (formato `.txt`), através do `filename.txt`, conforme mencionado acima.

