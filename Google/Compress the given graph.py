'''Compress the given graph

Starter code
class Node
{
    string key_;
    vector<Node*> out_edges;
};
class Solution
{
public:
    vector<Node*> compress_graph(vector<Node*> start_nodes)
    {
        return {};
    }
};
Input
//   f -           -> END
//      |         |
//      v         |
//      u -> l -> l -> e -> s -> t -> END
//      ^              |
//      |              |
//  d -                - > r -> END
Expected Output:
//   f -   -> END
//      | |
//      v |
//      ull -> e -> st -> END
//      ^      |
//      |      |
//   d -        -  r -> END
'''

from typing import List, Tuple
from collections import defaultdict, Counter

class Node:
    def __init__(self, val):
        self.val = val

END = object()

def compress_dag_graph(edges: List[Tuple[Node, Node]]):

    incoming = Counter()
    outgoing = Counter()
    graph = defaultdict(set)
    remap = {}
    for out, inc in edges:
        incoming[inc] += 1
        outgoing[out] += 1
        graph[out].add(inc)
        remap[inc] = inc
        remap[out] = out

    for out, inc in edges:
        out = remap[out]
        inc = remap[inc]
        if outgoing[out] == 1 and incoming[inc] == 1 and inc.val != END:
            print(f"merging {out.val} {inc.val}")
            out.val += inc.val

            for neighbor in graph[inc]:
                graph[out].add(neighbor)

            graph[out].remove(inc)
            outgoing[out] += outgoing[inc] - 1

            remap[inc] = out
            del graph[inc]
            del outgoing[inc]
            del incoming[inc]

    result = []
    for out in graph.keys():
        for inc in graph[out]:
            result.append([out, inc])
    return result


def unbuild(edges):
    ret = []
    for a, b in edges:
        b_val = b.val
        if b_val == END:
            b_val = "END"
        ret.append([a.val, b_val])
    return ret


f = Node("f")
u = Node("u")
l1 = Node("l")
l2 = Node("l")
d = Node("d")
e = Node("e")
s = Node("s")
t = Node("t")
r = Node("r")
end = Node(END)

input = [
    [f, u],
    [d, u],
    [u, l1],
    [l1, l2],
    [l2, end],
    [l2, e],
    [e, r],
    [r, end],
    [e, s],
    [s, t],
    [t, end]
]

g = compress_dag_graph(input)
print(unbuild(g))

'''Outputs:
merging u l
merging ul l
merging s t
[['f', 'ull'], ['d', 'ull'], ['ull', 'END'], ['ull', 'e'], ['e', 'st'], ['e', 'r'], ['r', 'END'], ['st', 'END']]'''