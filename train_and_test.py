import kenlm
import json
import sqlite3

from utils import *

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def evaluate_kenlm_model(model):
    processed = 0
    with open("test_hashes.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            
            print("Processed :", processed)
            processed += 1
            line = line.strip()
            content = get_content_from_db(line, cursor)
            data = json.loads(content)

            try:
                connections = data["connections"]
                all_objects = data["all_objects"]
            except:
                connections = []
                all_objects = []


            if len(connections) > 0:
                
                object_dict = create_a_dictionary_of_object_id_to_type(all_objects)

                sources = [connection["patchline"]["source"][0] for connection in connections]
                destinations = [connection["patchline"]["destination"][0] for connection in connections]
                nodes = set(sources + destinations)
            
                G_reversed = create_reverse_directed_graph(connections, all_objects)


                mrr_for_this_graph = 0.0
            
                for node in nodes:
                    # for each node, restart the algorithm from scratch
                    all_paths_ending_with_this_node = []
                    visited = {node: False for node in nodes}
                    current_path_for_this_node = []
                    three_length_dfs(node, G_reversed, visited, current_path_for_this_node, all_paths_ending_with_this_node)

                    true_next_word = object_dict[node]
                    rank = get_rank(all_paths_ending_with_this_node, model, object_dict, true_next_word, 0)


                    # write to a file
                    with open("output/" + line + ".txt", "a") as f:
                        f.write(node + " " + str(len(all_paths_ending_with_this_node)) + " " + object_dict[node] + " " + str(rank) + "\n")

                    if rank != -1:
                        mrr_for_this_graph += (1.0/rank)

                mrr_for_this_graph /= len(nodes)

                with open("mrr.txt", "a") as f:
                    f.write(line + " " + str(mrr_for_this_graph) + "\n")

            else:
                with open("exception.txt", "a") as f:
                    f.write(line + ": No connections found\n")





      

            

model = kenlm.Model('trained_models/kenlm_3_paths_all_not_padded.arpa')
evaluate_kenlm_model(model)


