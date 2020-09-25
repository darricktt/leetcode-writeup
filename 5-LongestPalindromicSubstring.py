# Manacher 算法
class Solution:
    def expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left -2 ) // 2
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        start = 0
        end = 0
        right, j = -1, -1
        arm_list = []
        for i in range(len(s)):
            if i > right:
                arm_len = self.expand(s,i,i)
            else:
                min_arm_len = min(right - i, arm_list[2 * j - i])
                arm_len = self.expand(s,i - min_arm_len,i + min_arm_len)
            arm_list.append(arm_len)
            if i + arm_len > right:
                j = i
                right = i + arm_len

            if 2 * arm_len + 1 > end - start:
                start = i - arm_len
                end = i + arm_len
        return s[start+1:end+1:2]