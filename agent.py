import re
import requests
import json
from fallbacks.vector_fallback import find_closest

OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

unit_to_type = {
    "meter": "length", "metre": "length",
    "kilometer": "length", "kilometre": "length",
    "centimeter": "length", "santimetre": "length",
    "millimeter": "length", "milimetre": "length",
    "mile": "length", "yard": "length", "foot": "length", "inch": "length",
    "gram": "weight", "kilogram": "weight",
    "milligram": "weight", "miligram": "weight",
    "ton": "weight", "ons": "weight", "libre": "weight",
    "celsius": "temperature", "celcius": "temperature", "santigrat": "temperature",
    "fahrenheit": "temperature", "kelvin": "temperature"
}

def normalize_text(text: str) -> str:
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\b(metre|gram|litre|santigrat|kelvin|fahrenheit|celsius|milimetre|santimetre|kilometre)(ye|yi|ya|dan|e|i|a|de|den|te|ten)?\b", r"\1", text)
    return text

def ask_llm(text: str) -> dict:
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/ozgurberkeakyol/unit-converter-cli",
            "X-Title": "Unit Converter CLI"
        }
        
        data = {
            "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
            "messages": [
                {
                    "role": "system",
                    "content": """Sen bir birim dönüştürme asistanısın. Kullanıcının girdiği metinden birim dönüşümü için gerekli bilgileri çıkar.
                    Desteklenen birimler:
                    - Uzunluk: metre, kilometre, santimetre, milimetre, mile, yard, foot, inch
                    - Ağırlık: gram, kilogram, miligram, ton, ons, libre
                    - Sıcaklık: celsius, fahrenheit, kelvin
                    
                    Yanıtını şu JSON formatında ver:
                    {
                        "type": "length|weight|temperature",
                        "from_unit": "kaynak_birim",
                        "to_unit": "hedef_birim",
                        "value": sayısal_değer
                    }"""
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        }
        
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return None
        return None
    except Exception as e:
        print(f"LLM API hatası: {e}")
        return None

def parse_sentence(text: str) -> dict:
    try:
        return parse_with_regex(text)
    except ValueError:
        llm_result = ask_llm(text)
        if llm_result:
            return llm_result
        
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