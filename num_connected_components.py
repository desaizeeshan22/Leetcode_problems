from collections import defaultdict
adj_list_map=defaultdict(list)## vertice as the key and it's adjacent nodes as compnent lists

visited=[False for  i in range(8)] ## keeping check of the vertices visited

input_vertices=[(1,2),(2,3),(2,4),(3,5),(6,7)] ## input as given by the question
for elem in input_vertices:
    adj_list_map[elem[0]].append(elem[1])## forming the map 1:[].append(2) and [2]:[].append(1)
    adj_list_map[elem[1]].append(elem[0])## every adjacent vertice is in each other's adjacency list

def DFS(current):
    visited[current]=True## set vertice numbered visited flag to True
    for elem in adj_list_map[current]:## traverse through the depth of the graph by traversing to adjacency list of every node
        if visited[elem]==True:## if already visited do nothing and skip
            continue
        else:
            DFS(elem)## recursively call to the element in the adjacency list to travel to max depth
num_connected_components=0## number of connected components
for elem in input_vertices:
    if visited[elem[0]]==True: ## if element already visited don't call DFS again as it has been included in the DFS
        ##call for the other connected components
        continue
    else:
        DFS(elem[0])## DFS completed while recursive DFS through one connected component
        num_connected_components+=1 ## increments after every complete call of the DFS
print(num_connected_components)
