# 3. Ride-Sharing Driver Matching
import heapq
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_closest_drivers(rider_x, rider_y, drivers_dict, n):
    max_heap = []
    for driver_name in drivers_dict:
        driver_x, driver_y = drivers_dict[driver_name]
        distance = get_distance(rider_x, rider_y, driver_x, driver_y)

        if len(max_heap) < n:
            heapq.heappush(max_heap, (-distance, driver_name))
        else:
            if distance < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, driver_name))

    result = []
    while len(max_heap) > 0:
        distance, name = heapq.heappop(max_heap)
        result.append(name)

    return result

# Example usage
rider_x = 0
rider_y = 0

drivers = {
    "driver1": (1, 2),
    "driver2": (4, 4),
    "driver3": (2, 1),
    "driver4": (10, 10)
}

closest_drivers = find_closest_drivers(rider_x, rider_y, drivers, 2)
print(closest_drivers)
# Output: ['driver3', 'driver1']