"""The data the ledger works with."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    """One movement of money in one account."""

    date: date
    account: str
    description: str
    category: str
    amount: Decimal
