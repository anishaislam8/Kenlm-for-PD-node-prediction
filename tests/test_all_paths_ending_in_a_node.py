def create_reverse_directed_graph_test(connections, all_objects):
    
    graph = {obj: [] for obj in all_objects}
    
    for connection in connections:

        source = connection[0]
        destination = connection[1]

        graph[destination].append(source)

    return graph


def three_length_dfs(node, G, visited, path, paths):

    '''
    Ref: code collected from internet
    Get all the paths of less than equal length 3 from the node
    '''

    visited[node] = True
    path.append(node)

    if len(path) <= 3:
        paths.append(path.copy())    
    
        for neighbor in G[node]:
            if not visited[neighbor]:
                three_length_dfs(neighbor, G, visited, path, paths)

    path.pop()
    visited[node] = False


connections = [["a", "b"], ["b", "c"], ["d", "c"], ["d", "e"], ["e", "f"], ["c", "f"], ["f", "g"]]
all_objects = ["a", "b", "c", "d", "e", "f", "g"]


G_reversed = create_reverse_directed_graph_test(connections, all_objects)

# test that the reverse graph has opposite edges as the original graph

assert(G_reversed["a"] == []) # no outgoing edges from a
assert(G_reversed["b"] == ["a"]) # b -> a 
assert(G_reversed["c"] == ["b", "d"]) # c -> b, c -> d
assert(G_reversed["d"] == []) # no outgoing edges from d
assert(G_reversed["e"] == ["d"]) # e -> d
assert(G_reversed["f"] == ["e", "c"]) # f -> e, f -> c
assert(G_reversed["g"] == ["f"]) # g -> f

print("Reverse graph test passed")

paths = {}


for node in all_objects:
    all_paths_ending_with_this_node = []
    visited = {node: False for node in all_objects}
    current_path_for_this_node = []
    three_length_dfs(node, G_reversed, visited, current_path_for_this_node, all_paths_ending_with_this_node)


    paths[node] = all_paths_ending_with_this_node
    # print("All paths ending with this node: ", node)
    # for path in all_paths_ending_with_this_node:
    #     print(path[::-1])
    # print("\n")


# number of paths ending in a node with length <= 3
assert(len(paths["a"]) == 1)
assert(len(paths["b"]) == 2)
assert(len(paths["c"]) == 4)
assert(len(paths["d"]) == 1)
assert(len(paths["e"]) == 2)
assert(len(paths["f"]) == 6)
assert(len(paths["g"]) == 4)

print("Number of paths ending in a node test passed")

print("All tests passed for create_reverse_directed_graph test and paths ending in a node test")
