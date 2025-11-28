class Solution:
    def findSubString(self, s):
        n = len(s)
        unique = len(set(s))   # number of distinct characters

        freq = {}
        count = 0
        left = 0
        min_len = float('inf')

        for right in range(n):
            # include current char
            freq[s[right]] = freq.get(s[right], 0) + 1

            # a new unique char added
            if freq[s[right]] == 1:
                count += 1

            # if window contains all unique chars --> shrink it
            while count == unique:
                min_len = min(min_len, right - left + 1)

                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    count -= 1
                left += 1

        return min_len
