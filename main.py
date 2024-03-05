import heapq 
from show_tree import show_tree

def minimize_total_costs(arr,descending=False):
    sign = -1 if descending else 1
    h = [sign * x for x in arr]
    heapq.heapify(h)
    total = 0
    connections = []
    
    while len(h) > 1:
        cabel1 = heapq.heappop(h)
        cabel2 = heapq.heappop(h)
        
        cables_cost = cabel1 + cabel2
        total += cables_cost
        heapq.heappush(h, cables_cost)
        # show_tree(h)
        connections.append((sign * cabel1, sign *cabel2))
        
    return sign * total, connections
        

arr1 = [30, 49, 63, 11, 40, 58, 2, 74, 92, 61, 24, 21, 83, 16, 86, 52, 33, 82, 79, 23, 14, 81, 18, 37, 67, 7, 62, 34]
arr2 = [4, 3, 8, 1, 13, 2, 6]

res_desc = minimize_total_costs(arr1, True)
res_asc = minimize_total_costs(arr1)

res_desc2 = minimize_total_costs(arr2, True)
res_asc2 = minimize_total_costs(arr2)


print(f"Minimum total cost using max heap: {res_desc[0]}")
print(f"Minimum total cost min heap: {res_asc[0]}")
# # second arr
print(f"\nMinimum total cost using max heap: {res_desc2[0]}")
print(f"Minimum total cost min heap: {res_asc2[0]}")

print('\n Conclusion:\n Min heap minimizes total costs better.\n')

for connection in res_desc2[1]:
    print(f"Connect cables {connection[0]} and {connection[1]}")
print('\n')
for connection in res_asc2[1]:
    print(f"Connect cables {connection[0]} and {connection[1]}")
