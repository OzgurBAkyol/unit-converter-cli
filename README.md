# Birim Dönüştürücü CLI Aracı

Bu araç, komut satırından birim dönüşümleri yapmanızı sağlayan bir Python uygulamasıdır.

## Özellikler

- Uzunluk, ağırlık ve sıcaklık birimleri arasında dönüşüm
- Doğal dil desteği (Türkçe ve İngilizce)
- Hem komut satırı argümanları hem de doğal dil girişi desteği

## Kurulum

```bash
# Poetry ile kurulum
poetry install

# veya pip ile kurulum
pip install .
```

## Kullanım

### Komut Satırı Modu

```bash
python converter.py --type length --from metre --to kilometre --value 1000
```

### Doğal Dil Modu

```bash
python converter.py --agent
# Ardından sorulacak soruya örnek:
# "1000 metreyi kilometreye çevir"
```

## Desteklenen Birimler

### Uzunluk
- metre, kilometre, santimetre, milimetre
- mile, yard, foot, inch

### Ağırlık
- gram, kilogram, miligram, ton
- ons, libre

### Sıcaklık
- celsius, fahrenheit, kelvin

## Lisans

MIT
