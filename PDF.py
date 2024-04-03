import PyPDF2
from PyPDF2 import PdfReader

# def lector(filename): #leer pdf
#     reader = PdfReader(filename)
#     print(f'Numero de paginas: {len(reader.pages)}')
#     data = reader.pages[1].extract_text()
#     return data

def lector(archivo_pdf):
    with open(archivo_pdf, "rb") as f:
        reader = PdfReader(f)
        resultado = []
        for i in range(0, len(reader.pages)):
            pagina_seleccionada = reader.pages[i]
            texto = pagina_seleccionada.extract_text()
            resultado.append(texto)
        return ' '.join(resultado)

#print(lector("PDF1.pdf"))


def comunes(pdf1, pdf2): #encontrar parrafo comunes
    palabras_pdf = lector(pdf1)
    palabras_pdf2 = lector(pdf2)
    lista_parrafos = palabras_pdf.split('\n')#parrafo pdf1
    lista_parrafos2 = palabras_pdf2.split('\n')#parrafo pdf2
    resultado = [] #vacio
    for parrafo1 in lista_parrafos:
        for parrafo2 in lista_parrafos2:
            if parrafo1 == parrafo2:
                resultado.append(parrafo1)
    #if palabras_pdf == palabras_diccionario:
    #    pal_comunes = palabras_pdf
    return resultado


#llamar funcion comunes
parrafos_comunes = comunes("PDF 1R.pdf", "Diccionari R.pdf")
imprimir = lector("PDF PRUEBA.pdf")
print (imprimir)
# imprime parrafo comunes
if parrafos_comunes:
    with open("Resultado.txt", "w") as archivo:
        archivo.write("Los parrafos comunes en el PDF y en el diccionario son:"+ '\n')
        for elemento in parrafos_comunes:
            archivo.write(elemento + '\n')
    
else:
    with open("Resultado.txt", "w") as archivo:
        archivo.write("No hay parafos comunes")
