def formarChaveEstendida(chave, mensagem): 
    chaveFinal = ""; tamanho_msg = len(mensagem)

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


chave = "segredo"
mensagem = "ataque amanha amigo"
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,;._#*\"\"-+"


'''
alfabeto = "abcdefghijklmnopqrstuvwxyz"
mensagem = "segredofoda"
chave = "lontra"
'''

chaveFinal = formarChaveEstendida(chave, mensagem)
print("ChaveFinal: ", chaveFinal)
mensagemCifrada = criptografar(chaveFinal, mensagem, alfabeto)
print("Mensagem Cifrada: ", mensagemCifrada)
mensagemDecriptografada = decriptografar(chaveFinal, mensagemCifrada, alfabeto)
print("Mensagem Decriptografada: ", mensagemDecriptografada)


print("Tamanho Mensagem: ", len(mensagem))
print("Tamanho Chave: ", len(chaveFinal))
print("Tamanho Mensagem Final: ", len(mensagemCifrada)) 