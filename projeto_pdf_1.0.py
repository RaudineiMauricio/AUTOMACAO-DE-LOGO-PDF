#PROJETO FUNCIONANDO E SOBREPONDO A LOGO E O TEXTO
# 
import fitz  # PyMuPDF


def replace_logo(input_pdf, output_pdf, logo_path, x, y):
    """
    Substitui a logo em um PDF.

    Args:
        input_pdf (str): Caminho para o PDF de entrada.
        output_pdf (str): Caminho para o PDF de saída.
        logo_path (str): Caminho para a nova logo.
        x (int): Coordenada x da nova logo.
        y (int): Coordenada y da nova logo.
    """
    # Abrir o PDF
    pdf_document = fitz.open(input_pdf)

    # Iterar sobre as páginas e adicionar a logo
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        # Definir a área onde a imagem será inserida
        rect = fitz.Rect(x, y, x + 200, y + 100)
        # Inserir a imagem na página
        page.insert_image(rect, filename=logo_path)

    return pdf_document


def replace_text(page, old_text, new_text, x, y, font_size=15):
    """
    Substitui um texto em uma página do PDF.

    Args:
        page (fitz.Page): A página do PDF onde o texto será substituído.
        old_text (str): Texto a ser substituído.
        new_text (str): Novo texto a ser adicionado.
        x (int): Coordenada x para o novo texto.
        y (int): Coordenada y para o novo texto.
        font_size (int): Tamanho da fonte do novo texto.
    """
    # Encontrar o texto antigo
    text_instances = page.search_for(old_text)

    # Iterar sobre todas as instâncias do texto encontrado
    for inst in text_instances:
        # Desenhar um retângulo branco para ocultar o texto antigo
        rect = fitz.Rect(inst)
        # Ajuste a cor se o fundo não for branco
        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

        # Adicionar o novo texto
        page.insert_text((x, y), new_text, fontsize=font_size, color=(
            0, 0, 1))  # Ajuste a cor conforme necessário


def process_pdf(input_pdf, output_pdf, logo_path, logo_x, logo_y, text_replacements):
    """
    Processa o PDF para substituir a logo e o texto.

    Args:
        input_pdf (str): Caminho para o PDF de entrada.
        output_pdf (str): Caminho para o PDF de saída.
        logo_path (str): Caminho para a nova logo.
        logo_x (int): Coordenada x da nova logo.
        logo_y (int): Coordenada y da nova logo.
        text_replacements (list of tuples): Lista contendo tuplas de (old_text, new_text, x, y, font_size).
    """
    # Abrir o PDF
    pdf_document = replace_logo(
        input_pdf, output_pdf, logo_path, logo_x, logo_y)

    # Iterar sobre as páginas para substituir o texto
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        for old_text, new_text, x, y, font_size in text_replacements:
            replace_text(page, old_text, new_text, x, y, font_size)

    # Salvar o PDF atualizado
    pdf_document.save(output_pdf)
    pdf_document.close()


# Exemplo de uso
input_file = r"c:.pdf" #CAMINHO DO PDF DE ENTRADA
output_file = r"c:.pdf" #CAMINHO PARA O PDF DE SÁIDA ONDE VÃO SER SALVO OS EDITADOS
logo_image = r"c:logo nova.jpg" #NOVA IMAGEM DO PDF
logo_x_position = 190 #ESSAS POSIÇÕES PODEM SER AUTERADAS CONFORTE NECESSIDADE 
logo_y_position = -10

# Lista de substituições de texto: (old_text, new_text, x, y, font_size)
text_replacements = [
    ("Rua Viçosa do Ceará 91, Vila Mascote – São Paulo SP\n04363-090 F: (11) 5181-8777",
     # 100,150,12
     "CLSW 504 Bloco B Loja 46 – Sudoeste - Brasília – DF\n        70.673-642 Fone: (61) 3032-5568\n         contato@mundodosoleos.com", 180, 790, 12),
]

process_pdf(input_file, output_file, logo_image,
            logo_x_position, logo_y_position, text_replacements)

print("Pdfs Editadoss com Sucesso!!")