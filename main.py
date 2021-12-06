"""
Tema: Controle de avaliações
Amanda Luiza Silva - BP3018598
Carlos Henrique Hermínio de Oliveira - BP301875X
Gustavo Costa Coelho - BP3018318
Iohara Pereira Bento Ferreira - BP3018881
"""



import sqlite3
from sqlite3 import Error
import colorama
from colorama import Fore
from os import system
from time import sleep
import schema
from tables import Professor as p
from tables import Aluno as a
from tables import limpar
import menus as m

colorama.init(autoreset='True')
BOLD = '\033[1m'

def conectar_bd(bd):
  print (Fore.LIGHTBLUE_EX + "Conectando ao banco de dados...")
  try:
    conexao = sqlite3.connect(bd)
    sleep(1)
    print(Fore.GREEN + 'Conexão bem sucedida')
    return conexao
  except Error as e: 
    print(e)


def tipoUsuario():
  print(25 * '-')
  print(Fore.GREEN + "---- MENU ----")
  print(25 * '-')
  print(Fore.BLUE + "0. Sair")
  print(Fore.BLUE + "1. Professor")
  print(Fore.BLUE + "2. Aluno ")
  print(25 * '-')
  try:
    tipo = int(input('Selecione seu tipo de usuário: '))
    if tipo < 0 or tipo > 2:
      print(Fore.RED + 'Opção inválida')
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")
    else: return tipo
  except: 
    print(BOLD + Fore.RED + 'Por favor, insira apenas números')
    input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")

def tableProf(opFun):
  if opFun == 1: # Opção para mexer apenas nas avaliações
    limpar()
    tabela = 'Avaliacoes'

    while True:
      op = m.menuAv()
      if op == 0: break
      elif op == 1: p.novaAvaliacao(tabela, con)
      elif op == 2: p.pesquisarAvaliacao(tabela, con)
      elif op == 3: p.atualizarAvaliacao(tabela, con)
      elif op == 4: p.excluirAvaliacao(tabela, con)
      elif op == 5: p.pesquisarMax(tabela, con)
      elif op == 6: p.pesquisarMin(tabela, con)
      limpar()    
        
  elif opFun == 2: # Opção para mexer apenas nos tipos de avaliação
    limpar()
    tabela = 'tipoAvaliacao'

    while True:
      op = m.menuTipo()
      if op == 0: break
      elif op == 1: p.novoTipo(tabela, con)
      elif op == 2: p.pesquisarTipo(tabela, con)
      elif op == 3: p.atualizarTipo(tabela, con)
      elif op == 4: p.excluirTipo(tabela, con)
      limpar()
        
  elif opFun == 3: # opção para mexer nos boletins dos alunos
    limpar()
    tabela = 'boletim'

    while True:
      op = m.menuBoletim()
      if op == 0: break
      elif op == 1: p.cadastraBoletim(tabela, con)
      elif op == 2: a.pesquisarDescricao(tabela, con)
      elif op == 3: p.atualizarBoletim(tabela, con)
      elif op == 4: p.excluirBoletim(tabela, con)
      limpar()
  else: print('Opção inválida')

  limpar()
  print(BOLD + Fore.LIGHTCYAN_EX + 'Voltando para as outras opções')
  sleep(1)
  limpar()

if __name__ == '__main__':
  limpar()
  banco = input('Informe o nome do banco de dados: ').lower()
  schema.criar_tabela(banco)
  con = conectar_bd(banco)
  while True:
    sleep(0.5)
    limpar()
    user = tipoUsuario()

    if user == 0: break
    #Usuário definido como professor
    elif user == 1:
      limpar()
      sleep(1)
      print(BOLD + Fore.CYAN +'Seja bem vindo professor')
      opFun = m.menuProf()
      while opFun != 0:
        tableProf(opFun)
        opFun = m.menuProf()

    #Usuário definido como aluno
    elif user == 2: 
      limpar()
      sleep(1)
      print(BOLD + Fore.CYAN +'Seja bem vindo')
      tabela = 'boletim'
      op = m.Aluno()
      while op != 0:
        if op == 1:
          print('Pesquisar avaliação')
          a.pesquisarBoletim(tabela, con)
        elif op == 2:
          print('Ver boletim')
          a.pesquisarDescricao(tabela, con)
        elif op == 3:
          print('Ver boletim')
          a.pesquisarData(tabela, con)
        else: print('Opção inválida')
        limpar()
        op = m.Aluno()
                  
  print('Obrigado por usar o sistema')
  
  print('Saindo do sistema...')
  sleep(1)
  limpar()
