import sys
from hspectral import generators
sys.path.insert(0, '../..')


def test_bare_controller():
    X, y = generators.generate_anomaly(random_state=1)
    assert(False)
