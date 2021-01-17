def findMergeNode(head1, head2):
    h1_ptr = head1
    st = set()
    while h1_ptr:
        st.add(h1_ptr)
    while head2:
        l1 = len(st)
        st.add(head2)
        l2 = len(st)
        if l1 == l2:
            return head2.data
        head2 = head2.next
