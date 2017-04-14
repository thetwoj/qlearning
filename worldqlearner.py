#!/usr/bin/python3

import random
from world import gen_nodes
import pprint
from operator import itemgetter

pp = pprint.PrettyPrinter(width=200)

GAMMA = .8
NODE_COUNT = 50


class WorldLearner:
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def best_action(self, state):
        state_qs = [(x, self.q[state][x]) for x in range(0, len(self.q)) if self.r[state][x] > -1]
        best_state, best_q = max(state_qs, key=itemgetter(1))
        if len([x[1] for x in state_qs if x[1] == best_q]) > 1:
            best_state = random.choice([state for state, q in state_qs if q == best_q])
        return best_state

    def state_q_values(self, state):
        return [self.q[state][x] for x in range(0, len(self.q)) if self.r[state][x] > -1]

    def set_q(self, state, next_state):
        self.q[state][next_state] = self.r[state][next_state] + GAMMA * max(self.state_q_values(next_state))
        return


def main():
    nodes = gen_nodes(NODE_COUNT)

    # Initialize empty q
    q = [[0 for _ in range(0, len(nodes))] for _ in range(0, len(nodes))]
    r = [[-1 for _ in range(0, len(nodes))] for _ in range(0, len(nodes))]
    for index, node in enumerate(nodes):
        for neighbor in node.neighbors:
            if neighbor.goal_node:
                r[node.name][neighbor.name] = 100
                continue
            r[node.name][neighbor.name] = 0

    wl = WorldLearner(q, r)

    print('Steps prior to learning')
    for x in range(0, 5):
        steps = 0
        initial_state = nodes[0].name
        current_state = initial_state

        while True:
            next_state = wl.best_action(current_state)
            current_state = next_state
            steps += 1

            if nodes[current_state].goal_node:
                print(steps)
                break

    for x in range(0, 2500):
        initial_state = nodes[random.randint(0, len(nodes)-1)].name
        current_state = initial_state
        # print('current {}'.format(current_state))

        while True:
            next_state = random.choice([neighbor.name for neighbor in nodes[current_state].neighbors])
            # print('next {}'.format(next_state))

            wl.set_q(current_state, next_state)
            current_state = next_state

            if nodes[current_state].goal_node:
                break

        # pprint(q)

    print('Steps after learning')
    for x in range(0, 5):
        steps = 0
        initial_state = nodes[0].name
        current_state = initial_state

        while True:
            next_state = wl.best_action(current_state)
            current_state = next_state
            steps += 1

            if nodes[current_state].goal_node:
                print(steps)
                break

    max_q = max([max(x) for x in wl.q])
    for index, state in enumerate(wl.q):
        for action_index, action in enumerate(state):
            q[index][action_index] = round((action / max_q) * 100)

    pp.pprint(wl.q)


if __name__ == '__main__':
    main()
