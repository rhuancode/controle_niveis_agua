import colorama

entrada_usuario = "Nível 5"

niveis = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]

def cor_mensagem_nivel(entrada_usuario, niveis):
    if entrada_usuario == niveis[0]:
        return f"{colorama.Fore.RED}{niveis[0]} - Muito baixo (crítico){colorama.Style.RESET_ALL}"
    elif entrada_usuario == niveis[1]:
        return f"{colorama.Fore.YELLOW}{niveis[1]} - Baixo{colorama.Style.RESET_ALL}"
    elif entrada_usuario == niveis[2]:
        return f"{colorama.Fore.GREEN}{niveis[2]} - Médio{colorama.Style.RESET_ALL}"
    elif entrada_usuario == niveis[3]:
        return f"{colorama.Fore.CYAN}{niveis[3]} - Alto{colorama.Style.RESET_ALL}"
    elif entrada_usuario == niveis[4]:
        return f"{colorama.Fore.BLUE}{niveis[4]} - Muito alto (alerta){colorama.Style.RESET_ALL}"
    else:
        return "Nível Inválido!"
        
resultado = cor_mensagem_nivel(entrada_usuario, niveis)
print(f"{resultado}")
