"""Ponto de entrada da calculadora Fleet Force (Sprint 1)."""
from src.input import collect_fleet_data
from src.report import build_report


def main() -> None:
    print("FLEET FORCE — CALCULADORA DE CUSTOS DE FROTA")
    while True:
        data = collect_fleet_data()
        print("\n" + build_report(data) + "\n")
        while True:
            response = input("Deseja calcular outro período/frota? (s/n): ").strip().lower()
            if response in ("s", "n"):
                break
            print("Digite 's' ou 'n'.")
        if response == "n":
            print("Programa encerrado.")
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma encerrado.")
