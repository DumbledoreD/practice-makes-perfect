from collections import defaultdict, deque
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)

            for subdomain in self._get_subdomains(domain):
                counter[subdomain] += count

        return (f"{v} {k}" for k, v in counter.items())

    def _get_subdomains(self, domain):
        segments = deque(domain.split("."))
        subdomain = ""

        while segments:
            subdomain = ".".join(segments)
            segments.popleft()
            yield subdomain
