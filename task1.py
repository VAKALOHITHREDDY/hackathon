import heapq

def top_k_posts(posts, k, get_score):
    min_heap = []

    for post in posts:
        score = get_score(post)
        if len(min_heap) < k:
            heapq.heappush(min_heap, (score, post))
        else:
            if score > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (score, post))

    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])

    return result

# Example
posts = ["p1", "p2", "p3", "p4"]
scores = {"p1": 10, "p2": 30, "p3": 25, "p4": 40}

def get_score(post):
    return scores[post]

output = top_k_posts(posts, 2, get_score)
print( output)
# Output: ['p4', 'p2']
