import operator

########################## MIN HEAP ##########################################

# heap_pop function returns the first element of the list implementing the heap,
# providing the heap is not empty

def heap_pop(heap):
    if heap != []:
        vertex,weight,parent = heap.pop(0)
        return (vertex, weight, parent)
    else:
        raise

# adds an element to the min heap
def heap_add_or_replace(heap, triplet):

    flag = 0
    if heap != []:
        for i in heap:
            if i[0] == triplet[0] and i[1] > triplet[1]:
                heap.remove(i)
                heap.append(triplet)
                flag = 1
                break;
            elif i[0] == triplet[0] and i[1] < triplet[1]:
                flag = 1
                break;
        if not flag:
            heap.append(triplet)
    else:
        heap.append(triplet)
    
    heap.sort(key=lambda item: item[1])
    return heap;

def is_explored(explored_vertices,vertex):
    return vertex in explored_vertices

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)
    
def Dijkstra(maze_graph,initial_vertex):
    # Variable storing the exploredled vertices vertexes not to go there again
    explored_vertices = list()
    
    # Stack of vertexes
    heap = list()
    
    #Parent dictionary
    parent_dict = dict()
    # Distances dictionary
    distances = dict()
    
    # First call
    initial_vertex = (initial_vertex, 0, initial_vertex)#vertex to visit, distance from origin, parent
    heap_add_or_replace(heap,initial_vertex)
    while len(heap) > 0:
        # get the triplet (vertex, distance, parent) with the smallest distance from heap list using heap_pop function.
        # if the vertex of the triplet is not explored:
        #     map the vertex to its corresponding parent
        #     add vertex to explored vertices.
        #     set distance from inital_vertex to vertex
        #     for each unexplored neighbor i of the vertex, connected through an edge of weight wi
        #         add (i, distance + wi, vertex) to the heap

        (vertex, distance, parent) = heap_pop(heap)
        if not is_explored(explored_vertices, vertex):
            parent_dict[vertex] = parent
            add_to_explored_vertices(explored_vertices, vertex)
            distances[vertex] = distance
            for i in maze_graph[vertex]:
                if not is_explored(explored_vertices, i):
                    heap_add_or_replace(heap,(i, distance + maze_graph[vertex][i], vertex))
    return explored_vertices, parent_dict, distances

#Driver program

maze_graph = {
    (0,0): {(1,0):3,(0,1):5}, 
    (1,0): {(0,1):1,(1,1):2},
    (0,1): {(1,1):1,(0,2):2},
    (1,1): {(1,2):2},
    (0,2): {(1,2):4},
    (1,2): {(0,1):3},
    (2,2): {(1,2):2,(3,2):1},
    (2,1): {(1,1):3,(2,2):7},
    (3,2): {(2,1):2}
}

explored_vertices,parent_dict,distances=Dijkstra(maze_graph,(0,0))
print("explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(1,0)):
    print("Vertex {} is reached from vertex {}, and its distance from initial vertex is {}".format(vertex,parent,distances[vertex]))
