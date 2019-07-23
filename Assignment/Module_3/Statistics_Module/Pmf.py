from collections import Counter

def is_anagram(word1, word2):
    """
    Checks whether the words are anagrams.
    word1: string
    word2: string

    returns: boolean
    """
    return Counter(word1) == Counter(word2)

print(is_anagram('tachymetric', 'mccarthyite'))
print(is_anagram('banana', 'peach'))

class Multiset(Counter):
    """A multiset is a set where elements can appear more than once."""

    def is_subset(self, other):
        """Checks whether self is a subset of other.

        other: Multiset

        returns: boolean
        """
        for char, count in self.items():
            if other[char] < count:
                return False
        return True

    # map the <= operator to is_subset
    __le__ = is_subset

def can_spell(word, tiles):
    """Checks whether a set of tiles can spell a word.

    word: string
    tiles: string

    returns: boolean
    """
    return Multiset(word) <= Multiset(tiles)

print(can_spell('SYZYGY', 'AGSYYYZ'))

class Pmf(Counter):
    """A Counter with probabilities."""

    def normalize(self):
        """Normalizes the PMF so the probabilities add to 1."""
        total = float(sum(self.values()))
        for key in self:
            self[key] /= total

    def __add__(self, other):
        """Adds two distributions.

        The result is the distribution of sums of values from the
        two distributions.

        other: Pmf

        returns: new Pmf
        """
        pmf = Pmf()
        for key1, prob1 in self.items():
            for key2, prob2 in other.items():
                pmf[key1 + key2] += prob1 * prob2
        return pmf

    def __hash__(self):
        """Returns an integer hash value."""
        return id(self)

    def __eq__(self, other):
        return self is other

    def render(self):
        """Returns values and their probabilities, suitable for plotting."""
        return zip(*sorted(self.items()))

d6 = Pmf([1,2,3,4,5,6])
d6.normalize()
d6.name = 'one die'
print(d6)
