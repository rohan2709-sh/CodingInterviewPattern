# ------------------------------------------------------------
# STEP-BY-STEP EXPLANATION
# ------------------------------------------------------------
#
# PROBLEM IDEA:
# We need to check if at any point in time (location),
# the number of passengers in the car exceeds capacity.
#
# ------------------------------------------------------------
#
# STEP 1: DIFFERENCE ARRAY (changes[])
#
# We do NOT simulate each trip separately.
# Instead, we record only when passengers enter or leave.
#
# changes[i] means:
#   net change in passengers at location i
#
# ------------------------------------------------------------
#
# STEP 2: CONVERT EACH TRIP INTO EVENTS
#
# trip = [numPassengers, from, to]
#
# At "from"  → passengers enter the car  (+)
# At "to"    → passengers leave the car  (-)
#
# Example:
#   [2, 1, 5]
#   changes[1] += 2
#   changes[5] -= 2
#
# ------------------------------------------------------------
#
# STEP 3: PREFIX SUM (SIMULATE MOVEMENT EAST)
#
# We move from location 0 → 1000
# and maintain running passenger count:
#
# currentCapacity += changes[i]
#
# This gives us how many passengers are currently in the car.
#
# ------------------------------------------------------------
#
# STEP 4: CAPACITY CHECK
#
# At every location:
#   if currentCapacity > capacity:
#       return False
#
# Because car cannot exceed seating limit at any point.
#
# ------------------------------------------------------------
#
# FINAL RESULT:
# If we never exceed capacity → return True
#
# ------------------------------------------------------------
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0] * 1001
        currentCapacity = 0
        for i in range(0, len(trips)):
            changes[trips[i][1]] += trips[i][0]
            changes[trips[i][2]] -= trips[i][0]
        
        for i in range(1001):
            currentCapacity += changes[i]
            if currentCapacity > capacity:
                return False
        return True
