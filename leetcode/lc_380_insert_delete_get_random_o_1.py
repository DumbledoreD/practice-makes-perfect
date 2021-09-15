import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = {}  # For O(1) insert and remove
        self._list = []  # For O(1) random access

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the
        specified element.
        """
        if val in self._dict:
            return False

        self._dict[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified
        element.
        """
        if val not in self._dict:
            return False

        val_i = self._dict[val]

        # Move val to the end of the list to pop
        self._list[val_i], self._list[-1] = self._list[-1], self._list[val_i]
        # Update previous last val's index
        self._dict[self._list[val_i]] = val_i

        # Remove val from list and dict
        del self._dict[val]
        self._list.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self._list)
