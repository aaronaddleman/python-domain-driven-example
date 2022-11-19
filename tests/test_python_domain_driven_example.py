from python_domain_driven_example import __version__
from python_domain_driven_example.model import Batch, OrderLine
from datetime import date


def test_version():
    assert __version__ == '0.1.0'


def make_batch_and_line(desc, qty, orderqty):
    batch = Batch("batch-001", desc, qty=qty, eta=date.today())
    line = OrderLine('order-ref', desc, orderqty)
    return batch, line


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, line = make_batch_and_line("ANGULAR-DESK", 20, 2)
    batch.allocate(line)
    assert batch.available_quantity == 18
