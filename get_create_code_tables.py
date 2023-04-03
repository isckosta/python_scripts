import pymysql

# Configurações de conexão com o banco de dados
host = 'localhost'
usuario = 'root'
senha = 'sipae'
banco_de_dados = 'sipae_aldeias'
porta = 3308

# Solicita ao usuário que digite os nomes das tabelas separados por vírgula ou *
tabelas_str = input("Digite o nome das tabelas que deseja obter o código CREATE (separe por vírgula) ou '*' para todas as tabelas: ")

if tabelas_str == "*":
    # Consulta SQL para obter o nome de todas as tabelas do banco de dados
    consulta = "SHOW TABLES"
    with pymysql.connect(
        host=host,
        user=usuario,
        password=senha,
        db=banco_de_dados,
        port=porta
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(consulta)
            tabelas = [resultado[0] for resultado in cursor.fetchall()]
else:
    tabelas = tabelas_str.split(",")

# Conexão com o banco de dados
conexao = pymysql.connect(
    host=host,
    user=usuario,
    password=senha,
    db=banco_de_dados,
    port=porta
)

# Loop pelas tabelas
for tabela in tabelas:
    # Consulta SQL para obter as informações sobre a tabela
    consulta = f"SHOW CREATE TABLE {tabela}"
    with conexao.cursor() as cursor:
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        codigo_create = resultado[1]
        
        # Salva o código CREATE em um arquivo .txt com o nome da tabela
        with open(f"{tabela}.txt", "w") as arquivo:
            arquivo.write(codigo_create)

            # Exibe mensagem de sucesso para a tabela atual
            print(f"O código CREATE da tabela {tabela} foi salvo com sucesso no arquivo {tabela}.txt")

# Fechando a conexão
conexao.close()

# Exibe mensagem de sucesso
if len(tabelas) == 1:
    tabela = tabelas[0]
    print(f"Código CREATE da tabela {tabela} foi salvo com sucesso no arquivo {tabela}.txt")
else:
    print("Códigos CREATE das tabelas informadas foram salvos com sucesso em arquivos .txt")
