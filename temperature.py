def convert(from_unit: str, to_unit: str, value: float) -> float:
    """
    Sıcaklık dönüşümleri: Celsius, Fahrenheit, Kelvin + Türkçe eşanlamlılar
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit in ["celsius", "celcius", "santigrat"]:
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError(f"Geçersiz başlangıç birimi: {from_unit}")

    if to_unit in ["celsius", "celcius", "santigrat"]:
        return celsius
    elif to_unit == "fahrenheit":
        return celsius * 9 / 5 + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        raise ValueError(f"Geçersiz hedef birim: {to_unit}")
