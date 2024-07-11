class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = collections.deque()
        
        for log in logs:
            if log == "./":
                continue
            elif log == "../" and len(stack) != 0:
                stack.pop()
            elif log != "../":
                stack.append(log)
        return len(stack)
