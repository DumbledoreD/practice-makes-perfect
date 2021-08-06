import random

import pytest

from .lc_877_stone_game import Solution


@pytest.mark.parametrize(
    "piles, expected",
    [
        ([5], True),
        ([5, 6], True),
        ([5, 6, 5], True),
        ([5, 3, 4, 5], True),
    ],
)
def test_basic(piles, expected):
    assert Solution().stoneGame(piles) == expected


def generate_piles():
    piles = random.choices(range(1, 100), k=random.randrange(1, 20))
    if sum(piles) % 2 == 0:
        piles[-1] += 1
    return piles


@pytest.mark.skip(
    reason="For showing that cheat solution only holds when len(piles) is even"
)
@pytest.mark.parametrize(
    "piles, expected",
    [(generate_piles(), True) for _ in range(20)],
)
def test_stress(piles, expected):
    assert Solution().stoneGame(piles) == expected
