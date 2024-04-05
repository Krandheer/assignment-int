class Solution:
    """Remove duplicates from a linked list"""
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
