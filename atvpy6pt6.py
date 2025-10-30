# LUCAS DA SILVA LIMA RM562118
# RIQUELME NASCIMENTO DE OLIVEIRA RM565468
# GUILHERME BARRETO RAMOS RM561226
 
import os
import oracledb
import pandas as pd
 
# Conexão do Banco
try:
    conn = oracledb.connect(user="RM561226", password="110505", dsn="oracle.fiap.com.br:1521/ORCL")
 
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
 
except Exception as e:
    conexao = False
else:
    conexao = True
 
 
# Limpar Tela
def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")
 
 
# Exibir Menu
def menu() -> None:
    print("=========== MENU ===========")
    print("""
    0 - Sair
    1 - Cadastrar Livro
    2 - Pesquisar Livro
    3 - Listar Registros de Livro
    4 - Editar Registro do Livro
    5 - Apagar Registro do Livro
    """)
 
 
# Cadastrar Livro
def cadastrar_livro() -> None:
    limpar_tela()
    print("----- CADASTRAR LIVRO -----")
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        numero_pag = int(input("Número de páginas: "))
        preco = float(input("Preço: "))
        dataPublicacao = input("Data de publicação (DD/MM/YYYY): ")
 
        cadastro = f""" INSERT INTO cppy_publi_livro (titulo, autor, numero_pag, preco, data_publi)
                        VALUES('{titulo}', '{autor}', {numero_pag}, {preco}, TO_DATE('{dataPublicacao}', 'DD/MM/YYYY')) """
 
        inst_cadastro.execute(cadastro)
        conn.commit()
    except ValueError:
        print("Digite um número no espaço correto!")
    except Exception as e:
        print("Erro ao gravar no banco:", e)
    else:
        print("Livro cadastrado!")
 
 
# Pesquisar livro por nome
def pesquisar_nome() -> None:
    limpar_tela()
    print("----------PESQUISA POR NOME----------")
    nome = input("Digite parte ou o nome completo do livro: ").strip()
 
    try:
        consulta = f""" SELECT * FROM cppy_publi_livro
                        WHERE LOWER(titulo) LIKE LOWER('%{nome}%')
                        ORDER BY id_livro
                        """
        inst_consulta.execute(consulta)
        data = inst_consulta.fetchall()
 
        if not data:
            print("Nenhum livro encontrado com esse nome!")
        else:
            dados_df = pd.DataFrame.from_records(data,
                                                 columns=['ID', 'Título', 'Autor', 'Paginas', 'Preco',
                                                          'Data_publicacao'],
                                                 index='ID')
            print(dados_df)
    except Exception as e:
        print("Erro ao pesquisar livro!", e)
 
 
# Listar Livros
def listar_livros() -> pd.DataFrame:
    limpar_tela()
    lista_dados = []
 
    inst_consulta.execute("SELECT * FROM cppy_publi_livro ORDER BY id_livro")
    data = inst_consulta.fetchall()
 
    for dt in data:
        lista_dados.append(dt)
 
    dados_df = pd.DataFrame.from_records(
        lista_dados,
        columns=['ID', 'Título', 'Autor', 'Páginas', 'Preço', 'Data Publicação'],
        index='ID'
    )
 
    return dados_df
 
 
# Alterar livro
def alterar_livro() -> None:
    limpar_tela()
    print("----- ALTERAR LIVRO -----")
    try:
        livro_id = int(input("Digite o ID do livro a alterar: "))
 
        consulta = f"SELECT * FROM cppy_publi_livro WHERE id_livro = {livro_id}"
        inst_consulta.execute(consulta)
        data = inst_consulta.fetchall()
 
        if not data:
            print(f"Nenhum livro com ID {livro_id}.")
        else:
            livro_atual = data[0]
            novo_titulo = livro_atual[1]
            novo_autor = livro_atual[2]
            nova_pag = livro_atual[3]
            novo_preco = livro_atual[4]
 
            alterar_titulo = input(f"Novo título ou aperte Enter para manter: ")
            if alterar_titulo != "":
                novo_titulo = alterar_titulo
 
            alterar_autor = input(f"Novo autor ou aperte Enter para manter: ")
            if alterar_autor != "":
                novo_autor = alterar_autor
 
            alterar_pag = input(f"Novo número de páginas ou aperte Enter para manter: ")
            if alterar_pag != "":
                nova_pag = int(alterar_pag)
 
            alterar_preco = input(f"Novo preço ou aperte Enter para manter: ")
            if alterar_preco != "":
                novo_preco = float(alterar_preco)
 
            alteracao = f"""
                UPDATE cppy_publi_livro
                SET titulo='{novo_titulo}', autor='{novo_autor}', numero_pag={nova_pag}, preco={novo_preco}
                WHERE id_livro={livro_id}
            """
            inst_alteracao.execute(alteracao)
            conn.commit()
            print("Livro atualizado com sucesso!")
 
    except ValueError:
        print("Digite valores numéricos válidos!")
    except Exception as e:
        print("Erro ao atualizar:", e)
 
 
