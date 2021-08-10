import pytest

from .lc_113_path_sum_ii import Solution
from .lc_tree_utils import BinaryTreeBuilder


@pytest.mark.parametrize(
    "tree_list, target_sum, expected",
    [
        ([], 5, []),
        ([1, 2, 3], 5, []),
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        ),
    ],
)
def test_basic(tree_list, target_sum, expected):
    root = BinaryTreeBuilder().build(tree_list)
    result = Solution().pathSum(root, target_sum)
    assert len(result) == len(expected)
    assert set(tuple(r) for r in result) == set(tuple(e) for e in expected)
