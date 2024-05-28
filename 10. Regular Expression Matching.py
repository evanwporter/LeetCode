class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        arr = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        arr[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                arr[0][j] = arr[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    arr[i][j] = arr[i - 1][j - 1]
                elif p[j - 1] == '*':
                    arr[i][j] = arr[i][j - 2] or (arr[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return arr[len(s)][len(p)]

