class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # First, we put position and speed into a single array.
        # This is to sort them without changing the parity corresponding values
        # We put position first, because we sort by that
        # This is an O(n) operation in space and time
        p_t = []
        for i in range(len(position)):
            p_t.append([position[i], speed[i]])
        
        # Now we sort by position.
        # This is an O(n * log(n)) operation
        p_t.sort()
        p_t.reverse()
        # The closest to target car is in the last slot in the array
        # (top of stack)

        # now we find time to destination for each car
        # This is an O(n) time and space operation
        ttd = []
        for i in range(len(p_t)):
            ttd.append((target - p_t[i][0])/p_t[i][1])
        
        # Now, we know that anything with a shorted ttd behind us,
        # Is part of our fleet

        fleets = 0
        cur_ttd = 0
        for time in ttd:
            if time > cur_ttd:
                fleets += 1
                cur_ttd = time
            
        return fleets
