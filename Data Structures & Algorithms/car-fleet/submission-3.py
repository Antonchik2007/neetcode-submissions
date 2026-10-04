class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        numTurns = []
        # 1, 7, 12
        for position, speed in cars:
            current_turns = (target-position) / speed

            if not numTurns or current_turns > numTurns[-1]:
                numTurns.append(current_turns)

        return len(numTurns)