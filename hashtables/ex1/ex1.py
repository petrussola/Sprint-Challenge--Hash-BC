#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):
        difference = limit - weights[i]
        index = hash_table_retrieve(ht, difference)
        if index == None:
            hash_table_insert(ht, weights[i], i)
        else:
            if i > index:
                return (i, index)
            else:
                return (index, i)
    # for i in range(length):
    #     if hash_table_retrieve(ht, weights[i]) == None:
    #         hash_table_insert(ht, weights[i], i)

    # for i in range(len(weights)):
    #     difference = limit - weights[i]
    #     if hash_table_retrieve(ht, difference) != None:
    #         index = hash_table_retrieve(ht, difference)

    #         if i >= index:
    #             return (i, index)
    #         else:
    #             return (index, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
