"""Formatação e apresentação do relatório."""
from src.calculations import (
    calculate_average_consumption,
    calculate_average_cost_per_vehicle,
    calculate_cost_distribution,
    calculate_cost_per_km,
    calculate_fuel_cost_per_km,
    calculate_total_cost,
    find_highest_cost_category,
)
from src.input import COST_CATEGORIES


def format_number(value: float, decimals: int = 2) -> str:
    return f"{value:,.{decimals}f}".replace(",", "_").replace(".", ",").replace("_", ".")


def format_currency(value: float) -> str:
    return f"R$ {format_number(value)}"


def build_report(data: dict) -> str:
    costs = data["costs"]
    total = calculate_total_cost(costs)
    distribution = calculate_cost_distribution(costs, total)
    maximum = find_highest_cost_category(costs)
    lines = [
        "=" * 55,
        "               FLEET FORCE | RELATÓRIO",
        "=" * 55,
        f"Período: {data['period']}",
        f"Veículos: {data['vehicle_count']}",
        f"Distância percorrida: {format_number(data['distance_km'])} km",
        "",
        "CUSTOS POR CATEGORIA",
        "-" * 55,
    ]
    for category, label in COST_CATEGORIES.items():
        lines.append(f"{label:<19} {format_currency(costs[category]):>19}  {format_number(distribution[category]):>7}%")
    lines.extend([
        "",
        "INDICADORES",
        "-" * 55,
        f"Custo total: {format_currency(total)}",
        f"Custo médio por veículo: {format_currency(calculate_average_cost_per_vehicle(total, data['vehicle_count']))}",
        f"Custo por quilômetro: {format_currency(calculate_cost_per_km(total, data['distance_km']))}/km",
    ])
    if maximum:
        category, value = maximum
        lines.append(f"Maior categoria de despesa: {COST_CATEGORIES[category]} ({format_currency(value)}, {format_number(distribution[category])}%)")
    else:
        lines.append("Maior categoria de despesa: nenhuma (todos os custos são zero)")
    liters = data["fuel_consumption_liters"]
    lines.append(
        f"Consumo médio: {format_number(calculate_average_consumption(data['distance_km'], liters))} km/L"
        if liters > 0 else "Consumo médio: indisponível (0 litro informado)"
    )
    lines.append(
        f"Custo de combustível por km: {format_currency(calculate_fuel_cost_per_km(costs['fuel'], data['distance_km']))}/km"
        if data["distance_km"] > 0 else "Custo de combustível por km: indisponível (0 km informado)"
    )
    lines.append("=" * 55)
    return "\n".join(lines)
