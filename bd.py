#Função validar login
def get_idlogin(cursor, login, senha):
    #executar o sql
    cursor.execute(f'select id_login from login where login = "{login}" and senha = "{senha}";')

    #recuperando o retorno do BD
    idlogin = cursor.fetchone()

    #fechar o cursor
    cursor.close()
    if idlogin is None:
        return None
    else:
        return idlogin[0]

    #verificar o retorno o idLogin

#função para retornar as disciplinas
def get_notas(cursor, idlogin):
    #Executar o sql

    cursor.execute(f'select disciplina, nota1, nota2, nota3 from notas where id_login = "{idlogin}";')

    #Recuperando o retorno do BD
    disciplinas = cursor.fetchall()


    #Fechando o cursor
    cursor.close()

    #Retornando as disciplinas
    return disciplinas

'''def validar_login_prof(cursor, login,  senha):
    cursor.execute(f'select idlogin from login_prof where login = "{login}" and senha = "{senha}";')
    # recuperando o retorno do BD
    idlogin = cursor.fetchone()
    #print(idlogin[1]) O RETORNO É UMA TUPLA E POSSO RECUPERAR O BANCO DE DADOS PELAS POSIÇÕES

    # fechar o cursor
    #cursor.close()

    if idlogin is None:
        return False
    else:
        return True

def validar_login_func(cursor, login,  senha):
    cursor.execute(f'select idlogin from login_func where login = "{login}" and senha = "{senha}";')
    # recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # fechar o cursor
    cursor.close()

    if idlogin is None:
        return False
    else:
        return True'''
