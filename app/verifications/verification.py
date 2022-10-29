class CheckData:
    def validarNome(self='', name='', lastname=''):
        """
        > Função que verifica os caracteres dos parametros.
        :param name primeiro nome
        :param lastname: utlimo nome
        :return: True ou False e nome e sobrenome, menssagem
        """

        name = name.strip().replace(" ", '')
        lastname = lastname.strip().replace(" ", '')

        if name.isalpha() and lastname.isalpha():
            return True, name, lastname, '<h1>Nome e Sobrenome são dados Válidos</h1>'
        else:
            print("Erro Nome/Sobrenome:\nOBS:Preencha todos os campos;\nCampos Nome e Sobrenome não aceitam caracteres numéricos ou especiais.")
        return False, name, lastname, "<h1>Erro Nome/Sobrenome:</h1><h3><br>OBS:<br>Preencha todos os campos;" \
                                      "<br>Campos Nome e Sobrenome não aceitam caracteres numéricos ou especiais.</h3>"


    def validarPassoword(self='', passsoword=''):
        """
        Função que valida senha e nome de usuário para cadastro
        :param username: nome de usuário
        :param passsoword: senha
        :return: False or True e menssagem
        """
        from app.banco import banco
        if(passsoword == '' or len(passsoword) < 8):
            print("Os campos não podem ficar vazios\n"
                  "Senha deve ter no mínimo 8 caracteres")
            return False, "<h1>Erro Passoword:</h1><h2>campo Senha não pode ficar vazios<br>Senha deve ter no mínimo 8 caracteres</h2>"
        else:
            return True, "<h1>Semha Válida</h1>"
