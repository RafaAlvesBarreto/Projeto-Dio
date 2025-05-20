import re

def identificar_bandeira(numero_cartao: str) -> str:
    numero_cartao = numero_cartao.replace(" ", "")
    padroes = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^(5[1-5][0-9]{14}|2(2[2-9][0-9]{12}|[3-6][0-9]{13}|7[01][0-9]{12}|720[0-9]{12}))$",
        "American Express": r"^3[47][0-9]{13}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "Cirrus": r"^(5018|5020|5038|6304|6759|6761|6762|6763|2340)[0-9]{12}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Elo": r"^(4011(78|79)|431274|438935|504175|451416|457393|5067(0[0-9]|1[0-9]|20)|5090[0-9]{2}|627780|636297|636368)[0-9]{0,10}$",
    }
    for bandeira, padrao in padroes.items():
        if re.match(padrao, numero_cartao):
            return bandeira
    return "Bandeira desconhecida ou inválida"

# Banco de dados simples (lista de dicionários)
cartoes = []

def adicionar_cartao(nome: str, numero: str):
    numero = numero.replace(" ", "")
    if not numero.isdigit():
        print("Número inválido. Deve conter apenas dígitos.")
        return
    bandeira = identificar_bandeira(numero)
    cartoes.append({
        "nome": nome,
        "numero": numero,
        "bandeira": bandeira
    })

def listar_cartoes():
    if not cartoes:
        print("Nenhum cartão cadastrado.")
        return
    for cartao in cartoes:
        print(f"Nome: {cartao['nome']}, Número: {cartao['numero']}, Bandeira: {cartao['bandeira']}")

def main():
    print("Bem-vindo ao sistema de cartões!")
    try:
        while True:
            print("\n1. Adicionar cartão\n2. Listar cartões\n3. Sair")
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                nome = input("Nome do titular: ").strip()
                numero = input("Número do cartão: ").strip()
                adicionar_cartao(nome, numero)
                print("Cartão adicionado!")
            elif opcao == "2":
                listar_cartoes()
            elif opcao == "3":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")

if __name__ == "__main__":
    main()
