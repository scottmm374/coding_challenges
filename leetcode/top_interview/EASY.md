# Easy 100 top interview Questions

<details>
<summary>STRINGS</summary>

<details>
<summary>Reverse String with O(1) SPACE</summary>

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

![Runtime](images/reverse_string_runtime.png)
![Space](images/reverse_string_space.png)

</details>
</details>

---

<details>
<summary>Valid Anagram</summary>

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

![Runtime](images/valid_anagram_runtime.png)
![Space](images/valid_anagram_space.png)

</details>
</details>

---

<details>
<summary>Reverse Integer</summary>

<br>

#### Instructions

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

![Runtime](images/reverse_int.png)
![Space](images/reverser_int.png)

</details>

</details>

---

<details>
<summary>View First Unique Character in a String</summary>

<br>

#### Instructions

    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

    Example 1:

    Input: s = "leetcode"
    Output: 0

    Example 2:

    Input: s = "loveleetcode"
    Output: 2

    Example 3:

    Input: s = "aabb"
    Output: -1

    Constraints:

        1 <= s.length <= 105
        s consists of only lowercase English letters.

<details>
<summary>Solution</summary>

```
class Solution:
    def firstUniqChar(self, s: str) -> int:

        char_dict = {}

        for x in range(len(s)):

            if s[x] not in char_dict:
                char_dict[s[x]] = 1

            else:
                char_dict[s[x]] +=1
        # print(char_dict)


        for x, y in char_dict.items():
            if y == 1:
                print(x)
                return s.index(x)

        return -1
```

</details>

<details>
<summary>Runtime and Space Results</summary>

![Runtime](images/first_unique_char_in_string.png)
![Space](images/first_unique_char_space.png)

</details>
</details>

---

<details>
<summary>Valid Palidrome</summary>

<br>

#### Instructions

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

<details>
<summary>Solution</summary>

```
class Solution:
    def isPalindrome(self, s: str) -> bool:

        only_chars = "".join(x for x in s if x.isalnum()).lower()
        reverse_str = only_chars[::-1]

        if only_chars == reverse_str:
            return True
        return False
```

</details>

<details>
<summary>Runtime and Space Results</summary>

![Runtime](images/valid_palidrome_runtime.png)
![Space](images/valid_palidrome-space.png)

</details>
</details>

## </details>

---

<details>
<summary>ARRAYS</summary>

<details>
<summary>Remove Duplicates from Sorted Array O(1)</summary>

    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
    }

    If all assertions pass, then your solution will be accepted.

    Example 1:

    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Example 2:

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Constraints:

        1 <= nums.length <= 3 * 104
        -100 <= nums[i] <= 100
        nums is sorted in non-decreasing order.

<br>

instructions

<details>
<summary>Solution</summary>

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        count_unique = 1
        unique = 0
        current = 1

        if len(nums) == 1:
            return 1

        while (current < len(nums)):

            if nums[current] == nums[unique]:
                nums.pop(current)

            else:
                unique = current
                count_unique += 1
                current = current + 1


        return count_unique
```

</details>

<details>
<summary>Runtime and Space Results</summary>

![Runtime](images/remove_Dups_sorted_array_runtime.png)
![Space](images/remove_Dups_sorted_array_space.png)

</details>
</details>

---

<details>

<!-- #### Title -->

<!-- <details>
<summary></summary>

<br>

instructions

<details>
<summary>Solution</summary>

```

```

</details>

<details>
<summary>Runtime and Space Results</summary>

![Runtime]
![Space]

</details>
</details>

<br> -->
