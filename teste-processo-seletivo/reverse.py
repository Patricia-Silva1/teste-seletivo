# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Entrada da string (pode ser definida diretamente ou através de input)
entrada = input("Digite a string que deseja inverter: ")
# entrada = "Exemplo de string"  # Você pode descomentar esta linha para usar uma string pré-definida

# Invertendo a string
resultado = inverter_string(entrada)

# Exibindo o resultado
print("String invertida:", resultado)