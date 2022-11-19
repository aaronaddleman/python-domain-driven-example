"""Define the model of the ordering process."""

from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass(frozen=True)
class OrderLine:
    """Define an OrderLine."""

    orderid: str
    sku: str
    qty: int


class Batch:
    """Define a batch of OrderLines."""

    def __init__(
            self,
            ref: str,
            sku: str,
            qty: int,
            eta: Optional[date]
    ):
        """Create a batch item."""
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty
        self._purchased_quantity = qty
        self._allocations = set()

    def __repr__(self):
        return f"<Batch {self.reference}>"

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(tuple(self.reference))

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: OrderLine):
        """Allocate an item to be ordered and upate the qty available."""
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        """Remove a line."""
        if line in self._allocations:
            self._allocations.remote(line)

    @property
    def allocated_quantity(self) -> int:
        """Return the sum of qty for all of the allocations."""
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        """Return the quantity left."""
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        """Return true if the item can be allocated."""
        return self.sku == line.sku and self.available_quantity >= line.qty
