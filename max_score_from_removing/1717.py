class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def calculate_score(s, first, second, score):
            stack = []
            total_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    total_score += score
                    stack.pop()
                else:
                    stack.append(char)
            return total_score, ''.join(stack)
        
        if x > y:
            score1, remaining = calculate_score(s, 'a', 'b', x)
            score2, _ = calculate_score(remaining, 'b', 'a', y)
        else:
            score1, remaining = calculate_score(s, 'b', 'a', y)
            score2, _ = calculate_score(remaining, 'a', 'b', x)
        
        return score1 + score2
