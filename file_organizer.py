import os
import shutil

# Dicionário que mapeia tipos de arquivos para nomes de pastas .
TIPOS_DE_ARQUIVO = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    'Vídeos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Músicas': ['.mp3', '.wav', '.aac'],
    'Compactados': ['.zip', '.rar', '.7z', '.tar.gz']
}

def encontrar_tipo_de_arquivo(extensao):
    """
    Percorre o dicionário TIPOS_DE_ARQUIVO para encontrar a categoria da extensão.
    Retorna o nome da pasta ou 'Outros' se não encontrar.
    """
    for tipo, extensoes in TIPOS_DE_ARQUIVO.items():
        if extensao.lower() in extensoes:
            return tipo
    return 'Outros'

def organizar_pasta(caminho_da_pasta):
    """
    Organiza os arquivos na pasta especificada, movendo-os para subpastas
    baseadas em seu tipo.
    """
    # Lista todos os itens no diretório fornecido #
    arquivos_na_pasta = os.listdir(caminho_da_pasta)

    for nome_do_arquivo in arquivos_na_pasta:
        caminho_completo_arquivo = os.path.join(caminho_da_pasta, nome_do_arquivo)

        # -Ignora se for uma pasta
        if os.path.isdir(caminho_completo_arquivo):
            continue

        # - Obtém a extensão do arquivo
        _, extensao = os.path.splitext(nome_do_arquivo)

        # - Se não tiver extensão, ignora (ou podemos movê-lo para 'Outros')
        if not extensao:
            continue

        # - Encontra a pasta de destino
        pasta_destino_nome = encontrar_tipo_de_arquivo(extensao)
        caminho_pasta_destino = os.path.join(caminho_da_pasta, pasta_destino_nome)

        # Cria a pasta de destino se ela não existir
        # O 'exist_ok=True' evita um erro se a pasta já existir
        os.makedirs(caminho_pasta_destino, exist_ok=True)

        # Monta o caminho final para onde o arquivo será movido
        caminho_final_arquivo = os.path.join(caminho_pasta_destino, nome_do_arquivo)

        # Move o arquivo
        shutil.move(caminho_completo_arquivo, caminho_final_arquivo)
        print(f"Movido: '{nome_do_arquivo}' -> para a pasta '{pasta_destino_nome}'")
