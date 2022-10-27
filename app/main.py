# TODO: Loja de streaming tipo, NETFLIX, HBO etc.
# TODO: Quando o usuário acessar o programa deverá haver opção de cadastro e de acesso, login, logon
# TODO: Coletar dados de cadastro de usuários (caso não haja)
# TODO: Coletar nome completo, separar para as varáveis: nome, sobrenome
# TODO: Caso usuário já exista, mostra um menu com opções de filmes para assistir
# TODO: Criar opção de logout
# TODO: Coletar idade
# TODO: Coletar CPF: ATENÇÃO, não coloque seus dados originais
# TODO: Na coleta do CPF, deverá ser aceito somente números: 1203120398
# TODO: Coletar CEP, e apartir do cep preencher o restante dos dados, rua e cidade
# TODO: Perguntar se dados do CEP estão corretos
# TODO: Coletar número da casa

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
@app.get('/registro/{Nome}-{Sobrenome}{Passoword}', response_class= HTMLResponse, status_code= 201)
async def coletarDados(Nome: str, Sobrenome: str, Passoword:str):
    """
    Função que coleta os dados e verifica apartir de outras funçoes
    """
    #Recebendo nome
    # while True:
    #     print(f"{'Cadastro':-^30}")
    #     nome = Nome
    #     sobrenome = input("Sobrenome:").strip()
    #     if CheckData.validarNome(name=nome, lastname=sobrenome):
    #         break
    #
    # #Recebendo data de nascimento
    # while True:
    #
    #     if CheckData.validarIdade(day=dia, month=mes, year=ano):
    #         dataNascimento = date(day=int(dia), month=int(mes), year=int(ano))
    #         break
    #
    #
    # #Recebendo CPF
    # while True:
    #     cpf = input("CPF: ").strip()
    #     condicao = CheckData.validarCPF(cpf=cpf)
    #     if condicao:
    #         break
    #
    # #Recebendo CEP
    # while True:
    #     cep = input("CEP: ").strip()
    #     verificacao, endereco = CheckData.validarCEP(cep=cep)
    #     if verificacao:
    #         break
    #     else:
    #         print(endereco)
    #
    # #Recebendo email e senha
    # while True:
    #     username = input("Username: ").strip()
    #     passoword = str(sha256(input("Passoword: ").strip().encode('utf-8')).hexdigest())
    #     if CheckData.validarCredenciais(username=username, passsoword=passoword):
    #         break
    banco.verificarBD()
    #Cadastro
    user = {
        "nome": Nome,
        "sobrenome": Sobrenome,
        # "data_nascimento": dataNascimento,
        # "cpf": Cpf,
        # 'logradouro': endereco['logradouro'],
        # 'bairro': endereco['bairro'],
        # 'localidade': endereco['localidade'],
        # "numero": endereco['numero'],
        # "username": username,
        "passoword": Passoword
            }
    banco.cadastrar(user)
#----------------------------------

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)

