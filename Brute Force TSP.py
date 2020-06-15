import utils

def create_vertices_meta_graph(piece_of_cheese, player_location):

    return( list(piece_of_cheese) + [(player_location)])

def create_edge_weight_maze_graph(maze_graph,vertices):
    adjacency_matrix={}
    # for each initial_vertex in vertices:
    #     considere this vertex as source vertex
    #     use this source vertex and maze_graph to browse the graph with dijkstra algorithm
    #     for each vertex in vertices:
        #     use adjacency_matrix to store distances between source vertex and each vertex in the graph.
        #     remember to not store the distance from the source vertex to itself.

    for vertex in vertices:
        (exploredVertices, parentDictionary, distanceDict) = utils.Dijkstra(maze_graph, vertex)
#         for i in distanceDict:
#         print(distanceDict)
        adjacency_matrix[vertex] = {}
        for k in distanceDict:
            if k != vertex and k in vertices:
                adjacency_matrix[vertex][k] = distanceDict[k]
    return adjacency_matrix

def auxbf(current_walk,best_walk,adjacency_matrix,vertices,current_distance,best_distance):
   
    order = len(vertices)
    if len(current_walk) >= order:
        if current_distance < best_distance:
            best_distance = current_distance
            best_walk = current_walk
    else:
        for i in vertices:
            if i not in current_walk:
                _from = current_walk[len(current_walk) - 1]
                _to = i
                p_best_walk, p_best_distance = auxbf(current_walk + list([i]),best_walk,adjacency_matrix,vertices,current_distance + adjacency_matrix[_from][_to],best_distance)
                if p_best_distance < best_distance:
                    best_distance = p_best_distance
                    best_walk = p_best_walk
                    
    return best_walk,best_distance
                    
def bruteforceTSP(maze_graph,pieces_of_cheese,player_location):
    # first we compute the vertices of the meta_graph:
    vertices=create_vertices_meta_graph(pieces_of_cheese, player_location)

    # then we create the adjacency matrix of the meta graph
    adjacency_matrix = create_edge_weight_maze_graph(maze_graph,vertices)
    
    # now we can start defining our variables
    # current_distance is the length of the walk for the current exploration branch
    current_distance = 0
    # current_walk is a container for the current exploration branch
    current_walk = [player_location]
    # best_distance is an indicator of the shortest walk found so far
    best_distance = float('inf')
    # best_walk is a container for the corresponding walk
    best_walk = []
    
    # we start the exploration:
    best_walk, best_distance = auxbf(current_walk,best_walk,adjacency_matrix,vertices,current_distance,best_distance)
    return best_walk, best_distance
