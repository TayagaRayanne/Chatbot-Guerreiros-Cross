import string
import os

def exibir_opcoes():
    # Função para exibir as opções disponíveis para o usuário.
    print("1 - Você deseja ver a grade de aulas?")
    print("2 - Você deseja pagar a mensalidade?")
    print("3 - Você está com problemas para agendar sua aula?")
    print("4 - Você deseja deixar uma sugestão?")
    print("5 - Você deseja falar com a recepção?")
    print("6 - Encerrar conversa")
    
def exibir_grade_aulas():
    # Função para exibir a grade de aulas.
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    print("Grade de aulas da semana:\n")
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    aulas_especificas = {
        "Segunda": "LPO",
        "Terça": "Gymnastic",
        "Quarta": "Hyrox",
        "Quinta": "Core",
        "Sexta": "Endurance"
    }
    # Segunda a sexta
    for dia in dias_semana:
        print(f"{dia}:")
        for hora in range(5, 13):  # 5h até 12h
            if hora == 7:
                print(f"  {hora:02d}:00 - {aulas_especificas[dia]}")
            else:
                print(f"  {hora:02d}:00 - Cross Training")
        print()
    # Sábado
    print("Sábado:")
    for hora in range(7, 10):  # 7h, 8h, 9h
        print(f"  {hora:02d}:00 - Cross Training")
    print("Obs: Os horários podem variar conforme a demanda.")
    voltar_menu()
    
def pagar_mensalidade():
    # Função para simular o pagamento da mensalidade.
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    print("Você pode pagar sua mensalidade através do nosso site ou aplicativo.")
    print("Para mais informações, acesse o link https://guerreiroscross.com.br")
    voltar_menu()

def agendar_aula():  
    # Função para agendar uma aula.
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    print("Se não está conseguindo agendar sua aula, por favor, deixe seu nome completo e o horário desejado para que possamos verificar.")
    cliente = input("Digite seu nome completo: ")
    horario = input("Digite o horário desejado (ex: 08:00): ")
    print("Ou, acesse nosso site https://guerreiroscross.com.br.")
    print(f"Obrigado, {cliente}! Sua solicitação para agendar a aula no horário {horario} foi recebida e passada para recepção.")
    voltar_menu()
    
def deixar_sugestao():
    # Função para receber sugestões do usuário.
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    print("Sua sugestão é muito importante para nós!")
    sugestao = input("Por favor, digite sua sugestão: ")
    print(f"Obrigado pela sua sugestão: '{sugestao}'! Vamos analisá-la.")
    voltar_menu()
    
def falar_com_atendente():
    # Função para falar com um atendente.
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    print("Para falar com um atendente, por favor, aguarde a reposta da nossa equipe. \nEles responderão dentro do horário de funcionamento: ")
    print("De segunda à sexta, de manhã das 8h às 12h, e à tarde das 15h às 21h.")
    print("Sábados, das 7h às 9h.")
    print("Ou envie um e-mail para @guerreiroscross.com.br.")
    voltar_menu()
    
def despedida():
    # Função para encerrar a conversa com o usuário.
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    print("Obrigado por entrar em contato conosco!")
    print("Esperamos vê-lo em breve na Guerreiros Cross!")
    
    
def escolher_opcao():
    # Função para escolher uma opção do menu.
    try:
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            exibir_grade_aulas()
        elif opcao == 2:
            pagar_mensalidade()
        elif opcao == 3:
            agendar_aula()
        elif opcao == 4:
            deixar_sugestao()
        elif opcao == 5:
            falar_com_atendente()
        elif opcao == 6:
            despedida()
        else:
            print("Opção inválida. Por favor, tente novamente.")
            
    except:
        print("Entrada inválida. Por favor, digite um número.")

def voltar_menu():
    # Função para voltar ao menu principal.
    input("Click enter para voltar ao menu principal.")
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    run_chatbot()
    
def logo():
    # Função para exibir o logo do chatbot.
    print("""
░█▀▀█ ░█─░█ ░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ▀█▀ ░█▀▀█ ░█▀▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀█ 
░█─▄▄ ░█─░█ ░█▀▀▀ ░█▄▄▀ ░█▄▄▀ ░█▀▀▀ ░█─ ░█▄▄▀ ░█──░█ ─▀▀▀▄▄ 　 ░█─── ░█▄▄▀ ░█──░█ ─▀▀▀▄▄ ─▀▀▀▄▄ 
░█▄▄█ ─▀▄▄▀ ░█▄▄▄ ░█─░█ ░█─░█ ░█▄▄▄ ▄█▄ ░█─░█ ░█▄▄▄█ ░█▄▄▄█ 　 ░█▄▄█ ░█─░█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄█
          """)

def run_chatbot():
    # Função principal que executa o loop de conversação do chatbot.
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
    logo()
    print("Olá! Bem vindo a Guerreiros Cross!")
    print("Estou aqui para ajudar. O que você gostaria de saber?")
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    run_chatbot()