from listlib import simple_list, twoway_list, cycle_list


GROUP_NAME_MASHUP = "<ENTER A MASHUP OF ALL YOUR GROUP'S NAMES IN HERE>"


def simple_num_links(simple_node):
    """Computes the number of nodes in a one-way linked list

    Args:
        simple_node (Node): The starting node of the linked list
    Returns:
        (int): the number of nodes in the linked list
    """


def twoway_num_links(two_node):
    """Computes the number of nodes in a two-way linked list

    Args:
        two_node (Node2): A node _somewhere_ in the list
    Returns:
        (int): the number of nodes in the linked list
    """


def cycle_num_links(cy_node):
    """Computes the number of unique nodes in a two-way cyclic linked list

    Args:
        cy_node (Node2): A node _somewhere_ in the list
    Returns:
        (int): the number of nodes in the linked list
    """


if __name__ == "__main__":
    A = simple_list(GROUP_NAME_MASHUP)
    print(f"There are {simple_num_links(A)} links in the simple linked list.")
    # B = twoway_list(GROUP_NAME_MASHUP)
    # print(f"There are {twoway_num_links(B)} links in the twoway linked list.")
    # C = cycle_list(GROUP_NAME_MASHUP)
    # print(f"There are {cycle_num_links(C)} unique links in the cycling linking list.")
