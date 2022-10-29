#bibliotecas
    #arquivos do programa
from verifications.verification import CheckData
from banco import banco
#Fast-API
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
#server
import uvicorn
    #outros
from datetime import date
import re
from hashlib import sha256


app = FastAPI()

#-{dia}-{mes}-{ano} -{cep}-{username}{senha}
@app.get('/registrar/{Nome}-{Sobrenome}-{Passoword}', response_class= HTMLResponse, status_code= 200)
async def coletarDados(Nome: str, Sobrenome: str, Passoword:str):
    """
    Função que coleta os dados e verifica apartir de outras funçoes
    """
    condicaoNomeSobrenome, Nome, Sobrenome, messageNomeSobrenome = CheckData.validarNome(name=Nome, lastname=Sobrenome)

    condicaoPassoword , messagePassoword = CheckData.validarPassoword(passsoword=Passoword)

    if condicaoNomeSobrenome and condicaoPassoword:
        banco.verificarBD()
        #Cadastro
        user = {
            "nome": Nome,
            "sobrenome": Sobrenome,
            "passoword": Passoword
                }
        return banco.cadastrar(user)
    else:
        return f"{messageNomeSobrenome}{messagePassoword}"


@app.get('/consultar', response_class=HTMLResponse, status_code=200)
async def Consultar():
    return banco.consultandoTodosClientes()


@app.get('/consultar/{id_usuario}', response_class = HTMLResponse, status_code = 200)
async def consultarID(id_usuario: str):
    if id_usuario.isnumeric():
        return banco.buscarUsuarioId(id=id_usuario)
    else:
        return f"<h1>id: '{id_usuario}' não existe</h1>"

@app.get('/deletar/{id_usuario}', response_class = HTMLResponse, status_code = 200)
async def deletarId(id_usuario: str):
    if id_usuario.isnumeric():
        print(id_usuario)
        return banco.deletarUsuario(id=id_usuario)
    else:
        return f"<h1>id: '{id_usuario}' não existe</h1>"


#----------------------------------

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)

