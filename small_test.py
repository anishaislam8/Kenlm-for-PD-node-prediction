from utils import *

connections = [["a", "b"], ["b", "c"], ["d", "c"], ["d", "e"], ["e", "f"], ["c", "f"], ["f", "g"]]
all_objects = ["a", "b", "c", "d", "e", "f", "g"]


G_reversed = create_reverse_directed_graph_test(connections, all_objects)


for node in all_objects:
    all_paths_ending_with_this_node = []
    visited = {node: False for node in all_objects}
    current_path_for_this_node = []
    three_length_dfs(node, G_reversed, visited, current_path_for_this_node, all_paths_ending_with_this_node)


    print("All paths ending with this node: ", node)
    for path in all_paths_ending_with_this_node:
        print(path[::-1])
    print("\n")




