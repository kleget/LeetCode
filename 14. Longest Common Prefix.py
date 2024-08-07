class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_len_world = len(min(strs, key=len))
        answer = 0
        if min_len_world == 0:
            return [""]

        elif min_len_world >= 1:
            for x in range(min_len_world):
                flag = True
                for t in range(len(strs)-1):
                    if strs[t][x] != strs[t + 1][x]:
                        flag = False
                        break

                if flag == True:
                    answer += 1
                else:
                    break
            return strs[0][:answer:]
