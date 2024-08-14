from __future__ import annotations
import random

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class Node:
    """A node representing a piece in a 1-way linked list"""

    def __init__(self, label: str, next: Node | None):
        self.label = label
        self.next = next

    def __repr__(self):
        if self.next is not None:
            return f"Node({self.label} -> {self.next.label})"
        else:
            return f"Node({self.label} -> None)"


class Node2:
    """A node representing a piece in a 2-way linked list"""

    def __init__(self, label: str, prev: Node2 | None, next: Node2 | None):
        self.label = label
        self.next = next
        self.prev = prev

    def __repr__(self):
        if self.next is not None and self.prev is not None:
            return f"Node({self.prev.label} -> {self.label} -> {self.next.label})"
        elif self.next is None and self.prev is not None:
            return f"Node({self.prev.label} -> {self.label} -> None)"
        elif self.next is not None and self.prev is None:
            return f"Node(None -> {self.label} -> {self.next.label})"
        else:
            return f"Node(None -> {self.label} -> None)"


def simple_list(group_name):
    random.seed(group_name)
    length = random.randint(5, 15)
    curr = Node(label="".join(random.sample(ALPHABET, 4)), next=None)
    for _ in range(length - 1):
        curr = Node(label="".join(random.sample(ALPHABET, 4)), next=curr)
    return curr


def twoway_list(group_name):
    random.seed(group_name[::-1])
    length = random.randint(5, 15)
    curr = Node2(label="".join(random.sample(ALPHABET, 4)), prev=None, next=None)
    for _ in range(length - 1):
        prev = curr
        curr = Node2(label="".join(random.sample(ALPHABET, 4)), prev=None, next=curr)
        prev.prev = curr

    for _ in range(random.randint(1, length - 1)):
        if curr.next:
            curr = curr.next

    return curr


def cycle_list(group_name):
    random.seed(group_name[: len(group_name) // 2] + group_name[len(group_name) // 2 :])
    length = random.randint(5, 15)
    first = Node2(label="".join(random.sample(ALPHABET, 4)), prev=None, next=None)
    curr = first
    for _ in range(length - 1):
        prev = curr
        curr = Node2(label="".join(random.sample(ALPHABET, 4)), prev=None, next=curr)
        prev.prev = curr
    curr.prev = first
    first.next = curr

    for _ in range(random.randint(1, length - 1)):
        if curr.next:
            curr = curr.next

    return curr


if __name__ == "__main__":
    A = simple_list("Jedishere")
    print(A)
    B = twoway_list("Jedishere")
    print(B)
    C = cycle_list("Jedishere")
    print(C)
