import argparse
import length
import weight
import temperature
import agent

def run_conversion(conversion_type, from_unit, to_unit, value):
    if conversion_type == "length":
        return length.convert(from_unit, to_unit, value)
    elif conversion_type == "weight":
        return weight.convert(from_unit, to_unit, value)
    elif conversion_type == "temperature":
        return temperature.convert(from_unit, to_unit, value)
    else:
        raise ValueError(f"Bilinmeyen dönüşüm türü: {conversion_type}")

def main():
    parser = argparse.ArgumentParser(description="Birim dönüştürücü CLI aracı")

    parser.add_argument("--agent", action="store_true", help="Doğal dil modunu etkinleştir")

    parser.add_argument("--type", choices=["length", "weight", "temperature"], help="Dönüştürme türü")
    parser.add_argument("--from", dest="from_unit", help="Başlangıç birimi")
    parser.add_argument("--to", dest="to_unit", help="Hedef birim")
    parser.add_argument("--value", type=float, help="Dönüştürülecek sayı")

    args = parser.parse_args()

    try:
        if args.agent:
            sentence = input("💬 Ne dönüştürmek istersiniz? → ")
            parsed = agent.parse_sentence(sentence)
            result = run_conversion(
                parsed["type"], parsed["from_unit"], parsed["to_unit"], parsed["value"]
            )
            print(f"\n🤖 {parsed['value']} {parsed['from_unit']} = {result:.4f} {parsed['to_unit']}")

        else:
            if not all([args.type, args.from_unit, args.to_unit, args.value is not None]):
                raise ValueError("Lütfen tüm parametreleri girin veya --agent modunu kullanın.")

            result = run_conversion(
                args.type, args.from_unit, args.to_unit, args.value
            )
            print(f"\n✅ {args.value} {args.from_unit} = {result:.4f} {args.to_unit}")

    except Exception as e:
        print(f"\n❌ Hata: {e}")

if __name__ == "__main__":
    main()
