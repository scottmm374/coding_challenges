def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = -1
        i = 0
        while(i < (len(s)//2)):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -=1
            i +=1


# Runtime: 362 ms 17.25%
# Memory Usage: 18.3 MB 90.70%