#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for el in tickets:
        hash_table_insert(hashtable, el.source, el.destination)

    first = hash_table_retrieve(hashtable, "NONE")
    route[0] = first
    index = 0
    insert = 1
    while insert < length:
        route[insert] = hash_table_retrieve(hashtable, route[index])
        index += 1
        insert += 1
    return route[:-1]

    # for i in range(length):

    print(route, "<<< route")
