import math


def calculate_intersection_points(radius):
    points = []
    for i in range(6):
        theta = i * (math.pi / 3)
        x = round(radius * math.cos(theta), 10)
        y = round(radius * math.sin(theta), 10)
        points.append((x, y))
    return points


radius = int(input("Enter radius: "))
intersection_points = calculate_intersection_points(radius)

print("Intersection Points:")
for point in intersection_points:
    print(point)


def calculate_distances(intersection_points, user_point):
    distances = []
    for point in intersection_points:
        x1, y1 = user_point
        x2, y2 = point

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distances.append(distance)

    return distances


def calculate_time(distances, speed_of_sound):
    times = []
    for distance in distances:
        time = distance / speed_of_sound
        times.append(time)
    return times


# Define the speed of sound (in meters per second)
speed_of_sound = 343.0  # Adjust this value if needed

user_x = float(input("Enter x coordinate of the point: "))
user_y = float(input("Enter y coordinate of the point: "))
user_point = (user_x, user_y)

distances = calculate_distances(intersection_points, user_point)

times = calculate_time(distances, speed_of_sound)

angle_theta = math.atan2(user_x, user_y)
angle_degrees = math.degrees(angle_theta)

print("\nDistances and Time taken for sound to travel each distance:")
for i, (distance, time) in enumerate(zip(distances, times)):
    print(f"Point {i + 1}: Distance = {distance:.4f} meters, Time = {time:.6f} seconds")

print("angle theta =" + str(angle_theta))
print("angle degrees =" + str(angle_degrees))
