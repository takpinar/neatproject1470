from neat.neat_structures import Genome, Gene
from neat.neat_functions import delta
import pytest

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
genome3 = Genome([gene00, gene10, gene20], 0)
genome4 = Genome([gene01], 0)
genome5 = Genome([gene10, gene20], 0)


def test_delta0():
    val = delta(genome0, genome1, 1, 2, 3)
    assert val == pytest.approx(0.4 * 3)


def test_delta1():
    val = delta(genome2, genome3, 1, 2, 3)
    assert val == pytest.approx(1 * (1 / 3) + 2 * (1 / 3))


def test_delta2():
    val = delta(genome3, genome4, 1, 2, 3)
    assert val == pytest.approx(1 * (2 / 3) + 3 * 0.2)


def test_delta3():
    val = delta(genome1, genome5, 1, 2, 3)
    assert val == pytest.approx(1 * (1 / 2) + 2 * (1 / 2) + 3 * 0.6)
