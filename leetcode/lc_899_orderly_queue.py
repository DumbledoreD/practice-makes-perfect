# Thought of greedy, perform the operation that decreases the lexicographical order.
# Can prove it's not a safe move, consider "aaacb".

# Note that for k>= 2, the string can be ordered in any way I like. Keep rotating till
# desired location, then insert. Hence the solution.
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return "".join(sorted(s))
