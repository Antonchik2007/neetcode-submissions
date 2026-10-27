class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        for letter in magazine:
            if letter not in mag_letters:
                mag_letters[letter] = 1
            else:
                mag_letters[letter] += 1
        for letter in ransomNote:
            if letter in mag_letters and mag_letters[letter] != 0:
                mag_letters[letter] -= 1
            else:
                return False
        return True