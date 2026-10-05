class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        speedMin, speedMax = 1, max(piles)
        prevSpeed = speedMax

        while speedMin<=speedMax:
            totalTime = 0
            midSpeed = (speedMax+speedMin) // 2

            #eat all the piles
            for pile in piles:
                totalTime = totalTime + math.ceil(pile / midSpeed)
            #if matches done
            if totalTime <= h:
                prevSpeed = midSpeed
                speedMax = midSpeed - 1
            else:
                speedMin = midSpeed + 1
            
        return prevSpeed


        