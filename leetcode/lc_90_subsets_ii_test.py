import pytest

from .lc_90_subsets_ii import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        pytest.param([0], [[], [0]]),
    ],
)
def test_basic(nums, expected):
    result = Solution().subsetsWithDup(nums)
    assert len(result) == len(expected)
    assert set(tuple(r) for r in result) == set(tuple(e) for e in expected)
