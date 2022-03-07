### <span style="color: SandyBrown;">Reverse String with O(1) SPACE</span>

<details>
<summary>View Reverse String</summary>

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

<br>

### <span style="color: SandyBrown;">Valid Anagram</span>

<details>
<summary>View Anagram</summary>

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
<br>

### <span style="color: SandyBrown;">Reverse Integer</span>

<details>
<summary>View Reverse Integer</summary>

<br>

        Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

        Example 1:

        Input: x = 123
        Output: 321

        Example 2:

        Input: x = -123
        Output: -321

        Example 3:

        Input: x = 120
        Output: 21

        Constraints:

            -2^31 <= x <= 2^31 - 1

<details>
<summary>Solution</summary>

```
class Solution:
    def reverse(self, x: int) -> int:
        j = math.pow(2, 31)

        if x < 0:
            negative_convert = abs(x)
            number = str(negative_convert)
            reversed_string = number[::-1]
            reversed_int = (int(reversed_string))
            if reversed_int > j:
                return 0
            return -abs(reversed_int)

        number = str(x)
        reversed_string = number[::-1]
        reversed_int = (int(reversed_string))
        if reversed_int > j:
                return 0
        return reversed_int

```

</details>

<details>
<summary>Space/Time Results</summary>

![Runtime](../../images/reverser_int.png)
![Space](../../images/reverse_int.png)

## </details>

</details>
