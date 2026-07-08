class Solution:

    # ------------------------------------------------------------
    # Intuition
    #
    # The set of projects we can choose from keeps changing as our
    # capital increases.
    #
    # At any point, we need to answer two questions:
    #
    # 1. Which projects can I afford with my current capital?
    # 2. Among those affordable projects, which one gives the
    #    maximum profit?
    #
    # A single heap cannot efficiently answer both questions, so
    # we use two heaps.
    #
    # - Min Heap:
    #   Stores projects sorted by the capital required.
    #   This lets us quickly find every project that has become
    #   affordable.
    #
    # - Max Heap:
    #   Stores only the affordable projects sorted by profit.
    #   This lets us always choose the project with the highest
    #   profit.
    #
    # After completing the most profitable affordable project,
    # our capital increases, which may unlock even more projects.
    # We repeat this process at most k times.
    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # Explanation
    #
    # 1. Insert every project into a min heap as
    #    (required_capital, project_index).
    #
    # 2. Repeat at most k times:
    #
    #    a) Move every project whose required capital is less than
    #       or equal to our current capital into the max heap.
    #
    #    b) If no projects are affordable, stop because we cannot
    #       complete any more projects.
    #
    #    c) Otherwise, pick the project with the maximum profit,
    #       add its profit to our capital, and continue.
    #
    # Since every project is inserted and removed from each heap at
    # most once, the solution is efficient.
    #
    # Time Complexity : O((n + k) log n)
    # Space Complexity: O(n)
    # ------------------------------------------------------------

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        maxHeap = []

        # Store every project in a min heap based on
        # the capital required to start it.
        for i in range(0, len(capital)):
            heapq.heappush(minHeap, (capital[i], i))

        # We can complete at most k projects.
        for j in range(k):

            # Move every project that is currently affordable
            # into the max heap.
            while minHeap and minHeap[0][0] <= w:
                capital, index = heappop(minHeap)
                heapq.heappush(maxHeap, -profits[index])

            # If no affordable projects are available,
            # we cannot continue.
            if not maxHeap:
                break

            # Choose the most profitable affordable project
            # and increase our capital.
            w += (-heappop(maxHeap))

        return w
