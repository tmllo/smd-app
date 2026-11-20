"""Reading transactions from a CSV file."""

import csv
from datetime import date
from decimal import Decimal
from pathlib import Path

from ledger.models import Transaction


def read_csv(path: Path) -> list[Transaction]:
    """Reads the CSV file and returns one Transaction per row."""
    with open(path, newline="") as f:
        return [
            Transaction(
                date=date.fromisoformat(row["date"]),
                account=row["account"],
                description=row["description"],
                category=row["category"],
                amount=Decimal(row["amount"]),
            )
            for row in csv.DictReader(f)
        ]
