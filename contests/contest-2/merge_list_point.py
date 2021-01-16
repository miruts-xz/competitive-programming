def findMergeNode(head1, head2):
    h1_ptr = head1
    h2_ptr = head2
    while h1_ptr:
        while h2_ptr:
            if hash(h1_ptr) == hash(h2_ptr):
                return h1_ptr.data
            h2_ptr = h2_ptr.next
        h2_ptr = head2
        h1_ptr = h1_ptr.next
