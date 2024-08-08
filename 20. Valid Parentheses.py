# I think this is not the best solution, but it works

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(list(s)) >=2 and len(list(s)) % 2 == 0:
            while ('[]' in s) or ('{}' in s) or ('()' in s):
                s = s.replace('{}', '').replace('()', '').replace('[]', '')
            a = list(s)
            while len(list(a)) != 0:
                flag = True
                for x in range(0, len(list(a)), 1):
                    if flag == True:
                        for y in range(len(list(a))-1, 0 - 1, -1):
                            if x != y and x < y:
                                if a[x]+a[y] in ('()', '{}', '[]'):
                                    if len(a[x+1:y:]) % 2 == 0:
                                        del a[y]
                                        del a[x]
                                        flag = False
                                        break
                                    else:
                                        return False
                    else:
                        break
                else:
                    return False
            if len(list(a)) == 0:
                return True
        else:
            return False


a = Solution()
print(a.isValid("([[]][([][])({})]())"))  # True: correct answer
