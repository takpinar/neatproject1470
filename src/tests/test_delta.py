from neat.neat_structures import Genome, Gene
from neat.neat_functions import delta

gene00 = Gene(
    n_in=0,
    n_out=2,
    w=.3,
    ino=0,
    active=True
)

gene01 = Gene(
    n_in=0,
    n_out=2,
    w=.5,
    ino=0,
    active=True
)

gene10 = Gene(
    n_in=1,
    n_out=2,
    w=.2,
    ino=1,
    active=True
)

gene11 = Gene(
    n_in=1,
    n_out=2,
    w=.8,
    ino=1,
    active=True
)

gene20 = Gene(
    n_in=2,
    n_out=3,
    w=.5,
    ino=3,
    active=True
)

genome0 = Genome([gene00, gene10], 0)
genome1 = Genome([gene01, gene11], 0)
genome2 = Genome([gene10], 0)
genome3 = Genome([gene00, gene20], 0)
genome4 = Genome([gene01], 0)
genome5 = Genome([gene10, gene20], 0)


def test_delta0():
    val = delta(1, 2, 3, genome0, genome1)
    assert round(val, 2) == round(0.4 * 3, 2)


def test_delta1():
    val = delta(1, 2, 3, genome2, genome3)
    assert round(val, 2) == round((1 * (1 / 2) + 2 * (2 / 2)), 2)


def test_delta2():
    val = delta(1, 2, 3, genome3, genome4)
    assert round(val, 2) == round(1 * (1 / 2) + 3 * 0.2, 2)


def test_delta3():
    val = delta(1, 2, 3, genome1, genome5)
    assert round(val, 2) == round(1 * (1 / 2) + 2 * (1 / 2) + 3 * 0.6, 2)
