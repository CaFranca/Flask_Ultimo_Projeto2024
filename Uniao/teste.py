def antiXSS(valor):
        for char in valor:
            if char == "<" or char ==">" or char == "'" or char == "=" or char == '"':
                print("Erro: tentativa de XSS")
                return True
                

texto_suspeito = "<script>"
texto_pog = antiXSS(texto_suspeito)
print(texto_pog)