# Deletar Livro
def excluir_livro() -> None:
    limpar_tela()
    print("----- EXCLUIR LIVRO -----")
    try:
        livro_id = int(input("Digite o ID do livro para excluir: "))
        consulta = f"SELECT * FROM cppy_publi_livro WHERE id_livro = {livro_id}"
        inst_consulta.execute(consulta)
        data = inst_consulta.fetchall()
 
        if not data:
            print(f"Nenhum livro com ID {livro_id}.")
        else:
            confirma = input("Confirma exclusão? [S/N]: ")
            if confirma.upper() == "S":
                exclusao = f"DELETE FROM cppy_publi_livro WHERE id_livro={livro_id}"
                inst_exclusao.execute(exclusao)
                conn.commit()
                print("Livro excluído!")
            else:
                print("Operação cancelada.")
    except ValueError:
        print("Digite um número válido para o ID!")
    except Exception as e:
        print("Erro ao excluir:", e)
 
 
# Mostrar data
def mostrar_df(data) -> None:
    if not data:
        print("Nenhum registro encontrado!")
    else:
        df = pd.DataFrame.from_records(
            data,
            columns=['ID', 'Título', 'Autor', 'Páginas', 'Preço', 'Data Publicação'],
            index='ID'
        )
        print(df)
 
 
# Gerar arquivo
def gerar_arquivo(df) -> None:
    import os
 
    print("\nGerar arquivo [E]xcel, [C]SV? Ou [ENTER] para voltar ao menu:")
    opcao = input("Escolha: ").strip().lower()
 
    if opcao == "e":
 
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()
        if nome_arquivo:
            caminho = f"{nome_arquivo}.xlsx"
            df.to_excel(caminho, index=False, engine="openpyxl")
            print(f"\n Arquivo Excel '{caminho}' gerado com sucesso!")
        else:
            print("Nome inválido. Arquivo não gerado.")
 
    elif opcao == "c":
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()
        if nome_arquivo:
            caminho = f"{nome_arquivo}.csv"
            df_form = df.copy()  
            with open(caminho, "w", encoding="utf-8-sig") as f:
                f.write("; ".join(map(str, df_form.columns)) + "\n")
                for _, row in df_form.iterrows():
                    linha = "; ".join(map(str, row.values)) + "\n"
                    f.write(linha)
            print(f"\nArquivo CSV '{caminho}' gerado com sucesso!")
            print(f"Caminho completo: {os.path.abspath(caminho)}")
        else:
            print("Nome inválido. Arquivo não gerado.")
    else:
        print("Voltando ao menu...")
 
 
# Escolher coluna
def selecionar_campos(df: pd.DataFrame) -> pd.DataFrame:
    print("\nColunas disponíveis para exibição (separe por vírgula (2,3) ou ENTER para todas):")
    for i, col in enumerate(df.columns, start=1):
        print(f"{i} - {col}")
 
    entrada = input("Escolhas: ").strip()
 
    if entrada == "":
        return df
 
    entrada_norm = entrada.replace(",", " ")
    tokens = [t for t in entrada_norm.split(" ") if t]
 
    idx_validos = []
    for t in tokens:
        try:
            idx = int(t)
            if 1 <= idx <= len(df.columns):
                idx_validos.append(idx)
            else:
                print(f"Ignorado índice fora do intervalo: {t}")
        except ValueError:
            print(f"Ignorado valor inválido: {t}")
 
    cols_escolhidas = []
    for i in idx_validos:
        col = df.columns[i - 1]
        if col not in cols_escolhidas:
            cols_escolhidas.append(col)
 
 
    if not cols_escolhidas:
        print("Nenhuma seleção válida. Exibindo todas as colunas.")
        return df
    return df[cols_escolhidas]  
 
