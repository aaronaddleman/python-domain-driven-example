from python_domain_driven_example import __version__
from python_domain_driven_example.model import Batch, OrderLine
from datetime import date


def test_version():
    assert __version__ == '0.1.0'


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(line)
    assert batch.available_quantity == 18
