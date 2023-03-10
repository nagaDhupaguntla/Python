class solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str1 = ''
        str2 = ''
        num = 0
        for i in s:
            if str1 != str2 or str1 == '' or str2 == '':
                if str1 == '' or (i not in str1 and i != str1[-1]) and len(str2) == 0:
                    str1 += i
                elif i not in str2:

                    str2 += i
        if str1 == str2:
            num = len(str1)
        if len(str1) > len(str2):
            num = len(str1)
        else:
            num = len(str2)

        return num

s=solution()
count1=s.lengthOfLongestSubstring('abcabcbb')
count2=s.lengthOfLongestSubstring('pwwkew')
count3=s.lengthOfLongestSubstring('bbbbb')
print(count1)
print(count2)
print(count3)

