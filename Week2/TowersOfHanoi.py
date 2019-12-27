def print_move(fr, to):
    print("move from " + str(fr) + " to " + str(to))


def towers(n, fr, to, spare):
    """
    :param n: int, number of disks to be moved
    :param fr: str, pillar where is the original disk position
    :param to: str, pillar where the disk is moved
    :param spare: str, spare pillar
    :return: invokes print_move function
    """
    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)


print(towers(4, "left", "middle", "right"))
