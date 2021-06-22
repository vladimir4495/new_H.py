
from typing import Tuple, List

FIELD = 7
RES = None

class Colobok:
    def __init__(self, x, y, papa):
        self.papa = papa
        self.y = y
        self.x = x

    def __repr__(self):
        if self.papa:
            return f"{self.papa}-> ({self.x}, {self.y})"
        return f"({self.x}, {self.y})"

def move_horse(a1, a2, b1, b2, visited: List[Tuple] = None):
    if not (0 <= a1 <= FIELD and 0 <= a2 <= FIELD):
        raise ValueError
    global RES
    visited = visited or []
    visited.append((a1, a2))

    if RES is not None and len(visited) + 1 > len(RES):
        return

    var = posible_move(a1, a2)
    if (b1, b2) in var:
        visited.append((b1, b2))
        RES = visited
        return
    var = list(set(var) - set(visited))

    for pos in var:
        move_horse(*pos, b1, b2, visited[:])


def move(a1, a2, b1, b2):
    q = [Colobok(a1, a2, None)]
    while q:
        q0:Colobok = q.pop(0)
        if (q0.x, q0.y) == (b1, b2):
            return q0


        q_pos = posible_move2(q0)
        q.extend(q_pos)


def posible_move2(c: Colobok) -> List[Colobok]:
    return [Colobok(x, y, c) for x,y in posible_move(c.x, c.y)]

def posible_move(a1, a2) -> List[Tuple]:
    return [cord for cord in
            [(a1 + 2, a2 + 1), (a1 - 2, a2 + 1), (a1 + 2, a2 - 1), (a1 - 2, a2 - 1),
             (a1 + 1, a2 + 2), (a1 + 1, a2 - 2), (a1 - 1, a2 + 2), (a1 - 1, a2 - 2)]
            if 0 <= cord[0] <= FIELD and 0 <= cord[1] <= FIELD]


if __name__ == '__main__':
    res = move_horse(0, 0, 7, 7)
    print(RES)
    print(move(0, 0, 7, 7))