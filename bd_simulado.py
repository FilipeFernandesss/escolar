
#Grade dos professores
grade_professores = {"professor123": [["Teoria da Computação", "Turma B", "23", "Ciência da Computação"], ["Lab. Programação", "Turma a", "21", "Ciência da Computação"], ["Sistemas de Informações", "Turma B", "23", "Ciência da Computação"]],
                     "professor1": [["Banco de Dados", "Turma a", "23", "Ciência da Computação"], ["Matemática Discreta", "Turma a", "21", "Ciência da Computação"], ["Lab. Programação", "Turma B", "20", "Ciência da Computação"]],
                     "professor2":[["Anatomia", "Turma a", "35", "Educação Física"], ["Anatomia", "Turma a", "29", "Enfermagem"], ["Anatomia", "Turma a", "29", "Medicina"]]}

#Dados dos funcionarios
info_funcionarios = {"funcionario123":["Asa Norte", "Auxiliar Administrativo", 1500],
                     "funcionario1":["Taguatinga", "Diretor", 3000],
                     "funcionario2":["Taguatinga", "Bibliotecário", 2500]}



def get_grade(login):
    return grade_professores[login]


def get_info_professores(login, disciplina):
    lista = []
    for disci in grade_professores[login]:
        if disci[0] == disciplina:
            lista.append(disci)

    return lista


def get_funcionarios(login):
    return info_funcionarios[login]

