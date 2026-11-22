"""Calculations on transactions. No printing, no files: data in, data out."""

from collections import defaultdict
from collections.abc import Callable, Iterable
from decimal import Decimal

from ledger.models import Transaction

TRANSFER = "transfer"


def totals_by(
    transactions: Iterable[Transaction], key: Callable[[Transaction], str]
) -> dict[str, Decimal]:
    """Adds up the amounts for each value of `key` (account, category...)."""
    totals: dict[str, Decimal] = defaultdict(Decimal)
    for t in transactions:
        totals[key(t)] += t.amount
    return dict(totals)


def is_spending(t: Transaction) -> bool:
    """True for money going out, except transfers between your own accounts."""
    return t.amount < 0 and t.category != TRANSFER


def balances(transactions: Iterable[Transaction]) -> dict[str, Decimal]:
    """The total of each account, sorted by account name."""
    return dict(sorted(totals_by(transactions, lambda t: t.account).items()))


def spending_by_category(transactions: Iterable[Transaction]) -> dict[str, Decimal]:
    """The spending of each category (negative totals), biggest first."""
    spending = [t for t in transactions if is_spending(t)]
    totals = totals_by(spending, lambda t: t.category)
    return dict(sorted(totals.items(), key=lambda item: item[1]))


def net_by_month(transactions: Iterable[Transaction]) -> dict[str, Decimal]:
    """The total of each month (YYYY-MM), transfers included, sorted by month."""
    totals = totals_by(transactions, lambda t: t.date.strftime("%Y-%m"))
    return dict(sorted(totals.items()))
