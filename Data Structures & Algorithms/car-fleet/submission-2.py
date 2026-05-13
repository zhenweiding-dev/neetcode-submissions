class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        i position:[int] speed:[int]; both len = n; 
            i is ith car(position an speed), miles/ miles/per hour
            destination at position[target]
            cannot pass: after reach same position, min(speeds)
            fleet: set(), cars at same position; single car is also a fleet
            need join before or at the moment reaches the destination
        o count(distinct car fleets)
        c n in [1,1000]; target[1,1000] and position[i]<target; speed(0, 100]
        e
        as the car closer to target most likely keep their speed,
        we can use a stack to track from the rightmost car
        if next car can reach it before the target, then they will join the same fleet
        if cannot, the next car will arrive at its own speed, and have a new time longer than first
        for the rest, if it's time short than any one before it, they will join the same fleet
        """
        n = len(position)
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda car : car[0], reverse = True)

        stack = []
        for i in range(n):
            arrive_time = (target - cars[i][0])/cars[i][1]
            if not stack or arrive_time > stack[-1]:
                stack.append(arrive_time)
        return len(stack)
        