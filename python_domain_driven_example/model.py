"""Define the model of the ordering process."""

from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
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

    def allocate(self, line: OrderLine):
        """Allocate an item to be ordered and upate the qty available."""
        self.available_quantity -= line.qty
