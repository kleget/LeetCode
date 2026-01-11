
def strStr(haystack: str, needle: str) -> int:
    first_symbol = needle[0]
    for i in range(len(haystack)):
        if haystack[i] == first_symbol:
            if haystack[i:i+len(needle)] == needle:
                print(i)
                break
    else:
        print(-1)
            


strStr(haystack="sadbutsad", needle="sad")