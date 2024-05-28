"""The Towers of Hanoi problem consists of three vertical rods, or towers, and N disks of different sizes, each with a hole in 
the center so that the rod can slide through it. The disks are originally stacked on one of the towers in order of descending size 
(i.e., the largest disc is on the bottom). The goal of the problem is to move all the disks to a different rod while complying with the 
following three rules:

Only one disk can be moved at a time.

Only the disk at the top of a stack may be moved.

A disk may not be placed on top of a smaller disk.

The following figure shows the steps of the solution to the Tower of Hanoi problem with three disks"""


def towers(n, from_tower, to_tower, alt_tower):
    if n != 0:
        towers(n-1, from_tower, alt_tower, to_tower)
        print(f"move disk {n} from tower {from_tower} to tower {to_tower}")
        towers(n-1, alt_tower, to_tower, from_tower)

towers(6, 1, 3,2)