def LIFO_push(LIFO_list, element):
    LIFO_list.append(element)

def LIFO_pop(LIFO_list):
    return LIFO_list.pop(-1)

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def is_explored(explored_vertices,vertex):
    return vertex in list(explored_vertices)
    
def DFS(maze_graph, initial_vertex) :
    
    # explored vertices list
    explored_vertices = list()
    
    #LIFO stack
    queuing_structure = list()
    
    #Parent Dictionary
    parent_dict = dict()
        

    LIFO_push(queuing_structure,(initial_vertex,None)) # push the initial vertex to the queuing_structure
    while len(queuing_structure) > 0: #   while queuing_structure is not empty:
        # current_vertex,parent = queuing_structure.pop()
        # if the current vertex is not explored
            # add current_vertex to explored vertices
            # use parent_dict to map the parent of the current vertex
            # for each neighbor of the current vertex in the maze graph:
                # if neighbor is not explored:
                    # push the tuple (neighbor,current_vertex) to the queuing_structure
        current_vertex,parent = LIFO_pop(queuing_structure)
        #
        if(not is_explored(explored_vertices, current_vertex)):
            add_to_explored_vertices(explored_vertices, current_vertex)
            parent_dict[current_vertex] = parent;
            for i in maze_graph[current_vertex]:
                if not is_explored(explored_vertices, i):
                    #print(maze_graph[current_vertex][i])
                    LIFO_push(queuing_structure,(i, current_vertex))
        #
    return explored_vertices,parent_dict    
###################################################################

#Driver Program

from operator import itemgetter

maze_graph = {
    (0,0): {(0,1):1,(1,0):1}, 
    (0,1): {(0,2):1,(0,0):1},
    (1,0): {(1,1):1,(0,0):1},
    (1,1): {(1,2):1,(1,0):1},
    (0,2): {(0,1):1,(1,2):1},
    (1,2): {(0,2):1,(1,1):1}
}
explored_vertices,parent_dict = DFS(maze_graph, (0,0))
print("Explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("Vertex {} is the parent of vertex {}".format(parent,vertex))

#Print the path

def create_walk_from_parents(parent_dict,initial_vertex,target_vertex):

    walk = list();
    
    while target_vertex != initial_vertex:
        walk.append(target_vertex)
        target_vertex = parent_dict[target_vertex]
        
    walk.reverse()
    
    return walk
