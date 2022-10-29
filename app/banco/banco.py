import sqlite3


def verificarBD():
    """
    Função que cria o banco de dados caso não exista
    :return: sem retorno
    """
    import os
    arquivo = 'banco\streaminghorse_fastapi.db'
    if os.path.exists(arquivo):
        print("Carregando Banco de dados")
    else:
        con = sqlite3.connect('banco\streaminghorse_fastapi.db')
        cur = con.cursor()
        try:
            cur.execute('CREATE TABLE cliente ('
                        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'nome TEXT, '
                        'sobrenome TEXT, '
                        'passoword TEXT);')
        except:
            pass

            # salvar a conexão
            con.commit()
            print("Banco criado com sucesso!!!")

            # fechando a conexão
            con.close()


def cadastrar(dados_user=''):
    """
    > Função que cadastra usuário no banco dedados
    :param dados_user: Dicionário com dados do cliente
    """
    con = sqlite3.connect('banco\streaminghorse_fastapi.db')
    cur = con.cursor()

    #inserindo valores

    cur.execute('INSERT INTO cliente ('
                'nome, '
                'sobrenome, '
                'passoword) '
                'VALUES (?,?,?)',   (
                                            dados_user['nome'],
                                            dados_user['sobrenome'],
                                            dados_user['passoword']
                                    )
                )
    # salvar a conexão
    con.commit()


    # fechando a conexão
    con.close()
    return "<h1>Cadastrado com sucesso!!!</h1>"


def consultandoTodosClientes():
    try:
        con = sqlite3.connect('banco\streaminghorse_fastapi.db')
        cur = con.cursor()

        cur.execute(f"SELECT id, nome, sobrenome FROM cliente")
        resultado = cur.fetchall()
        if resultado == []:
            return f"<h1>não há nenhum cadastro existe</h1>"
        else:
            return f"<h2>ID, NOME, SOBRENOME<br>{resultado}</h2>".replace('), (', '<br>').replace('[(', '').replace(')]', '')
    except sqlite3.Error as error:
        print(f"Falha na execução da query\n{error}")
    con.close()


def buscarUsuarioId(id):

    try:
        con = sqlite3.connect('banco\streaminghorse_fastapi.db')
        cur = con.cursor()

        cur.execute(f"SELECT id, nome, sobrenome FROM cliente WHERE id = {id}")
        resultado = cur.fetchall()
        con.close()
        if resultado == []:
            return f"id: '{id}' não existe"
        else:
            return f"ID: {resultado[0][0]}<br>Nome: {resultado[0][1]}<br>Sobrenome: {resultado[0][2]}"
    except sqlite3.Error as error:
        print(f"Falha na execução da query\n{error}")
        con.close()


def deletarUsuario(id=''):
    try:
        dados = buscarUsuarioId(id)
        con = sqlite3.connect('banco\streaminghorse_fastapi.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM cliente where ID = '{id}'")
        con.commit()
        con.close()
        if dados == f"<h1>id: '{id}' não existe</h1>":
            return dados
        else:
            return f"Cliente:<br>{dados}<br>Excluidos com Sucesso"
        # salvar a conexão

    except sqlite3.Error as error:
        print(f"Falha na execução da query\n{error}")
        con.close()