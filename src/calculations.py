"""Cálculos determinísticos da Sprint 1."""


def calculate_total_cost(costs: dict[str, float]) -> float:
    return sum(costs.values())


def calculate_average_cost_per_vehicle(total_cost: float, vehicle_count: int) -> float:
    if vehicle_count <= 0:
        raise ValueError("A quantidade de veículos deve ser maior que zero.")
    return total_cost / vehicle_count


def calculate_cost_per_km(total_cost: float, distance_km: float) -> float:
    return total_cost / distance_km if distance_km > 0 else 0.0


def calculate_cost_distribution(costs: dict[str, float], total_cost: float) -> dict[str, float]:
    if total_cost <= 0:
        return {category: 0.0 for category in costs}
    return {category: cost / total_cost * 100 for category, cost in costs.items()}


def find_highest_cost_category(costs: dict[str, float]) -> tuple[str, float] | None:
    if not costs or all(cost == 0 for cost in costs.values()):
        return None
    return max(costs.items(), key=lambda item: item[1])


def calculate_average_consumption(distance_km: float, liters: float) -> float:
    return distance_km / liters if liters > 0 else 0.0


def calculate_fuel_cost_per_km(fuel_cost: float, distance_km: float) -> float:
    return fuel_cost / distance_km if distance_km > 0 else 0.0
