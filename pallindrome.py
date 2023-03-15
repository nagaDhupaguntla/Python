# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#             reverseNum = 0
#             tempOriginal = x
#
#             while (tempOriginal > 0):
#                 lastDigit = tempOriginal % 10
#                 reverseNum = reverseNum * 10 + lastDigit
#                 tempOriginal = tempOriginal // 10
#
#             if (x == reverseNum):
#                 print(x)
#                 print(reverseNum)
#                 return 1
#             else:
#                  return 0
#
#
# sl=Solution()
# x=121
# sl.isPalindrome(x)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(len(s))
        if(len(s)>0):

            s2=s[0]+s[1]
            s3=''
            if(s[:2]==s[1]+s[0]):


                s2==s[0:2]
                s3=s[0:2]

            for i in range(2,len(s)):
                s2=s2+s[i]
                y=i
                z = (len(s) - y)
                for j in range(i):

                    n=-(len(s)-j)-1
                    #print(z)
                    s4=s[-z:n:-1]

                    y = y - 1
                    if (s4==s4[::-1]):
                        s3=s4
                        break
        else:
            s3=s
        print(s3)
        return s3


sl=Solution()
sl.longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn")
s='abb'
#print(len(s))
print(s[-1:-3:-1])