import sqlite3
import json
import sys
sys.setrecursionlimit(1000000)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def get_content_from_db(hash):
    cursor.execute("SELECT Content FROM Contents WHERE hash = ?", (hash,))
    content = cursor.fetchall()[0][0]
    return content

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


# does not consider double edges
def make_edge_map(nodes,edges):
    edge_map = dict([(i,dict()) for i in nodes])
    for a,b in edges:
        edge_map[a][b] = 1
    return edge_map

with open("train_hashes.txt", "r") as f:
    processed = 0
    lines = f.readlines()
    for line in lines:

        print("Processed :", processed)
        processed += 1
        line = line.strip()
        content = get_content_from_db(line)
        data = json.loads(content)

        try:
            connections = data["connections"]
            all_objects = data["all_objects"]
        except:
            connections = []
            all_objects = []

        if len(connections) > 0:
            object_dict = {}
            for obj in all_objects:
                if obj["box"]["object_type"] in ["list"]:
                    obj_text = obj["box"]["text"].split(" ")[:2]
                    obj_text_str = "_".join(obj_text)
                    object_dict[obj["box"]["id"]] = obj_text_str
                else:
                    object_dict[obj["box"]["id"]] = obj["box"]["object_type"]



            sources = [connection["patchline"]["source"][0] for connection in connections]
            destinations = [connection["patchline"]["destination"][0] for connection in connections]

            all_nodes = set(sources + destinations)


            # create a dictionary of nodes where the key is the node id and the value is the node name
            node_dict = {}
            reverse_node_dict = {}
            for i, node in enumerate(all_nodes):
                node_dict[node] = i
                reverse_node_dict[i] = node

            nodes = list(node_dict.values())
            edges = [(node_dict[connection["patchline"]["source"][0]], node_dict[connection["patchline"]["destination"][0]]) for connection in connections]

            edge_map = make_edge_map(nodes, edges) # creates an adjacency list of the graph

            all_generated_paths =  all_all_paths(nodes, edge_map)

            for path in all_generated_paths:
                for i in range(len(path)):
                    path[i] = object_dict[reverse_node_dict[path[i]]]

            with open("paths_all" + line + ".txt", "w") as f:
                for path in all_generated_paths:
                    for i in range(len(path)):
                        path[i]= str(path[i])
                        if i == len(path) - 1:
                            f.write(path[i])
                        else:
                            f.write(path[i] + " ")
                    f.write("\n")

        else:
            with open("paths_all" + line + ".txt", "w") as f:
                f.write("No connections")


cursor.close()
conn.close()