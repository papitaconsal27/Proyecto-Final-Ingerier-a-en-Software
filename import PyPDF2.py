import PyPDF2
from PyPDF2 import PdfReader
from fpdf import FPDF
import os



def lector(archivo_pdf): #funcion para leer el pdf
    with open(archivo_pdf, "rb") as f: 
        reader = PdfReader(f)
        resultado = [] #convertir el pdf a una lista
        for i in range(0, len(reader.pages)): #leer todas las paginas
            pagina_seleccionada = reader.pages[i]
            texto = pagina_seleccionada.extract_text()
            resultado.append(texto)
        return ' '.join(resultado) #juntar paginas



def comunes(pdf1, pdf2): #encontrar parrafo comunes
    palabras_pdf = lector(pdf1)
    palabras_pdf2 = lector(pdf2)
    lista_parrafos = palabras_pdf.split('\n')#parrafo pdf1
    lista_parrafos2 = palabras_pdf2.split('\n')#parrafo pdf2

    lista_frase2 = palabras_pdf2.split('\n')#parrafo del diccionario 
    resultado = [] #lista vacia
    j = 0
    for frase in lista_frase2:
        secuencia = ""
        frase = lista_frase2[j] #la linea en la que voy de mi diccionario
        for i in range (len(palabras_pdf)):
            secuencia = palabras_pdf[i:i+len(frase)-2]
            for k in range (len(frase)-2):
                if (secuencia[k] == frase[k]):
                    if (k == (len(frase)-3)):#llego al final de la frase
                        resultado.append(frase)
                else:
                    break
        j = j+1
    return resultado



print("Escribe la direccion del PDF a comparar: ")
documento = input()
print ("Escribe la direccion del diccionario: ")
diccionario = input()

#llamar funcion comunes
parrafos_comunes = comunes(documento, diccionario)


# imprime frases comunes en txt
if parrafos_comunes:
    with open("Resultado.txt", "w") as archivo:
        archivo.write("Los parrafos comunes en el PDF y en el diccionario son:"+ '\n')
        for elemento in parrafos_comunes:
            archivo.write(elemento + '\n')
else:
    with open("Resultado.txt", "w") as archivo:
        archivo.write("No hay parafos comunes")



# imprime frases comunes en PDF
pagina = FPDF()
pagina.add_page()
pagina.set_font('Arial', 'B', 20)

if parrafos_comunes:
    pagina.write (4, "Las frases comunes entre el PDF y el diccionario son:"+ '\n')
    pagina.set_font('Arial', size=12)
    pagina.set_xy(10, 25)
    textos = ""
    for elemento in parrafos_comunes:
        textos += elemento + "\n"
    pagina.multi_cell(190, 10, textos, align='J')
    pagina.output('Frases Comunes.pdf', 'F')
else:
    pagina.write (4, "No hay frases comunes")
    pagina.output('Frases Comunes.pdf', 'F')