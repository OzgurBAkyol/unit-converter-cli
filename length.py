conversion_rates = {
    "meter": 1.0, "metre": 1.0,
    "kilometer": 1000.0, "kilometre": 1000.0,
    "centimeter": 0.01, "santimetre": 0.01,
    "millimeter": 0.001, "milimetre": 0.001,
    "mile": 1609.34,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254
}


def convert(from_unit: str, to_unit: str, value: float) -> float:
    """
    Belirtilen uzunluk biriminden başka birime dönüşüm yapar.
    """
    if from_unit not in conversion_rates:
        raise ValueError(f"Geçersiz başlangıç birimi: {from_unit}")
    if to_unit not in conversion_rates:
        raise ValueError(f"Geçersiz hedef birim: {to_unit}")

    value_in_meters = value * conversion_rates[from_unit]
    result = value_in_meters / conversion_rates[to_unit]
    return result
