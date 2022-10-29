from verifications.verification import CheckData
import sqlite3
import banco.banco
id = '9'

try:
    dados = banco.banco.buscarUsuarioId(id)
    con = sqlite3.connect('banco\streaminghorse_fastapi.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM cliente where ID = {id}")
    if dados == f"<h1>id: '{id}' não existe</h1>":
        print(dados)
    else:
        print( f"Cliente:{dados}Excluidos com Sucesso")
    # salvar a conexão
    con.commit()
except sqlite3.Error as error:
    print(f"Falha na execução da query\n{error}")
con.close()