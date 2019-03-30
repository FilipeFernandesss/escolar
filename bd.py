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
        print(idlogin)
        print(idlogin[0])
        return idlogin[0]

    #verificar o retorno o idLogin

#função para retornar as disciplinas
def get_notas(cursor, idlogin):
    #Executar o sql

    cursor.execute(f"""SELECT    D.id_disciplina,D.nome,nota1, nota2, nota3
from disciplinas D, notas N, login
where N.id_login = "{idlogin}" and N.id_disciplina = D.id_disciplina and N.id_login = login.id_login;""")

    #Recuperando o retorno do BD
    disciplinas = cursor.fetchall()


    #Fechando o cursor
    cursor.close()

    #Retornando as disciplinas
    return disciplinas

#Funcao para retornar a descrição de uma disciplina

def get_descricao(cursor,id_disciplina):
    #Executar o sql
    cursor.execute(f"""SELECT descricao, nome
from disciplinas
where id_disciplina = "{id_disciplina}";""")

    descricao = cursor.fetchall()
    cursor.close()
    print(descricao)

    return descricao







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
