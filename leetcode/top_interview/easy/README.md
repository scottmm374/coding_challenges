<details>
<summary>Reverse String O(1) SPACE</summary>

#### Instructions

    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.



    Example 1:

    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

    Example 2:

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]



    Constraints:

        1 <= s.length <= 105
        s[i] is a printable ascii character.

<details>
<summary>Solution</summary>

```
        j = -1
        i = 0
        while(i < (len(s)//2)):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -=1
            i +=1

```

</details>

<details>
<summary>Runtime and Space Results</summary>

![Runtime](../../images/reverse_string_runtime.png)
![Space](../../images/reverse_string_space.png)

</details>
</details>

<details>
<summary>Valid Annogram</summary>

#### Instructions

        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



        Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true

        Example 2:

        Input: s = "rat", t = "car"
        Output: false



        Constraints:

            1 <= s.length, t.length <= 5 * 104
            s and t consist of lowercase English letters.

<details>
<summary>Solution</summary>

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_dict = {}

        if len(s) != len(t):
            return False

        for x in range(len(s)):
            if s[x] not in freq_dict:
                freq_dict[s[x]] = 1
            else:
                freq_dict[s[x]] += 1

        for j in range(len(t)):
            if t[j] in freq_dict:
                freq_dict[t[j]] -=1


        for key, val in freq_dict.items():
            if val != 0:
                return False

        return True
```

</details>

<details>
<summary>Space/Time Results</summary>

![Runtime](../../images/valid_anagram_runtime.png)
![Space](../../images/valid_anagram_space.png)

</details>

</details>
