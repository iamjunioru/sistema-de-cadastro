from os import path
from sqlite3 import dbapi2

def criarTabelas():

    tb_alunos = '''
            CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY, 
            nome VARCHAR(30) not null,
            nascimento VARCHAR(5) not null,
            sexo VARCHAR(1) not null
            );''' 

    tb_turmas = '''
            CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY,
                codigo_turma VARCHAR(5) NOT NULL UNIQUE,
                nome_turma VARCHAR(50) NOT NULL
            );''' 
    tb_matriculas = '''
        CREATE TABLE IF NOT EXISTS matriculas(
            cod_matricula INTEGER PRIMARY KEY,
            id_aluno INTEGER NOT NULL REFERENCES alunos(id),
            id_turma INTEGER NOT NULL REFERENCES turmas(id),    
            ano INTEGER NOT NULL,
            periodo TEXT NOT NULL
        );'''

    db_file = path.join(path.dirname(path.abspath(__file__)), 'db3_alunos.db')
    print('▶▶▶ Iniciando Banco de Dados')
    cx = dbapi2.connect(db_file)
    print('▶▶▶ Iniciando o cursor')
    cursor = cx.cursor()
    print('▶▶▶ Iniciando a tabela do banco de dados')
    cursor.execute(tb_alunos)
    cursor.execute(tb_turmas)
    cursor.execute(tb_matriculas)
    cx.commit()
    cursor.close()
    cx.close()

criarTabelas()