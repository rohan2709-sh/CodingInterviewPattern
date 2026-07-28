class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # ----------------------------------------------------------
        # Approach:
        # 1. Use a min-heap to keep track of the smallest current
        #    element from both sorted arrays.
        #
        # 2. Each heap entry stores:
        #       (value, listIndex, elementIndex)
        #    where:
        #       listIndex = 0 -> nums1
        #       listIndex = 1 -> nums2
        #
        # 3. Initially, insert the first valid element from each array.
        #
        # 4. Repeatedly:
        #    - Pop the smallest element from the heap.
        #    - Append it to the output array.
        #    - Insert the next element from the same array (if one exists).
        #
        # 5. Continue until the heap becomes empty.
        #
        # 6. Copy the merged result back into nums1.
        #
        # Time Complexity:
        #   O((m + n) * log 2) = O(m + n)
        #
        # Space Complexity:
        #   O(m + n) for the output array.
        #   Heap size is at most 2 (O(1)).
        # ----------------------------------------------------------

        minHeap = []

        # Insert the first valid element of nums1 into the heap.
        if m > 0:
            heapq.heappush(minHeap, (nums1[0], 0, 0))

        # Insert the first element of nums2 into the heap.
        if n > 0:
            heapq.heappush(minHeap, (nums2[0], 1, 0))

        output = []

        # Process elements until both arrays are exhausted.
        while minHeap:

            # Remove the smallest available element.
            value, listIndex, elementIndex = heapq.heappop(minHeap)

            # Add it to the merged result.
            output.append(value)

            # If the element came from nums1,
            # push the next valid element from nums1.
            if listIndex == 0:
                if elementIndex + 1 < m:
                    heapq.heappush(
                        minHeap,
                        (nums1[elementIndex + 1], 0, elementIndex + 1)
                    )

            # If the element came from nums2,
            # push the next element from nums2.
            if listIndex == 1:
                if elementIndex + 1 < n:
                    heapq.heappush(
                        minHeap,
                        (nums2[elementIndex + 1], 1, elementIndex + 1)
                    )

        # Store the merged sorted array back into nums1.
        nums1[:] = output
