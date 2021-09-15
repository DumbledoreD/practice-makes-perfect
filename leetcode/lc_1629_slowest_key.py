from typing import List


class Solution:
    def slowestKey(self, release_times: List[int], keys_pressed: str) -> str:
        prev_release_time = 0
        max_duration, max_duration_key = 0, ""

        for release_time, key in zip(release_times, keys_pressed):
            duration = release_time - prev_release_time

            if duration >= max_duration:
                max_duration_key = (
                    max(max_duration_key, key) if max_duration == duration else key
                )
                max_duration = duration

            prev_release_time = release_time

        return max_duration_key
