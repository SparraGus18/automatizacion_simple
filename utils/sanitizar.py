import unicodedata

def sanitizar(texto):
    # 1. Convertir a minúsculas y quitar espacios en blanco a los lados
    texto = texto.lower().strip()
    
    # 2. Normalizar el texto para separar los acentos de las letras
    # NFD descompone caracteres como 'ñ' en 'n' + '~' o 'á' en 'a' + '´'
    texto_normalizado = unicodedata.normalize('NFD', texto)
    
    # 3. Filtrar solo los caracteres que no sean marcas de acentuación (Mn)
    # y reconstruir la cadena. Esto elimina tildes, diéresis y el moño de la ñ.
    texto_sin_tildes = "".join(
        c for c in texto_normalizado 
        if unicodedata.category(c) != 'Mn'
    )
    
    # 4. (Opcional) Si quieres ser muy estricto, podrías codificar a ASCII 
    # y decodificar, pero con el paso anterior ya tienes lo que pidió el profe.
    return texto_sin_tildes