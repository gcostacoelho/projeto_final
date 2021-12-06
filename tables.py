import sqlite3
from sqlite3 import Error
import colorama
from colorama import Fore
from os import system
from time import sleep

colorama.init(autoreset='True')
BOLD = '\033[1m'

def limpar():
    import os
    def limpar():
        if os.name == 'posix': _ = os.system('clear')
        else: _ = os.system('cls')
    sleep(1)
    limpar()

class Professor:
#opcao 1
  def novaAvaliacao(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'Avaliacoes':
        professor = None
        try:
          while True:
            siglaA = input("Informe a sigla: ").lower()
            if siglaA == '':
              print('insira algo na sigla.')
            else: break
          while True:
            descricao = input("Informe a descricao: ").lower()
            if descricao == '':
              print('insira algo na descricao.')
            else: break
          while True:
            professor = input("Informe o nome do professor:").lower()
            if professor == '':
              print('insira algo na professor.')
            else: break
          while True:
            dataInicio = input("Informe a data de início (AAAA-MM-DD):").lower()
            if dataInicio == '':
              print('insira algo na data de inicio.')
            else: break
          while True:
            dataPrev = input("Informe a data de término (AAAA-MM-DD):").lower()
            if dataPrev == '':
              print('insira algo na data de término.')
            else: break
          while True:
            notaAprov= float(input("Informe a nota de aprovação: "))
            if notaAprov < 0 or notaAprov > 10 or notaAprov == '': print('Digite notas entre 0 e 10')
            else: break
          while True:
            notaMax= float(input("Informe a nota máxima: "))
            if notaMax < 0 or notaMax > 10 or notaMax == '': print('Digite notas entre 0 e 10')
            else: break
          while True:
            notaMin= float(input("Informe a nota mínima: "))
            if notaMin < 0 or notaMin > 10 or notaMin == '': print('Digite notas entre 0 e 10')
            else: break
        except Error as e:
          sleep(1)
          print('Algum campo foi preenchido Incorretamente.')
          sleep(2)
          limpar()
      
        avaliacao = (siglaA, descricao, professor, dataInicio, dataPrev, notaAprov, notaMax, notaMin)
        c.execute("INSERT INTO Avaliacoes (siglaA, descricao, professor, dataInicio, dataPrev, notaAprov, notaMax, notaMin) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", avaliacao)
        conexao.commit()
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.GREEN + f"Inserção com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")

  #opcao 2
  def novoTipo(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'tipoAvaliacao':
        while True:
          tipo = input("Informe a sigla do tipo de avaliação: ").lower()
          if tipo == '': print(Fore.LIGHTRED_EX + 'Insira o tipo de avaliação\n')
          else: break
        while True:
          descricao = input("Informe a descrição: ").lower()
          if descricao == '': print(Fore.LIGHTRED_EX + 'Insira a descrição da avaliação\n')
          else: break          
        tipoAvaliacao = (tipo, descricao,)
        c.execute("INSERT INTO tipoAvaliacao (tipo, descricao) VALUES(?, ?);", tipoAvaliacao)
        conexao.commit()
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else: 
      print(Fore.GREEN + f"Inserção com sucesso em {tabela}.")
      input(Fore.BLUE + "Pressione <ENTER> para continuar...")

  #opcao 3
  def pesquisarAvaliacao(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'Avaliacoes':
        c.execute(
          "SELECT * FROM avaliacoes;"
        )   
      resultado = c.fetchall()
      if resultado:
        print(Fore.BLUE + "{:<5} {:<7} {:<25} {:<15} {:<13} {:<13} {:<13} {:<10} {:<10}".format("ID", "Sigla", "Descrição", "Professor", "Dt Início", "Dt Fim", "Nota Aprov", "Nota max", "Nota min"))
        
        for item in range(len(resultado)):
          print(Fore.YELLOW + "{:<5} {:<7} {:<25} {:<15} {:<13} {:<13} {:<13} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5], resultado[item][6], resultado[item][7],resultado[item][8]))
      else:
        print(Fore.RED + "Não foram encontrados registros.")
        return False
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.GREEN + f"Pesquisa realizada com sucesso em {tabela}")
      input(BOLD + Fore.BLUE + f"Pressione <ENTER> para continuar ...")

  #opcao 4
  def pesquisarMax(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'Avaliacoes':
        c.execute("SELECT descricao, notaMax FROM Avaliacoes;")
      
      resultado = c.fetchall()
      if resultado:
        print(BOLD + Fore.LIGHTBLUE_EX + "{:<5} {:<50}".format("Descricao", "Nota Máxima"))
        for item in range(len(resultado)):
          print("{:<5} {:>10}".format(resultado[item][0], resultado[item][1]))
      else:
        print(BOLD + Fore.RED + "Não foram encontrados registros.")
        input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.LIGHTGREEN_EX + f"Pesquisa realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")

  #opcao 5
  def pesquisarMin(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'Avaliacoes':
        c.execute("SELECT descricao, notaMin FROM Avaliacoes;")
      
      resultado = c.fetchall()
      if resultado:
        print(BOLD + Fore.LIGHTBLUE_EX + "{:<5} {:<50}".format("Descricao", "Nota Mínima"))
        for item in range(len(resultado)):
          print("{:<5} {:>10}".format(resultado[item][0], resultado[item][1]))
      else:
        print(BOLD + Fore.RED + "Não foram encontrados registros.")
        input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.LIGHTGREEN_EX + f"Pesquisa realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")

  #opcao 6
  def pesquisarTipo(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'tipoAvaliacao':
        c.execute('SELECT * FROM tipoAvaliacao;')
        resultado = c.fetchall()
        if resultado:
          print(Fore.CYAN + BOLD + '{:<5} {:<50}'.format('Tipo', 'Descrição'))
          for item in range(len(resultado)):
            print(BOLD + '{:<5} {:<50}'.format(resultado[item][0], resultado[item][1]))
        else: 
          print(BOLD + Fore.RED + 'Não foram encontrados registros')
          return False
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.') 
    else:
      print(BOLD + Fore.GREEN + f'\nPesquisa realizada com sucesso em {tabela}')
      input(BOLD + Fore.BLUE + 'Pressione <ENTER> para continuar...' + Fore.RESET)
  
  #opcao 7
  def cadastraBoletim(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'boletim':
        aluno = input("Informe o nome do Aluno: ").lower()
        while aluno == '':
          sleep(1)
          print(Fore.RED + BOLD + '\nInforme um nome para aluno(a).')
          aluno = input("Informe o nome do Aluno: ").lower()
        avaliacao = input("Informe a descricao da avaliação: ").lower()
        while avaliacao == '':
          sleep(1)
          print(Fore.RED + BOLD + '\nInforme uma descrição para a avaliação')
          avaliacao = input("Informe a descricao da avaliação: ").lower()      
        try:
          while True:
            dataConcl = input("Informe a data de conclusão: (AAAA-MM-DD):").lower()
            if dataConcl == '': print('digite uma data de conclusão.')
            else: break       
          while True:
            notAtrib = float(input("Informe a nota do aluno:"))
            if notAtrib < 0 or notAtrib > 10: print(Fore.RED + 'Digite notas entre 0 e 10')
            else: break
          while True:
            situacao = input('Informe a situação do aluno (Aprovado ou Reprovado): ').lower()
            if (situacao == 'aprovado') or (situacao == 'reprovado'): break
            else: 
              sleep(1)
              print(Fore.RED + '\nInforme se o aluno foi aprovado ou reprovado\n')
        except: 
          print('Algum campo foi inserido incorretamente.')
        
        dados = (aluno, avaliacao, dataConcl, notAtrib, situacao)
        c.execute("INSERT INTO boletim (aluno, avaliacao, dataConcl, notAtrib, situacao) VALUES (?, ?, ?, ?, ?);", dados)
        conexao.commit()
    
    except:
      print('Algo está errado, tente novamente.')
      sleep(2)
    else:
      print(BOLD + Fore.GREEN + f"Inserção com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")

  #opcao 8
  def atualizarTipo(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'tipoAvaliacao':
        c = conexao.cursor()
        dado = Professor.pesquisarTipo(tabela, conexao)
        if dado != False:
          while True:
            tipo = input("Informe o tipo de avaliação a atualizar: ").lower()
            if tipo == '': print(Fore.LIGHTRED_EX + 'Insira o tipo de avaliação\n')
            else: break
          while True:
            descricao = input("Informe a descrição: ").lower()
            if descricao == '': print(Fore.LIGHTRED_EX + 'Insira a descrição da avaliação\n')
            else: break 
          tipoAvaliacao = (descricao,tipo)
          c.execute("UPDATE tipoAvaliacao SET descricao=? WHERE tipo=?;", tipoAvaliacao)
          conexao.commit()
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.') 
    else:
      print(BOLD + Fore.GREEN + f"Atualização realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + f"Pressione <ENTER> para continuar ...")

  #opcao 9
  def excluirTipo(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'tipoAvaliacao':
        dado = Professor.pesquisarTipo(tabela, conexao)
        if dado != False:
          while True:
            tipo = input("Informe o tipo da avaliação a excluir: ").lower()
            if tipo == '': print(Fore.RED + 'Insira o tipo de avaliação que você deseeja excluir')
            else: break
          tipoAvaliacao = (tipo,)
          c.execute("DELETE FROM tipoAvaliacao WHERE tipo=?;", tipoAvaliacao)	
          conexao.commit()
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.GREEN + f"Exclusão com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + f"Pressione <ENTER> para continuar ...")

  
  #opcao 10
  def atualizarAvaliacao(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'Avaliacoes':
        dado = Professor.pesquisarAvaliacao(tabela, conexao)
        if dado != False:
          while True:
            siglaA = input("Informe a sigla da avaliação a atualizar: ").lower()
            if siglaA == '':
              print(Fore.RED,'Digite algo em sigla.')
            else : break
          while True:
            descricao = input("Informe a descrição: ").lower()
            if descricao == '':
              print(Fore.RED,'Digite algo em descrição.')
            else : break
          while True:
            professor = input("Informe o nome do professor:").lower()
            if professor == '':
              print(Fore.RED,'Digite algo em professor.')
            else : break
          while True:
            dataInicio = input("Informe a data de início (AAAA-MM-DD):").lower()
            if dataInicio == '':
              print(Fore.RED,'Digite algo em data de inicio.')
            else : break
          while True:
            dataPrev = input("Informe a data de término (AAAA-MM-DD):").lower()
            if dataPrev == '':
              print(Fore.RED,'Digite algo em data de inicio.')
            else : break  
          avaliacao = (descricao,professor,dataInicio,dataPrev,siglaA)
          c.execute("UPDATE Avaliacoes SET descricao=?, professor=?, dataInicio=?, dataPrev=? WHERE siglaA=?;", avaliacao)
          conexao.commit()
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.GREEN + f"Atualização realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + f"Pressione <ENTER> para continuar ...")


#opcao 11
  def excluirAvaliacao(tabela, conexao):
      limpar()
      try:
        c = conexao.cursor()
        if tabela == 'Avaliacoes':
          dado = Professor.pesquisarAvaliacao(tabela, conexao)
          if dado != False:
            siglaA = input("Informe a sigla da avaliação a excluir: ").lower()
            while siglaA == '':
              print(Fore.RED + 'Por favor insira a sigla da avaliação que você deseja excluir')
              siglaA = input("Informe a avaliação a excluir: ").lower()
            avaliacao = (siglaA,)
            c.execute("DELETE FROM Avaliacoes WHERE siglaA=?;", avaliacao)	
            conexao.commit()
      except Error as e:
        sleep(2)
        print('Algum campo foi preenchido Incorretamente, tente novamente.')
      else:
        print(BOLD + Fore.GREEN + f"Exclusão com sucesso em {tabela}.")
        input(BOLD + Fore.BLUE + f"Pressione <ENTER> para continuar ...")

#opcao 12
  def atualizarBoletim(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'boletim':
        dado = Aluno.pesquisarBoletim(tabela, conexao)
        if dado != False:
          while True:
            aluno = input("Informe o nome do Aluno a ser a atualizado: ").lower()
            if aluno == '': print(Fore.RED + 'Por favor insira um nome')
            else: break
            while True:
              avaliacao = input("Informe a descricao da avaliação: ").lower()
              if avaliacao == '': print(Fore.RED + 'Por favor insira o nome da avaliação')
              else: break
            while True:
              dataConcl = input("Informe a data de conclusão: (AAAA-MM-DD):").lower()
              if dataConcl == '': print(Fore.RED + 'Por favor informe uma data de conclusão')
              else: break
          try:
            while True:
              notAtrib = float(input("Informe a nota do aluno:"))
              if notAtrib < 0 or notAtrib > 10: print(Fore.RED + 'Digite notas entre 0 e 10')
              else: break
          except: print('Por favor, digite apenas números')
          situacao = input('Informe a situação do aluno: ').lower()
          dados = (avaliacao, dataConcl, notAtrib, situacao, aluno)
          c.execute("UPDATE boletim SET avaliacao=?, dataConcl=?, notAtrib=?, situacao=? WHERE aluno=?;", dados)
          conexao.commit()
        else:
          sleep(1)
          print('Não a nenhum registro para atualizar')
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.GREEN + f"Atualização realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + f"Pressione <ENTER> para continuar ...")

#opcao 13          
  def excluirBoletim(tabela, conexao):
    limpar()
    try:
      c = conexao.cursor()
      if tabela == 'boletim':
        dado =  Aluno.pesquisarBoletim(tabela, conexao)
        if dado != False:
          aluno = input("Informe o aluno a excluir: ").lower()
          boletim = (aluno,)
          c.execute("DELETE FROM boletim WHERE aluno=?;", boletim)	
          conexao.commit()
        else:
          sleep(1)
          print('Não a nenhum registro para atualizar')
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(BOLD + Fore.GREEN + f"Exclusão com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + f"Pressione <ENTER> para continuar ...") 

class Aluno:
  #1
  def pesquisarBoletim(tabela, conexao):
    try:
      c = conexao.cursor()
      if tabela == 'boletim':
        nome = input("Digite o nome do aluno: ").lower()
        c.execute("SELECT * FROM boletim WHERE aluno like (?);", ('%'+nome+'%',))
      resultado = c.fetchall()
      if resultado:
        print(Fore.GREEN + "{:<15} {:<15} {:<25} {:<10}".format("Aluno", "Avaliação", "Data de Conclusão", "Nota", "Situacao"))
        for item in range(len(resultado)):
          print("{:<15} {:<15} {:<25} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3]), resultado[item][4])
      else:
        sleep(1)
        print(Fore.BLUE + "Não foram encontrados registros.")
        return False
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(Fore.GREEN + f"Pesquisa realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")
  
  #2
  def pesquisarDescricao(tabela, conexao):
    try:
      c = conexao.cursor()
      if tabela == 'boletim':
        descricao = input("Informe a descrição da prova: ")
        if descricao != '':
          c.execute(
          "SELECT * FROM boletim WHERE avaliacao like (?);", ('%'+descricao+'%',
          ))
        else:
          c.execute("SELECT * FROM boletim;")

      resultado = c.fetchall()
      if resultado:
        print(Fore.GREEN + "{:<5} {:<15} {:<25} {:<15} {:<10} {:<10}".format("ID", "Aluno", "Avaliação", "Dt Conclusão", "Nota", "Situacao"))
        for item in range(len(resultado)):
          print("{:<5} {:<15} {:<25} {:<15} {:<10} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5]))
      else:
        print(Fore.BLUE + "Não foram encontrados registros.")
    except Error as e:
      print(e)
      sleep(15)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(Fore.GREEN + f"Pesquisa realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")

 #3
  def pesquisarData(tabela, conexao):
    try:
      c = conexao.cursor()
      if tabela == 'boletim':
        data = input("Digite a data da prova (AAAA-MM-DD): ").lower()
        c.execute(
				"SELECT * FROM boletim WHERE dataConcl like (?);", ('%'+data+'%',)
			)
      resultado = c.fetchall()
      if resultado:
        print(Fore.GREEN + "{:<5} {:<50} {:<10} {:>10}".format("Aluno", "Avaliação", "Data de Conclusão", "Nota", "Situacao"))
        for item in range(len(resultado)):
          print("{:<5} {:<50} {:>10} {:>10}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3]), resultado[item][4])
      else:
        print(Fore.BLUE + "Não foram encontrados registros.")
    except:
      sleep(2)
      print('Algum campo foi preenchido Incorretamente, tente novamente.')
    else:
      print(Fore.GREEN + f"Pesquisa realizada com sucesso em {tabela}.")
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")  