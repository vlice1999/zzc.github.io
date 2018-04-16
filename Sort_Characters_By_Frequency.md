## 题目描述
Given a string, sort it in decreasing order based on the frequency of characters.
```
Example 1: 
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2: 
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3: 
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```
## 题目分析
其实这个题不难理解，只要用map存放相应的Key-Value就可以了，但是难就难在排序上。这不像<a href="https://github.com/vlice1999/zzc.github.io/blob/master/Top_K_Frequent_Elements.md">Top_K_Frequent_Elements</a>
