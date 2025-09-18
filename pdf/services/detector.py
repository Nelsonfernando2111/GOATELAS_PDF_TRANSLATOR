import pdfplumber
import langid

def extrair_texto_pdf(caminho_pdf):
    """
    Extrai todo o texto de um PDF usando pdfplumber.
    Retorna uma string com o texto concatenado de todas as páginas.
    """
    texto = ""
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            pagina_texto = pagina.extract_text()
            if pagina_texto:
                texto += pagina_texto + "\n"
    return texto.strip()

def detectar_idioma_pdf(caminho_pdf):
    """
    Detecta o idioma predominante do PDF usando langid.
    Retorna uma tupla (codigo_idioma, confianca).
    """
    texto = extrair_texto_pdf(caminho_pdf)
    if not texto:
        return None, 0 
    idioma, confianca = langid.classify(texto)
    return idioma, confianca
