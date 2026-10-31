"""Testes unitários sem dependências externas: python -m unittest discover -s tests."""
import unittest

from src.calculations import (
    calculate_average_consumption,
    calculate_average_cost_per_vehicle,
    calculate_cost_distribution,
    calculate_cost_per_km,
    calculate_total_cost,
    find_highest_cost_category,
)
from src.report import build_report


class CalculationsTests(unittest.TestCase):
    def setUp(self):
        self.costs = {"fuel": 54000, "maintenance": 18000, "tolls": 12000, "fines": 3000, "taxes": 8000, "other": 2000}

    def test_total_and_unit_metrics(self):
        self.assertEqual(calculate_total_cost(self.costs), 97000)
        self.assertEqual(calculate_average_cost_per_vehicle(97000, 40), 2425)
        self.assertAlmostEqual(calculate_cost_per_km(97000, 85000), 1.14117647)
        self.assertAlmostEqual(calculate_average_consumption(85000, 9500), 8.94736842)

    def test_percentages_sum_to_100(self):
        distribution = calculate_cost_distribution(self.costs, 97000)
        self.assertAlmostEqual(sum(distribution.values()), 100)
        self.assertEqual(find_highest_cost_category(self.costs), ("fuel", 54000))

    def test_zero_division_and_zero_costs(self):
        self.assertEqual(calculate_cost_per_km(10, 0), 0)
        self.assertEqual(calculate_average_consumption(10, 0), 0)
        self.assertEqual(calculate_cost_distribution({"fuel": 0}, 0), {"fuel": 0})
        self.assertIsNone(find_highest_cost_category({"fuel": 0}))
        with self.assertRaises(ValueError):
            calculate_average_cost_per_vehicle(10, 0)

    def test_report(self):
        report = build_report({"period": "10/2026", "vehicle_count": 40, "distance_km": 85000, "fuel_consumption_liters": 9500, "costs": self.costs})
        self.assertIn("R$ 97.000,00", report)
        self.assertIn("Combustível", report)
        self.assertIn("55,67%", report)


if __name__ == "__main__":
    unittest.main()
