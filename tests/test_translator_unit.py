import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__))) 
import pytest
from translator import translate

def test_translate_apple_to_spanish():
    query = "apple"
    locale = "es-ES"
    result = translate(query,locale)

    assert result == "manzana", f"Esperaba 'manzana' pero obtuve'{result}'"

@pytest.mark.parametrize("word,locale,expected", [
    ("apple", "es-ES", "manzana"),
    ("bread", "de-DE", "brot"),
    ("lemon", "it-IT", "limone"),
])
def test_multiple_translations(word,locale,expected):
    result = translate(word,locale)
    assert result == expected

    