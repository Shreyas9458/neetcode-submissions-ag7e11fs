class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, sp in cars:
            timeRequired = (target - pos)/sp
            if not stack or timeRequired > stack[-1]:
                stack.append(timeRequired)
        return len(stack)
        