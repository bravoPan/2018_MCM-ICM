# the shortest distance
    def find_shortest(self, start, end):
        # org, not will be replaced
        org_start = start
        org_end = end
        
        # set costs inf
        costs = {}
        inf = float("inf")
        # first to 0, or it will endless
        costs.setdefault(start, 0)
        for i in list(self.co_map):
            costs.setdefault(i, inf)
    
        # process for filter unprocessed point
        process = []
        parens = {"A": None}
        while start != end:
            # if end in neighbors, end program, get the dis
            if end in self.ne_map[start]:
                break
            # update neighbors weight
            for i in self.ne_map[start]:
                if i not in process:
                    current_dis = self.compute_dis(self.co_map[start][0], self.co_map[i][0],
                                                   self.co_map[start][1], self.co_map[i][1])
                                                   # find the smallest weighted neighbor as the next loop start
                                                   if current_dis + costs[start] < costs[i]:
                                                       costs[i] = current_dis + costs[start]
                                                       parens.setdefault(i, start)
            # add this point as processed
            process.append(start)
            # return the smallest
            start = [i[0] for i in sorted(costs.items(), key=lambda x: x[1], reverse=False) if
                     i[0] not in process][0]
                parens[end] = start
                costs[end] = costs[start] + self.compute_dis(self.co_map[start][0], self.co_map[end][0],
                                                             self.co_map[start][1], self.co_map[end][1])
                return self.find_path(parens, org_start, org_end)

    '''
    work principle likes this(end: F, start: A)
    F B D E A
    B D E A None
    F has a special key for link the start
    '''
        def find_path(self, link_dict, start, end):
        path = []
        while end != start:
            path.append(end)
            end = link_dict[end]
path.append(start)
path.reverse()
return path

