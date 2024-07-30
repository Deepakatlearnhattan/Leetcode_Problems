class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        s = str(x)
        # Check if the string is the same forwards and backwards
        return s == s[::-1]

# Example usage
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False
