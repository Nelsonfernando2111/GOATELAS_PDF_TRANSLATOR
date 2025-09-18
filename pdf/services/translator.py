from deep_translator import GoogleTranslator

def traduzir_texto(texto, idioma_origem, idioma_destino):
    """
    Traduz texto usando deep-translator (Google).
    idioma_origem: detectado pelo langid
    idioma_destino: escolhido pelo usuário
    """
    if not texto.strip():
        return ""
    
    try:
        traducao = GoogleTranslator(
            source=idioma_origem,
            target=idioma_destino
        ).translate(texto)
        return traducao
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return texto
