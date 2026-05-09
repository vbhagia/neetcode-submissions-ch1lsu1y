class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We're going to put position and speed into a single array
        # O(n) time and space
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        # Now sort this array by position descending
        cars = sorted(cars, reverse=True)
        print()
        # O(n log(n)) time, no space because sorting and reversing is in place
        
        # Calculate time to destination, then number of fleets
        # These are both O(n) operations, which in total require O(n) space
        ttd = []
        for [position, speed] in cars:
            ttd.append((target - position)/speed)
        
        curr_time = ttd[0]
        fleets = 1
        for time in ttd:
            if time > curr_time:
                # new fleet
                curr_time = time
                fleets += 1
    
        return fleets