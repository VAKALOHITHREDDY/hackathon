# 2. E-commerce Flash Sale Hot Items
import heapq

def hot_items(request_counts, stock_levels, k):
    min_heap = []

    for item_id in request_counts:
        if item_id in stock_levels and stock_levels[item_id] > 0:
            count = request_counts[item_id]
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count, item_id))
            else:
                if count > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (count, item_id))

    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])

    return result

# Example
request_counts = {"item1": 50, "item2": 75, "item3": 10, "item4": 90}
stock_levels = {"item1": 5, "item2": 0, "item3": 2, "item4": 10}

output = hot_items(request_counts, stock_levels, 2)
print(output)
#output = ['item1', 'item4'] 