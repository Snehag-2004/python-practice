
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []
    count = 0

    # Insert the first node of each list into heap
    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, count, node))
            count += 1

    dummy = ListNode()
    current = dummy

    while heap:
        val, index, node = heapq.heappop(heap)

        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(
                heap, (node.next.val, count, node.next)
            )
            count += 1

    return dummy.next


# Function to create linked list
def createList(arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Function to print linked list
def printList(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


# Example 1
lists1 = [
    createList([1, 4, 5]),
    createList([1, 3, 4]),
    createList([2, 6])
]

print("Merged List:")
printList(mergeKLists(lists1))


# Example 2
lists2 = [
    createList([4, 5]),
    createList([1, 6])
]

print("Merged List:")
printList(mergeKLists(lists2))
