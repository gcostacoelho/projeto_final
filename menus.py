import colorama
from colorama import Fore

colorama.init(autoreset='true')
BOLD = '\033[1m'

def menuProf():
  print(25 * '-')
  print("---- O que deseja fazer? ----")
  print(BOLD + Fore.RED + "0. Sair")
  print("1. Avaliação")
  print(Fore.BLUE + "2. Tipo de avaliação")
  print(Fore.BLUE + "3. Boletim")
  try:
    menu = int(input('Escolha uma função: '))
    if menu < 0 or menu > 3:
      print('Opção inválida')
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")
    else: return menu
  except:
    print(BOLD + Fore.RED + 'Por favor, insira apenas números')
    input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")

def menuAv():
  print(25 * '-')
  print("---- O que deseja fazer? ----")
  print(BOLD + Fore.RED + "0. Sair")
  print("1. Nova avaliação")
  print(Fore.MAGENTA + "2. Ver todas avaliações")
  print(BOLD + Fore.CYAN + '3. Atualizar avaliação')
  print(BOLD + Fore.LIGHTYELLOW_EX + '4. Excluir avaliação')
  print(Fore.GREEN + "5. Ver notas máximas")
  print(Fore.RED + "6. Ver notas mínimas ")
  try:
    menu = int(input('Escolha uma opção: '))
    if menu < 0 or menu > 6:
      print(Fore.RED + 'Opção inválida')
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")
    else: return menu
  except:
    print(BOLD + Fore.RED + 'Por favor, insira apenas números')
    input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")

def menuTipo():
  print(25 * '-')
  print("---- O que deseja fazer? ----")
  print(BOLD + Fore.RED + "0. Sair")
  print(Fore.BLUE + "1. Novo tipo de avaliação")
  print(Fore.YELLOW + "2. Ver tipo de avaliação")
  print(Fore.BLUE + "3. Atualizar tipo de avaliação")
  print(Fore.MAGENTA + "4. Excluir tipo de avaliação")
  try:
    menu = int(input('Escolha uma opção: '))
    if menu < 0 or menu > 4:
      print('Opção inválida')
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")
    else: return menu
  except:
    print(BOLD + Fore.RED + 'Por favor, insira apenas números')
    input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")

def menuBoletim():
  print(25 * '-')
  print("---- O que deseja fazer? ----")
  print(BOLD + Fore.RED + "0. Sair")
  print("1. Cadastar Boletim")
  print(Fore.MAGENTA + "2. Pesquisar boletim")
  print(Fore.GREEN + "3. Atualizar boletim")
  print(Fore.GREEN + "4. Excluir boletim")
  try:
    menu = int(input('Escolha uma opção: '))
    if menu < 0 or menu > 4:
      print('Opção inválida')
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")
    else: return menu
  except:
    print(BOLD + Fore.RED + 'Por favor, insira apenas números')
    input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")

def Aluno():
  print(25 * '-')
  print(f"---- O que deseja fazer? ----")
  print(Fore.RED + '0. Sair')
  print(BOLD + f"1. Pesquisar avaliação")
  print(Fore.BLUE + BOLD +"2. Ver boletim")
  print(Fore.CYAN + BOLD +'3. Pesquisar por data')
    
  try:
    opcaoA= int(input('Escolha a opção: '))
    if opcaoA < 0 or opcaoA > 3: 
      print(Fore.RED + 'Opção inválida')
      input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar ...")
    else: return opcaoA
  except: 
    print(BOLD + Fore.RED + 'Por favor, insira apenas números')
    input(BOLD + Fore.BLUE + "Pressione <ENTER> para continuar...")