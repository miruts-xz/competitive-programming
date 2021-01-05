class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_vals = []
        node = l1
        while node:
            l1_vals.append(str(node.val))
            node = node.next
        l2_vals = []
        node = l2
        while node:
            l2_vals.append(str(node.val))
            node = node.next
        l1_vals.reverse()
        l2_vals.reverse()
        l1_str = ''.join(l1_vals)
        l2_str = ''.join(l2_vals)
        int_sum = int(l1_str) + int(l2_str)
        sum_str = str(int_sum)
        node_list = []
        for i in range(len(sum_str)):
            nd = ListNode(int(sum_str[i]))
            if i > 0:
                nd.next = node_list[i - 1]
            node_list.append(nd)

        return node_list.pop()
