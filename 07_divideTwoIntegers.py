class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if divisor == 0:
            return 2**31 - 1  
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > -(2**31):  
                return -dividend
            else:
                return 2**31 - 1

        positive = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        if not positive:
            quotient = -quotient
    
        return min(max(-2**31, quotient), 2**31 - 1)

# Example usage:
solution = Solution()
print(solution.divide(10, 3))  # Output: 3
print(solution.divide(7, -3))  # Output: -2
print(solution.divide(0, 1))  # Output: 0
print(solution.divide(1, 1))  # Output: 1
