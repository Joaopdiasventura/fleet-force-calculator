"""Entrada interativa e validação dos dados."""

COST_CATEGORIES = {
    "fuel": "Combustível",
    "maintenance": "Manutenção",
    "tolls": "Pedágios",
    "fines": "Multas",
    "taxes": "Impostos",
    "other": "Outros custos",
}


def read_nonnegative_float(message: str) -> float:
    while True:
        raw = input(message).strip().replace(",", ".")
        try:
            value = float(raw)
            if value < 0 or not (value < float("inf")):
                raise ValueError
            return value
        except ValueError:
            print("Valor inválido. Informe um número maior ou igual a zero.")


def read_positive_int(message: str) -> int:
    while True:
        raw = input(message).strip()
        try:
            value = int(raw)
            if value > 0:
                return value
        except ValueError:
            pass
        print("Valor inválido. Informe um número inteiro maior que zero.")


def read_required_text(message: str) -> str:
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Este campo é obrigatório.")


def collect_fleet_data() -> dict:
    print("\n=== CADASTRO DA FROTA ===")
    period = read_required_text("Período (ex.: 10/2026): ")
    vehicle_count = read_positive_int("Quantidade de veículos: ")
    distance_km = read_nonnegative_float("Quilômetros percorridos pela frota: ")
    fuel_liters = read_nonnegative_float("Combustível consumido (litros): ")
    costs = {}
    for category, label in COST_CATEGORIES.items():
        costs[category] = read_nonnegative_float(f"Gasto com {label.lower()} (R$): ")
    return {
        "period": period,
        "vehicle_count": vehicle_count,
        "distance_km": distance_km,
        "fuel_consumption_liters": fuel_liters,
        "costs": costs,
    }
