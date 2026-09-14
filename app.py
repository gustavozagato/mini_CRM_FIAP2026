from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    stage = input("Etapa no funil de vendas: ")

    # validar os dados
    # depois de validado...
    # precisamos modelar os dados do lead como um dict

    print(model_lead(name,email,stage))

    # precisa enviar para o leads.json
    # para isso, vamos usar o control/controller
    control.create_lead(model_lead(name,email,stage))

    print("\nLead adicionado (func)")

def list_leads():
    leads = control.read_leads()
    print(leads)
    # +1 desafio: printar como tabela

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do Programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("\nSaindo do Programa")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()