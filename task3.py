# 3. Ride-Sharing Driver Matching .
import heapq

def find_closest_drivers(rider, drivers, n):
    heap = []

    rider_lat, rider_lon = rider

    for driver_id in drivers:
        driver_lat, driver_lon = drivers[driver_id]
        distance = (rider_lat - driver_lat) ** 2 + (rider_lon - driver_lon) ** 2
        if len(heap) < n:
            heapq.heappush(heap, (-distance, driver_id))
        else:
            if -distance > heap[0][0]:
                heapq.heappushpop(heap, (-distance, driver_id))

    result = []
    while heap:
        item = heapq.heappop(heap)
        result.append(item[1])
    result.reverse()
    return result

rider_location = (10.0, 20.0)

# example
drivers_data = {
    "driver1": (10.1, 20.1),
    "driver2": (11.0, 21.0),
    "driver3": (9.9, 19.9),
    "driver4": (12.0, 25.0),
    "driver5": (10.05, 20.05)
}

closest = find_closest_drivers(rider_location, drivers_data, 3)
print(closest)
# Output: ['driver5', 'driver1', 'driver3']
