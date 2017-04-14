# qlearning

**qlearner.py** is a simplistic qlearning implementation based on numerous online tutorials

**worldqlearner.py** and **world.py** make up a more interesting implementation of that generates a semi-random graph of n nodes and uses qlearning to uncover the shortest path to the goal node given a random starting node

Example run of **worldqlearner.py** set to generate and solve a 15 node graph:
```bash
jjgraham@vps:~/dev/qlearning$ python3 worldqlearner.py
[<Node name: 0, neighbors: 4, goal: False,
 <Node name: 1, neighbors: 4, goal: False,
 <Node name: 2, neighbors: 2, goal: False,
 <Node name: 3, neighbors: 2, goal: True,
 <Node name: 4, neighbors: 2, goal: False,
 <Node name: 5, neighbors: 1, goal: False,
 <Node name: 6, neighbors: 2, goal: False,
 <Node name: 7, neighbors: 3, goal: False,
 <Node name: 8, neighbors: 4, goal: False,
 <Node name: 9, neighbors: 4, goal: False,
 <Node name: 10, neighbors: 1, goal: False,
 <Node name: 11, neighbors: 1, goal: False,
 <Node name: 12, neighbors: 1, goal: False,
 <Node name: 13, neighbors: 1, goal: False,
 <Node name: 14, neighbors: 4, goal: False]
Steps prior to learning
41
54
26
27
3
Steps after learning
2
2
2
2
2
[[0, 80, 0, 0, 51, 0, 0, 0, 64, 0, 0, 0, 0, 51, 0],
 [64, 0, 64, 100, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0],
 [0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51],
 [0, 80, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0],
 [64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51],
 [0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 64, 41, 0, 0, 0, 0, 0],
 [0, 0, 0, 100, 0, 64, 0, 0, 64, 0, 0, 0, 0, 0, 0],
 [64, 0, 0, 0, 0, 0, 51, 80, 0, 0, 51, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 51, 0, 0, 0, 0, 0, 33, 0, 51],
 [0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0],
 [0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0],
 [64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 64, 0, 51, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0]]
```
