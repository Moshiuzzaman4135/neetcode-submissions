class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = {}
        frequency_t = {}

        # Quick check: if lengths aren't equal, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Build frequency dictionary for string s
        for i in range(len(s)):
            letter = s[i]
            if letter in frequency_s:      # Check if key already exists in dictionary
                frequency_s[letter] += 1   # Increase count
            else:
                frequency_s[letter] = 1    # Otherwise put 1

        # Build frequency dictionary for string t
        for i in range(len(t)):
            letter = t[i]
            if letter in frequency_t:      # Check if key already exists in dictionary
                frequency_t[letter] += 1   # Increase count
            else:
                frequency_t[letter] = 1    # Otherwise put 1

        # Direct comparison of the two dictionaries
        return frequency_s == frequency_t