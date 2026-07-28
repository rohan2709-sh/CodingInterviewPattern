class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int):

        # ----------------------------------------------------------
        # Approach:
        # 1. Since every row is sorted, treat each row as an
        #    individual sorted list.
        #
        # 2. Use a min-heap to keep track of the smallest current
        #    element from each row.
        #
        # 3. Each heap entry stores:
        #       (value, matrixIndex, elementIndex)
        #    where:
        #       matrixIndex  -> row number
        #       elementIndex -> column number within that row
        #
        # 4. Initially, insert the first element of every row into
        #    the heap.
        #
        # 5. Repeatedly:
        #    - Pop the smallest element from the heap.
        #    - Count how many elements have been removed.
        #    - If it is the kth element, return it.
        #    - Otherwise, insert the next element from the same row
        #      (if one exists).
        #
        # 6. Since only one element from each row is kept in the
        #    heap at any time, the heap size never exceeds n.
        #
        # Time Complexity:
        #   O(n + k log n)
        #   - O(n) to build the initial heap.
        #   - Up to k heap operations, each taking O(log n).
        #
        # Space Complexity:
        #   O(n) for the min-heap.
        # ----------------------------------------------------------

        minHeap = []

        listIndex = 0

        # Insert the first element from every row into the heap.
        for lst in matrix:
            heapq.heappush(minHeap, (lst[0], listIndex, 0))
            listIndex += 1

        numbers_checked = 0

        # Process elements in ascending order.
        while minHeap:

            # Remove the smallest available element.
            value, matrixIndex, elementIndex = heapq.heappop(minHeap)

            # Count how many smallest elements have been processed.
            numbers_checked += 1

            # If this is the kth smallest element, store and stop.
            if numbers_checked == k:
                output = value
                break

            # Insert the next element from the same row, if available.
            if elementIndex + 1 < len(matrix[matrixIndex]):
                heapq.heappush(
                    minHeap,
                    (
                        matrix[matrixIndex][elementIndex + 1],
                        matrixIndex,
                        elementIndex + 1,
                    ),
                )

        return output
