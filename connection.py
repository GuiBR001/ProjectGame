import oracledb

try:
    conn = oracledb.connect(user = "RM561226", password = "110505", dsn = "oracle.fiap.com.br:1521/ORCL" )

    inst_gerar = conn.cursor()
    inst_excluir = conn.cursor()
    inst_modificar = conn.cursor()
    inst_mostrar = conn.cursor()
    
except Exception as e:
    print("Erro no banco de dados", e)
    conexao = False

else:
    conexao = True