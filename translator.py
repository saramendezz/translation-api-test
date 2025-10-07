TRANSLATIONS = {
    ("apple", "es-ES"): "manzana",
    ("bread", "de-DE"): "brot",
    ("lemon", "it-IT"): "limone",
}

def translate(query:str, locale:str) -> str:
    return TRANSLATIONS.get((query, locale), "N/A")