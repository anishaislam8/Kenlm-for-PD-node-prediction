import heapq

def get_content_from_db(hash, cursor):
    cursor.execute("SELECT Content FROM Contents WHERE hash = ?", (hash,))
    content = cursor.fetchall()[0][0]
    return content

def create_a_dictionary_of_object_id_to_type(all_objects):
    
    '''
    Create a dictionary of object_id to object_type
    For example, if the object_id is PD-ROOT_obj-0 and the object_type is "list_append", then the dictionary entry will be {"PD-ROOT_obj-0": "list_append"}
    '''

    object_dict = {}
    for obj in all_objects:
        if obj["box"]["object_type"] in ["list"]: # because for list we need the second argument
            obj_text = obj["box"]["text"].split(" ")[:2]
            obj_text_str = "_".join(obj_text)
            object_dict[obj["box"]["id"]] = obj_text_str
        else:
            object_dict[obj["box"]["id"]] = obj["box"]["object_type"]
    return object_dict

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


def create_reverse_directed_graph(connections, all_objects):
    
    graph = {obj["box"]["id"]: [] for obj in all_objects}
    
    for connection in connections:

        source = connection["patchline"]["source"][0]
        destination = connection["patchline"]["destination"][0]

        graph[destination].append(source)

    return graph



def create_reverse_directed_graph_test(connections, all_objects):
    
    graph = {obj: [] for obj in all_objects}
    
    for connection in connections:

        source = connection[0]
        destination = connection[1]

        graph[destination].append(source)

    return graph


def get_rank(all_paths_ending_with_this_node, model, object_dict, true_next_word, model_number):

    max_heap_size = 10
    heap = []
    vocab_file = None
    if model_number == 0:
        vocab_file = "trained_models/kenlm_all_paths_without_padding.vocab"
    if model_number == 1:
        vocab_file = "trained_models/model1/kenlm_all_paths_without_padding.vocab"
    elif model_number == 2:
        vocab_file = "trained_models/model2/kenlm_all_paths_without_padding.vocab"
    elif model_number == 3:
        vocab_file = "trained_models/model3/kenlm_all_paths_without_padding.vocab"
    elif model_number == 4:
        vocab_file = "trained_models/model4/kenlm_all_paths_without_padding.vocab"
    elif model_number == 5:
        vocab_file = "trained_models/model5/kenlm_all_paths_without_padding.vocab"

    vocabulary = None
    with open(vocab_file, "r", encoding="utf8") as vocab_f:
        vocabulary = vocab_f.readlines()
    
    for path in all_paths_ending_with_this_node:
        path = path[::-1]
        path = [object_dict[node] for node in path]

        if len(path) == 1 and len(all_paths_ending_with_this_node) == 1:
            context = ""
        elif len(path) == 1:
            continue
        elif len(path) > 1:
            # Use all words except the last one as context
            context = " ".join(path[:-1])
            context += " " 
       

    
        for candidate_word in vocabulary:
            candidate_word = candidate_word.strip()
            context_with_candidate = context + candidate_word
            score = model.score(context_with_candidate)
            
            

            found = False
            for token in heap:
                if token[1] == candidate_word:
                    found = True
                    if token[0] < score:
                        # replace the score
                        heap.remove(token)
                        heapq.heappush(heap, (score, candidate_word))
                    
                    break
                
            if found:
                heapq.heapify(heap)
                
            else:
                if len(heap) < max_heap_size:
                    heapq.heappush(heap, (score, candidate_word))
                
                else:
                    if score > heap[0][0]: # if current score is larger than the lowest possible element in heap
                        heapq.heappop(heap)
                        heapq.heappush(heap, (score, candidate_word))

    
    heapq.heapify(heap)
    # sort the heap
    heap.sort(key=lambda x: x[0], reverse = True)

    for i in range(len(heap)):
        if heap[i][1] == true_next_word:
            return i+1
        
    return -1

