import fitz  # PyMuPDF

def remove_images_from_pdf(input_pdf, output_pdf):
    """Remove todas as imagens de todas as páginas de um PDF."""
    # Abrir o PDF
    pdf_document = fitz.open(input_pdf)

    # Iterar sobre as páginas
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)  # Lista de todas as imagens na página
        
        print(f"Página {page_num + 1}: {len(image_list)} imagens encontradas.")
        
        # Remover imagens
        for img_index, img in enumerate(image_list):
            xref = img[0]  # Obter xref da imagem
            # Verifica se a imagem pode ser removida
            try:
                if page.delete_image(xref):  # Tenta remover a imagem
                    print(f"Imagem com xref {xref} removida da página {page_num + 1}.")
                else:
                    print(f"xref {xref} não é uma imagem válida ou já foi removida.")
            except Exception as e:
                print(f"Erro ao remover a imagem com xref {xref}: {e}")

    # Salvar o PDF modificado
    pdf_document.save(output_pdf)
    pdf_document.close()
    print(f"PDF salvo em: {output_pdf}")

# Exemplo de uso
input_file = r"c:.pdf"
output_file = r"c:.pdf"

# Chamada para remover imagens
remove_images_from_pdf(input_file, output_file)

print("PDF Editados com Sucesso!!")