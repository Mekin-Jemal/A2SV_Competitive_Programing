class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words = sorted(words, key=lambda w: int(w[-1]))
        words = [w[:-1] for w in words]
        return ' '.join(words)
