class Solution:
    def reverseVowels(self, s: str) -> str:
        c = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(c) - 1

        while left < right:
            while left < right and c[left] not in vowels:
                left += 1
            while left < right and c[right] not in vowels:
                right -= 1

            c[left], c[right] = c[right], c[left]
            left += 1
            right -= 1

        return "".join(c)