conversion_rates = {
    "gram": 1.0,
    "kilogram": 1000.0,
    "milligram": 0.001, "miligram": 0.001,
    "ton": 1_000_000.0,
    "pound": 453.592, "libre": 453.592,
    "ounce": 28.3495, "ons": 28.3495
}


def convert(from_unit: str, to_unit: str, value: float) -> float:
    """
    Belirtilen ağırlık biriminden başka birime dönüşüm yapar.
    """
    if from_unit not in conversion_rates:
        raise ValueError(f"Geçersiz başlangıç birimi: {from_unit}")
    if to_unit not in conversion_rates:
        raise ValueError(f"Geçersiz hedef birim: {to_unit}")

    value_in_grams = value * conversion_rates[from_unit]
    result = value_in_grams / conversion_rates[to_unit]
    return result
