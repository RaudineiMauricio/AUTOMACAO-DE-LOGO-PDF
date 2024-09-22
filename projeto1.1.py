#ESSE CÓDIGO FUNCIONA REMOVE A IMAGEM ANTIGA, DEIXA APENAS UM QUADRADO NO LUGAR.
import fitz  # PyMuPDF

def replace_and_add_image(input_pdf, output_pdf, new_image_path, offset_x=100):
    # Abra o PDF
    pdf_document = fitz.open(input_pdf)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        # Obtenha as imagens da página
        image_list = page.get_images(full=True)
        
        # Verifique se há imagens na página
        if image_list:
            for image_index, img in enumerate(image_list):
                xref = img[0]
                image_rects = page.get_image_rects(xref)
                
                if image_rects:
                    img_rect = image_rects[0]  # Pegue as coordenadas da primeira imagem
                    
                    # Se esta imagem for a que você deseja remover (suponha que seja a primeira)
                    if image_index == 0:  # Alterar o índice, se necessário, para corresponder à imagem a ser excluída
                        page.delete_image(xref)  # Remove a imagem selecionada (EBF Comercial)
                    
                    # Se esta for a imagem que você quer adicionar uma nova ao lado (Mundo dos Óleos)
                    if image_index == 1:  # Supondo que esta seja a segunda imagem (índice 1)
                        # Defina a posição da nova imagem ao lado da atual
                        new_x0 = img_rect.x1 + -10
                        new_x1 = new_x0 + 150  # Largura da nova imagem (pode ajustar)
                        new_y0 = img_rect.y0 -50
                        new_y1 = new_y0 + 100  # Altura da nova imagem (pode ajustar)
                        
                        # Criar o retângulo para a nova imagem
                        rect = fitz.Rect(new_x0, new_y0, new_x1, new_y1)
                        
                        # Adicionar a nova imagem ao lado da imagem existente
                        page.insert_image(rect, filename=new_image_path)
    
    # Salvar o PDF com as modificações
    pdf_document.save(output_pdf)
    pdf_document.close()

# Exemplo de uso
input_pdf = r"c:.pdf"
output_pdf = r"c:.pdf"
new_image = r"logo nova.jpg"
replace_and_add_image(input_pdf, output_pdf, new_image, offset_x=50)  # Ajuste o offset conforme necessário

print("PDFS EDITADOS")
