import re
from fallbacks.vector_fallback import find_closest


unit_to_type = {
    # Length (English + Turkish)
    "meter": "length", "metre": "length",
    "kilometer": "length", "kilometre": "length",
    "centimeter": "length", "santimetre": "length",
    "millimeter": "length", "milimetre": "length",
    "mile": "length", "yard": "length", "foot": "length", "inch": "length",

    # Weight
    "gram": "weight",
    "kilogram": "weight",
    "milligram": "weight", "miligram": "weight",
    "ton": "weight",

    # Temperature
    "celsius": "temperature", "celcius": "temperature", "santigrat": "temperature",
    "fahrenheit": "temperature",
    "kelvin": "temperature",

    "ons": "weight",
    "libre": "weight",
}

import re


def normalize_text(text: str) -> str:
    text = re.sub(r"[^\w\s]", " ", text)
    # Türkçedeki ekleri sadeleştir
    text = re.sub(
        r"\b(metre|gram|litre|santigrat|kelvin|fahrenheit|celsius|milimetre|santimetre|kilometre)(ye|yi|ya|dan|e|i|a|de|den|te|ten)?\b",
        r"\1", text)
    return text


def parse_sentence(text: str) -> dict:
    try:
        return parse_with_regex(text)
    except ValueError:
        fallback = find_closest(text)
        if fallback:
            return {
                "type": fallback["type"],
                "from_unit": fallback["from_unit"],
                "to_unit": fallback["to_unit"],
                "value": fallback["value"]
            }
        else:
            raise ValueError("Cümle yorumlanamıyor: daha fazla bağlam gerek.")

def parse_with_regex(text: str) -> dict:
    text = text.lower()

    matches = re.findall(r"\b\d+(?:\.\d+)?\b", text)
    if not matches:
        raise ValueError("Girdi içinde sayısal bir değer bulunamadı.")

    value = float(matches[0])

    found_units = sorted(
        [unit for unit in unit_to_type if re.search(rf"\b{unit}\b", text)],
        key=lambda u: text.index(u)
    )

    if len(found_units) < 2:
        raise ValueError("En az iki farklı birim (kaynak ve hedef) belirtilmelidir.")

    from_unit, to_unit = found_units[0], found_units[1]
    conversion_type = unit_to_type[from_unit]

    return {
        "type": conversion_type,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "value": value
    }



