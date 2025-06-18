

class Solution(object):
    @staticmethod
    def canConstruct(ransom_note, magazine):
        magazine_size = {}

        for char in magazine:
            if char in magazine_size:
                magazine_size[char] += 1
            else:
                magazine_size[char] = 1

        for char in ransom_note:
            if char not in magazine_size or magazine_size[char] == 0:
                return False
            magazine_size[char] -= 1

        return True