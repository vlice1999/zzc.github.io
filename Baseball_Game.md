# Description
You're now a baseball game point recorder. 
Given a list of strings, each string can be one of the 4 following types: 
Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.

Each round's operation is permanent and could have an impact on the round before and the round after. 
You need to return the sum of the points you could get in all the rounds. 
Example 1:
```
Input: ["5","2","C","D","+"]
Output: 30
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.  
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
```
Example 2:
```
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation: 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.  
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
```
# Solution
At first, I want to solve this problem by using four points, but I found it's impossible quickly. Then I used vector container (nums) to store every step's score. 


If the string is "C", delete the last number in "nums". 


If the string is "D", double the last number.


If the string is "+", the last number is the sum of the last numebr and the last second numeber.
# C++(4ms)
```cpp
class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> nums;
        for(int i = 0;i < ops.size();i ++){
            if(ops[i] == "C"){
                nums.pop_back();
            }
            else if(ops[i] == "D"){
                int n = nums.back();
                nums.push_back(2 * n);
            }
            else if(ops[i] == "+"){
                int n1 = nums.back();
                nums.pop_back();
                int n2 = nums.back();
                nums.push_back(n1);
                nums.push_back(n1 + n2);        
            }
            else {
                int n = std::stoi(ops[i]);
                nums.push_back(n);
            }
        }
        
        int re = 0;
        for(int i = 0;i < nums.size();i ++)
            re += nums[i];
        return re;
    }
};
```







