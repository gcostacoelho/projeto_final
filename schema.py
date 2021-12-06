import sqlite3
from sqlite3 import Error

def criar_tabela(bd):
    con = sqlite3.connect(bd)
    c = con.cursor()

    try:
        c.execute("""
            CREATE TABLE IF NOT EXISTS tipoDeUsuario(
                siglaU    TEXT primary key,
                descricao TEXT NOT NULL
            );
        """)
            
        c.execute(""" 
            CREATE TABLE IF NOT EXISTS usuario (
                nome  TEXT primary key,
                idade INTEGER NOT NULL,
                sigla TEXT NOT NULL
            );
        """)
            
        c.execute("""
            CREATE TABLE IF NOT EXISTS tipoAvaliacao(
                tipo TEXT primary key,
                descricao TEXT NOT NULL
            );
        """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS Avaliacoes(
                idAvaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
                siglaA    TEXT NOT NULL,
                descricao TEXT NOT NULL,
                professor TEXT NOT NULL,
                dataInicio DATE NOT NULL,
                dataPrev   DATE NOT NULL,
                notaAprov DECIMAL(2,1) NOT NULL,
                notaMax   DECIMAL(2,1) NOT NULL,
                notaMin   DECIMAL(2,1) NOT NULL
            );
        """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS boletim(
                idAluno INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno TEXT NOT NULL,
                avaliacao TEXT NOT NULL,
                dataConcl DATE NOT NULL,
                notAtrib Decimal(2,1),
                situacao TEXT NOT NULL
            );
        """)
    except Error as e:
        print(e)