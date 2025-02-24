def criar_contato(nome, telefone, email):
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print("Contato adicionado na sua agenda.")
  return

def visualizar_contatos(contatos):
  if not contatos:
        print("Nenhum contato na agenda.")
        return
  
  print("\nLista de contatos:")
  for i, contato in enumerate(contatos):
    indice_formatado = i + 1;
    favorito = '★' if contatos[i]["favorito"] else " "
    print(f"{indice_formatado}. nome: {contato['nome']}, telefone: {contato['telefone']}, email: {contato['email']} {favorito}")
  return

def editar_contato(contatos, indice, chave, valor):
  if valor.strip():
    contatos[indice][chave] = valor
  return

def visualizar_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  for i, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      print(f"{i}. nome: {contato['nome']}, telefone: {contato['telefone']}, email: {contato['email']}")
  return

def deletar_contato(indice, contatos):
  nome = contatos[indice]["nome"]
  del contatos[indice]
  print(f"Contato {nome} deletado com sucesso")
  return

contatos = []

while True:
  print("\nMenu da Agenda")
  print("1. Adicionar contato")
  print("2. Visualizar lista de contatos")
  print("3. Editar contatos")
  print("4. Marcar/Desmarcar contato como favorito")
  print("5. Visualizar lista de contatos favoritos")
  print("6. Apagar contato")
  print("7. Sair")
  escolha = input("Digite sua escolha: ")

  if escolha == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número do contato: ")
    email = input("Digite o email do contato: ")
    criar_contato(nome, telefone, email)
  elif escolha == "2":
    visualizar_contatos(contatos)
  elif escolha == "3":
    visualizar_contatos(contatos)
    try:
      indice = int(input("Selecione o contato para atualizar: ")) - 1
      if 0<= indice < len(contatos):
        nome = input("Digite o novo nome do contato: ")
        telefone = input("Digite o novo número do contato: ")
        email = input("Digite o novo email do contato: ")
        editar_contato(contatos, indice, "nome", nome)
        editar_contato(contatos, indice, "telefone",telefone)
        editar_contato(contatos, indice, "email",email)
        print(f"Contato {contatos[indice]["nome"]} atualizado com sucesso")
      else: 
        print("Número de índice inválido")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
  elif escolha == "4":
    visualizar_contatos(contatos)
    try:
      indice = int(input("Selecione o contato para favoritar/desfavoritar: ")) - 1
      if 0<= indice < len(contatos):
        if contatos[indice]["favorito"]:
          contatos[indice]["favorito"] = False
          print("Contato removido dos favoritos")
        else:
          contatos[indice]["favorito"] = True
          print("Contato adicionado aos favoritos")
      else: 
        print("Número de índice inválido")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
  elif escolha == "5":
    visualizar_favoritos(contatos)
  elif escolha == "6":
    visualizar_contatos(contatos)
    try:
      indice = int(input("Selecione o contato para deletar: ")) - 1
      if 0<= indice < len(contatos):
        deletar_contato(indice, contatos)
      else: 
        print("Número de índice inválido")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
  elif escolha == "7":
    print("Saída do sistema efetuada com sucesso.")
    break
  else:
    print("Opção inválida. Escolha uma opção entre 1 e 7.")