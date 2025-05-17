def formarChaveEstendida(chave, mensagem): 
    chaveFinal = ""
    tamanho_msg = len(mensagem)

    while True:
        for i in range(len(chave)):
            if tamanho_msg == 0:
                return chaveFinal
            
            chaveFinal += chave[i]
            tamanho_msg -= 1

def criptografar(chave, mensagem, alfabeto):
    msg_criptografada = ""
    for i in range(len(mensagem)):
        id_atual_msg = alfabeto.index(mensagem[i])
        id_atual_chave = alfabeto.index(chave[i])

        calculo_indice = (id_atual_msg + id_atual_chave) % len(alfabeto)
        msg_criptografada += alfabeto[calculo_indice]

    return msg_criptografada

def decriptografar(chave, mensagemCifrada, alfabeto):
    msg_decriptografada = ""
    for i in range(len(mensagemCifrada)):
        id_atual_msg = alfabeto.index(mensagemCifrada[i])
        id_atual_chave = alfabeto.index(chave[i])
        
        calculo_indice = (id_atual_msg - id_atual_chave + len(alfabeto)) % len(alfabeto)
        msg_decriptografada += alfabeto[calculo_indice]

    return msg_decriptografada

def verificar_alfabeto(entrada, alfabeto):
    for char in entrada:
        if char not in alfabeto:
            return False
    return True


chave = input("Digite a chave: ")
mensagem = input("Digite a mensagem: ")
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,;._#*\"\"-+"


if not verificar_alfabeto(chave, alfabeto):
    print("A mensagem contém caracteres invalidos!")
else:
    if not verificar_alfabeto(mensagem, alfabeto):
        print("A mensagem contém caracteres invalidos!")
    else:
        chaveFinal = formarChaveEstendida(chave, mensagem)
        escolha = input("Quer encriptar ou decriptar a mensagem? (e/d): ").lower()

        if escolha == 'e':
            mensagemCifrada = criptografar(chaveFinal, mensagem, alfabeto)
            print("Mensagem Cifrada: ", mensagemCifrada)
        elif escolha == 'd':
            mensagemDecriptografada = decriptografar(chaveFinal, mensagem, alfabeto)
            print("Mensagem Decriptografada: ", mensagemDecriptografada)
        else:
            print("Opção inválida! Digite 'e' para encriptar ou 'd' para decriptar")
