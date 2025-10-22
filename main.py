import os
from file_organizer import organizar_pasta

def main():
    """
    Função principal que solicita ao usuário o caminho da pasta
    e inicia o processo de organização.
    """
    print("--- Organizador de Arquivos Automático ---")

    # Solicita o caminho da pasta ao usuário
    caminho_da_pasta = input("Por favor, digite ou cole o caminho da pasta que você deseja organizar: ")

    # Verifica se o caminho fornecido é uma pasta válida
    if not os.path.isdir(caminho_da_pasta):
        print(f"Erro: O caminho '{caminho_da_pasta}' não é uma pasta válida ou não foi encontrado.")
        return

    # Se a pasta for válida, chama a função de organização
    try:
        print(f"\nIniciando a organização da pasta: {caminho_da_pasta}")
        organizar_pasta(caminho_da_pasta)
        print("\nOrganização concluída com sucesso!")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado durante a organização: {e}")

if __name__ == "__main__":
    main()
