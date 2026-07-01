# ─────────────────────────────────────────────────
# INTUITION
# ─────────────────────────────────────────────────
# A linked list is a chain of nodes where each node
# points forward. To reverse it, we need every node
# to point BACKWARD instead.
#
# We walk through the list once, and at each node we
# "redirect" its .next pointer to the previous node.
# The trick is that we can't afford to lose our grip
# on the rest of the list while doing this — so we
# save curr.next in `temp` before overwriting it.
#
# POINTER STATE at each step:
#   prev → the already-reversed portion (starts as None)
#   curr → the node we're currently reversing
#   temp → saves curr.next so we don't lose the rest
#
# EXAMPLE:  1 → 2 → 3 → None
#
#   Step 1: temp=2→3, 1→None,  prev=1, curr=2
#   Step 2: temp=3→None, 2→1, prev=2, curr=3
#   Step 3: temp=None,  3→2,  prev=3, curr=None
#
#   Loop ends. prev points to 3 (new head). ✓
#
# TIME:  O(n) — single pass
# SPACE: O(1) — no extra data structures
# ─────────────────────────────────────────────────

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next   # save the rest of the list before we break the link
            curr.next = prev   # reverse the pointer
            prev = curr        # advance prev
            curr = temp        # advance curr (using saved reference)

        return prev            # prev is now the new head