# Listar os registros
def listar_registros() -> None:
    limpar_tela()
    print("----- LISTAR REGISTROS DE LIVRO -----")
    print("""                              
    a - Todos
    b - Pesquisar por parte da String e listar
    c - Pesquisar por um campo numérico e listar
    d - Pesquisa genérica
    """)
    sub = input("Escolha (a/b/c/d): ").strip().lower()
 
    if sub == "a":
        print("----- TODOS OS LIVROS -----")
        df = listar_livros()
        # [ALTERADO] Permitir ao usuário escolher quais campos exibir
        df = selecionar_campos(df)  # [ALTERADO]
        print(df)  # [ALTERADO]
        if not df.empty:
            gerar_arquivo(df)  # [ALTERADO] Exporta somente as colunas escolhidas
    else:
        if sub == "b":
            print("\nCampo de texto para pesquisar:")
            print("1 - Título\n2 - Autor")
            esc = input("Escolha (1/2): ").strip()
 
            if esc == "1":
                campo = "titulo"
            elif esc == "2":
                campo = "autor"
            else:
                print("Opção inválida.")
                return
 
            termo = input("Digite parte do texto para busca: ").strip()
 
            consulta = f"""SELECT * FROM cppy_publi_livro              
                            WHERE LOWER({campo}) LIKE LOWER('%{termo}%')
                            ORDER BY id_livro"""
            try:
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
                # [ALTERADO] Montar DataFrame com TODOS os campos
                df = pd.DataFrame.from_records(  # [ALTERADO]
                    data,  # [ALTERADO]
                    columns=['ID', 'Título', 'Autor', 'Páginas', 'Preço', 'Data Publicação'],  # [ALTERADO]
                    index='ID'  # [ALTERADO]
                )  # [ALTERADO]
                if df.empty:  # [ALTERADO]
                    print("Nenhum registro encontrado!")  # [ALTERADO]
                else:
                    # [ALTERADO] Permitir escolher as colunas a exibir
                    df = selecionar_campos(df)  # [ALTERADO]
                    print(df)  # [ALTERADO]
                # (mantido sem exportação aqui, como no original)  # [ALTERADO]
            except Exception as e:
                print("Erro na pesquisa por string:", e)
 
        elif sub == "c":
            print("\nCampo numérico para filtrar:")
            print("1 - ID do Livro\n2 - Número de Páginas\n3 - Preço")
            esc = input("Escolha (1/2/3): ").strip()
 
            if esc == "1":
                campo = "id_livro"
                tipo = "int"
            elif esc == "2":
                campo = "numero_pag"
                tipo = "int"
            elif esc == "3":
                campo = "preco"
                tipo = "float"
            else:
                print("Opção inválida.")
                return
 
            print("\nOperador (>, >=, <, <=, ==, !=):")
            operador = input("Digite o operador: ").strip()
 
            if operador == "==":
                operador_sql = "="
            elif operador == "!=":
                operador_sql = "<>"
            elif operador in [">", ">=", "<", "<="]:
                operador_sql = operador
            else:
                print("Operador inválido.")
                return
 
            try:
                if tipo == "int":
                    valor = int(input("Valor (inteiro): ").strip())
                else:
                    valor = float(input("Valor (decimal): ").strip().replace(",", "."))
            except ValueError:
                print("Valor numérico inválido.")
                return
 
            consulta = f"""SELECT * FROM cppy_publi_livro            
                            WHERE {campo} {operador_sql} {valor}
                            ORDER BY id_livro"""
            try:
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
                # [ALTERADO] Montar DataFrame com TODOS os campos
                df = pd.DataFrame.from_records(  # [ALTERADO]
                    data,  # [ALTERADO]
                    columns=['ID', 'Título', 'Autor', 'Páginas', 'Preço', 'Data Publicação'],  # [ALTERADO]
                    index='ID'  # [ALTERADO]
                )  # [ALTERADO]
                if df.empty:  # [ALTERADO]
                    print("Nenhum registro encontrado!")  # [ALTERADO]
                else:
                    # [ALTERADO] Permitir escolher as colunas a exibir
                    df = selecionar_campos(df)  # [ALTERADO]
                    print(df)  # [ALTERADO]
                # (mantido sem exportação aqui, como no original)  # [ALTERADO]
            except Exception as e:
                print("Erro na pesquisa numérica:", e)
 
        elif sub == "d":
            print("\n----- PESQUISA GENÉRICA -----")
            termo = input("Digite parte do texto para buscar em vários campos: ").strip()
 
            consulta = f"""
                SELECT * FROM cppy_publi_livro
                WHERE LOWER(titulo) LIKE LOWER('%{termo}%')
                   OR LOWER(autor)  LIKE LOWER('%{termo}%')
                   OR TO_CHAR(data_publi, 'DD/MM/YYYY') LIKE '%{termo}%'
                   OR TO_CHAR(preco) LIKE '%{termo}%'
                ORDER BY id_livro
            """
 
            try:
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
 
                if not data:
                    print("Nenhum registro encontrado para o termo informado!")  
                else:
                    df = pd.DataFrame.from_records(
                        data,
                        columns=['ID', 'Título', 'Autor', 'Páginas', 'Preço', 'Data Publicação'],
                        index='ID'
                    )
                    # [ALTERADO] Permitir escolher as colunas a exibir
                    df = selecionar_campos(df)  # [ALTERADO]
                    print(df)  # [ALTERADO]
                    gerar_arquivo(df)  # [ALTERADO] Exporta somente as colunas escolhidas
            except Exception as e:
                print("Erro na pesquisa genérica:", e)
 
        else:
            print("Opção inválida.")
 
 
# Repetição
while conexao:
    limpar_tela()
    menu()
    opcao = input("Escolha uma opção: ")
 
    match opcao:
        case "0":
            conexao = False
            print("Saindo do programa...")
        case "1":
            cadastrar_livro()
        case "2":
            pesquisar_nome()
        case "3":
            listar_registros()
        case "4":
            alterar_livro()
        case "5":
            excluir_livro()
        case _:
            print("Opção inválida. Tente novamente.")
 
    if conexao:
        input("\nPressione ENTER para continuar...")