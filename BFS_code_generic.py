def BFS(node,adj_list):
    level={node:0} ## source node
    parent={node:None}  ## source node has no parent (this structure is optional)
    i=1
    frontier=[node] ## first start from the source node
    while frontier: ## while the frontier collection is not empty
        next=[]
        for u in frontier: ## for node in frontier
            for elem in adj_list[u]: # for node in adjacency list of each frontier
                if elem not in level:## if we have not visited the node before
                    level[elem]=i ## set level to current i
                    parent[elem]=u## parent of element is the node whose adjacency list the element belongs to
                    next.append(elem) ## append the elements of the adjacency list to traverse next along the breadth
        frontier=next## the next level becomes the current level
        i+=1## increase level count every iteration
    return level,parent