# does not consider double edges
def make_edge_map(nodes,edges):
    edge_map = dict([(i,dict()) for i in nodes])
    for a,b in edges:
        edge_map[a][b] = 1
    return edge_map


def all_paths_from(current,prefix,seen,edge_map):
    paths = []
    for k in edge_map[current]:
        if k in seen:
            continue
        new_prefix = prefix + [k]
        paths.append( new_prefix )
        seen[k] = 1
        paths = paths + all_paths_from(k,new_prefix, seen, edge_map)
    return paths

def all_all_paths(nodes,edge_map):
    all_paths = []
    for i in nodes:
        # change 1 : set prefix and seen instead of None
        prefix = [i]
        seen = {i:1}
        all_paths = all_paths + (all_paths_from(i,prefix,seen,edge_map))
    return all_paths


# sample connections
connections = [("a", "b"), ("a", "c"), ("a", "c"), ("c", "d"), ("c", "e"), ("d", "f"), ("d", "g"), ("g", "h"), ("g", "i"), ("i", "j")]
sources = [connection[0] for connection in connections]
destinations = [connection[1] for connection in connections]
all_nodes = set(sources + destinations)
node_serial = []
for node in all_nodes:
    node_serial.append(node)

assert("a" in all_nodes and "b" in all_nodes and "c" in all_nodes and "d" in all_nodes and "e" in all_nodes and "f" in all_nodes and "g" in all_nodes and "h" in all_nodes and "i" in all_nodes and "j" in all_nodes)
print("All nodes from a to j are present in the graph")


object_dict = {
    "a": "msg",
    "b": "tgl",
    "c": "floatatom",
    "d": "r",
    "e": "send",
    "f": "bng",
    "g": "osc~",
    "h": "*",
    "i": "*~",
    "j": "dac~"
}


# create a dictionary of nodes where the key is the node id and the value is the node name
node_dict = {}
reverse_node_dict = {}



for i, node in enumerate(all_nodes):
    node_dict[node] = i
    reverse_node_dict[i] = node


correct_node_dict = {node_serial[0]: 0, node_serial[1]: 1, node_serial[2]: 2, node_serial[3]: 3, node_serial[4]: 4, node_serial[5]: 5, node_serial[6]: 6, node_serial[7]: 7, node_serial[8]: 8, node_serial[9]: 9}
correct_reversed_node_dict = {0: node_serial[0], 1: node_serial[1], 2: node_serial[2], 3: node_serial[3], 4: node_serial[4], 5: node_serial[5], 6: node_serial[6], 7: node_serial[7], 8: node_serial[8], 9: node_serial[9]}


assert node_dict == correct_node_dict
assert reverse_node_dict == correct_reversed_node_dict

print("Implementation of node dict and reverse node dict is correct")


nodes = list(node_dict.values())
edges = [(node_dict[connection[0]], node_dict[connection[1]]) for connection in connections]


edge_map = make_edge_map(nodes, edges) # creates an adjacency list of the graph

all_generated_paths =  all_all_paths(nodes, edge_map)

for path in all_generated_paths:
    for i in range(len(path)):
        path[i] = object_dict[reverse_node_dict[path[i]]]


assert(len(all_generated_paths) == 25)
assert(['msg', 'floatatom', 'r', 'osc~', '*~', 'dac~'] in all_generated_paths)
assert(['msg', 'tgl'] in all_generated_paths)
assert(['msg', 'floatatom'] in all_generated_paths)
assert(['msg', 'floatatom', 'r'] in all_generated_paths)
assert(['msg', 'floatatom', 'r', 'bng'] in all_generated_paths)
assert(['msg', 'floatatom', 'r', 'osc~'] in all_generated_paths)
assert(['msg', 'floatatom', 'r', 'osc~', '*'] in all_generated_paths)
assert(['msg', 'floatatom', 'r', 'osc~', '*~'] in all_generated_paths)
assert(['msg', 'floatatom', 'r', 'osc~', '*~', 'dac~'] in all_generated_paths)
assert(['msg', 'floatatom', 'send'] in all_generated_paths)
assert(['osc~', '*'] in all_generated_paths)
assert(['osc~', '*~'] in all_generated_paths)
assert(['osc~', '*~', 'dac~'] in all_generated_paths)
assert(['floatatom', 'r'] in all_generated_paths)
assert(['floatatom', 'r', 'bng'] in all_generated_paths)
assert(['floatatom', 'r', 'osc~'] in all_generated_paths)
assert(['floatatom', 'r', 'osc~', '*'] in all_generated_paths)
assert(['floatatom', 'r', 'osc~', '*~'] in all_generated_paths)
assert(['floatatom', 'r', 'osc~', '*~', 'dac~'] in all_generated_paths)
assert(['floatatom', 'send'] in all_generated_paths)
assert(['r', 'bng'] in all_generated_paths)
assert(['r', 'osc~'] in all_generated_paths)
assert(['r', 'osc~', '*'] in all_generated_paths)
assert(['r', 'osc~', '*~'] in all_generated_paths)
assert(['r', 'osc~', '*~', 'dac~'] in all_generated_paths)
assert(['*~', 'dac~'] in all_generated_paths)
print("All paths have been generated correctly")