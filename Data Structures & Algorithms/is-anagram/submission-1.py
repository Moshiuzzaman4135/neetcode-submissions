class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = {}
        frequency_t = {}

        if len(s) != len(t):
            return False
        
        # A single loop builds both dictionaries simultaneously
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Process string s
            if char_s in frequency_s:
                frequency_s[char_s] += 1
            else:
                frequency_s[char_s] = 1
                
            # Process string t
            if char_t in frequency_t:
                frequency_t[char_t] += 1
            else:
                frequency_t[char_t] = 1

        # Compare the final dictionary structures
        return frequency_s == frequency_t
