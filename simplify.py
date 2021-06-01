import sys

# Implementation of Ford-Fulkerson
# Inputs: Takes an dictionary and converts it into a readable list format using make_list method
# List is then passed to the simplify_result method
# List: 2D directed graph with debts
# Time-Complexity:


class simplify:
    @staticmethod
    def __make_list(balance_sheet):
        # To convert nested dictionaries into nested list
        keys = list(balance_sheet.keys())
        balance_list = [[0 for x in range(0, len(keys))] for x in range(0, len(keys))]
        i = 0
        for key in keys:
            temp_dict = balance_sheet[key]
            for val in temp_dict:
                pos = keys.index(val)
                if temp_dict[val] < 0:
                    balance_list[i][pos] = -(temp_dict[val])
            i = i + 1

        return balance_list

    @staticmethod
    def __breadth_frst_search(g_balance, source, target, parent):
        # Finds if path exists and returns path in parent list
        # Eg: Parent = [0, -1, 0, 1, 1, 4]
        # -1 denotes the source = 1 and let target = 5
        # Start= target || parent[start] and path = parent[start] i.e (5,4), (4,1) reached source = 1
        # Path used is from 1 -> 4 -> 5
        queue = []
        visited_nodes = [0] * len(g_balance)
        queue.append(source)  # Add source to queue
        visited_nodes[source] = 1  # Mark source node as visited
        parent[source] = -1  # For indication that path ends
        while len(queue) != 0:
            start = queue[0]  # BFS - so check for next adjacent valid nodes and store in queue
            queue.pop(0)
            for i in range(0, len(g_balance)):
                if (g_balance[start][i] > 0) and (not visited_nodes[i]):
                    # valid node - debt exists and is not visited yet
                    queue.append(i)
                    parent[i] = start  # store the path into its parent index
                    visited_nodes[i] = 1


        return visited_nodes[target] == 1

    @staticmethod
    def __ford_fulkerson(balance_graph, source, target):
        # Make a copy of directed graph 
        # For every path existing between source and target find max_flow (BFS)
        
        parent = [0] * len(balance_graph)  # Holds the path between source and target
        res_graph_balance = []  # copy of debts graph
        for i in range(0, len(balance_graph)):
            temp = []
            for j in range(0, len(balance_graph)):
                temp.append(balance_graph[i][j])
            res_graph_balance.append(temp)

        max_flow = 0  # max_flow for a particular combination of vertices

        while simplify.__breadth_frst_search(res_graph_balance, source, target, parent):
            # parent holds the path from source to target
            minflow_path = sys.maxsize
            start = target  # start at target(end) and traverse back to source and check for least value(min_Flow)
            while start != source:
                path = parent[start]
                minflow_path = res_graph_balance[path][start] if minflow_path > res_graph_balance[path][
                    start] else minflow_path

                start = parent[start]

            path_node = target  # start at target and traverse back to source and update debt values in residual graph
            while path_node != source:
                path = parent[path_node]
                res_graph_balance[path][path_node] -= minflow_path  # Forward flow - so we decrement the value
                res_graph_balance[path_node][path] += minflow_path  # Residual value if we need to undo the change
                path_node = parent[path_node]

            max_flow += minflow_path  # update the max_flow value
        # copy the updated values of debts excluding the residual values
        # Copy only if original debt exists
        for i in range(0, len(balance_graph)):
            for j in range(0, len(balance_graph)):
                if balance_graph[i][j] > 0:
                    balance_graph[i][j] = res_graph_balance[i][j]

        return max_flow

    @staticmethod
    def __simplify_result(balance_sheet):
        # We turn dictionary to a 2D list
        # For every value greater than 0 or If debt exists
        # Then we apply ford_fulkerson with source as the payee and target as receiver
        # Method returns max_flow between source and target
        # if flow > 0 then change the debt to the max_flow value

        graph_balances = simplify.__make_list(balance_sheet)

        for s in range(0, len(graph_balances)):
            for t in range(0, len(graph_balances)):
                if graph_balances[s][t] > 0:
                    flow = simplify.__ford_fulkerson(graph_balances, s, t)
                    if flow > 0:
                        graph_balances[s][t] = flow

        return graph_balances

    @staticmethod
    def __make_dict(final_res, user_names):
        # To convert the nested list back to nested dictionary

        final_dict = {k: {} for k in user_names}
        for i in range(0, len(final_res)):
            for j in range(0, len(final_res)):
                if final_res[i][j] > 0:
                    final_dict[user_names[i]][user_names[j]] = - final_res[i][j]
                    final_dict[user_names[j]][user_names[i]] = final_res[i][j]

        return final_dict

    @staticmethod
    def simplify(balance_sheet):
        # Main method for simplification of debts
        # result holds the simplified version of debts and users holds the names of all users
        # we return result by turning it back to nested dictionary
        result = simplify.__simplify_result(balance_sheet)
        users = list(balance_sheet.keys())
        return simplify.__make_dict(result, users)
