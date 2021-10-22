from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        # Bucket sort O(n), counter.most_common() O(nlogn).
        max_freq = max(counter.values())

        buckets = [[] for _ in range(max_freq + 1)]

        for character, freq in counter.items():
            buckets[freq].append(character)

        return "".join(
            c * (max_freq - freq_offset)
            for freq_offset, characters in enumerate(reversed(buckets))
            for c in characters
        )
