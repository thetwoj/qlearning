#!/usr/bin/python3

import random
from pprint import pprint
from operator import itemgetter

r = [
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100],
]

q = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

gamma = .8


def best_action(state):
    return max(((x, q[state][x]) for x in range(0, len(q))), key=itemgetter(1))[0]


def action_options(state):
    return [x for x in range(0, len(q)) if r[state][x] > -1]


def state_q_values(state):
    return [q[state][x] for x in range(0, len(q)) if r[state][x] > -1]


def set_q(state, next_state):
    q[state][next_state] = r[state][next_state] + gamma * max(state_q_values(next_state))
    return


def main():
    for x in range(0, 10000):
        initial_state = random .randint(0, 5)
        current_state = initial_state
        # print('current {}'.format(current_state))

        while True:
            next_state = random.choice(action_options(current_state))
            # print('next {}'.format(next_state))

            set_q(current_state, next_state)
            current_state = next_state

            if current_state is 5:
                break

        # pprint(q)

    max_q = max([max(x) for x in q])
    for index, state in enumerate(q):
        for aindex, action in enumerate(state):
            q[index][aindex] = round((action / max_q) * 100)

    pprint(q)


if __name__ == '__main__':
    main()
