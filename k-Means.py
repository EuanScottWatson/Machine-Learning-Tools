import numpy as np


# L1 norm
def manhattan_distance(a, b):
    return sum([abs(i - j) for i, j in zip(a, b)])


# L2 norm
def euclidian_distance(a, b):
    return np.linalg.norm(a - b)


def assign(clusters, data, distance_metric):
    # Assigns each data point to a cluster
    assignments = {i: [] for i in range(len(clusters))}
    print("Nodes: \tCentroid Centroid Pos \t Distance to Centroid")
    for node in data:
        closest = (float('inf'), None, -1)
        for i, c in enumerate(clusters):
            distance = distance_metric(node, c)
            if distance < closest[0]:
                closest = (distance, c, i)
        
        assignments[closest[2]].append(node)
        print("{0}: \t{1} \t {2} \t\t {3}".format(node, closest[2] + 1, closest[1], closest[0]))

    print("\nAssignments for each centroid:")
    for (k, v) in assignments.items():
        print("\t", k, v)

    return assignments


def updates(assigments):
    new = {}
    for (k, v) in assigments.items():
        newC = sum(v) / len(v)
        new[k] = newC

    print("\nNew Centroid Positions:")
    for (k, v) in new.items():
        print("\t", k, v)    

if __name__ == "__main__":
    # All the centroids
    centroids = [
        np.array([1, 3]),
        np.array([7, 3]),
        np.array([5, 7]),
        np.array([8, 9])
    ]

    # All the data points
    data = [
        np.array([4, 7]),
        np.array([7, 1]),
        np.array([9, 2]),
        np.array([9, 3]),
        np.array([2, 1]),
        np.array([8, 9]),
        np.array([4, 8]),
        np.array([4, 8]),
        np.array([3, 4]),
        np.array([6, 6]),
        np.array([7, 2]),
        np.array([8, 9]),
        np.array([1, 1]),
        np.array([8, 9]),

    ]

    assignments = assign(centroids, data, manhattan_distance)
    updates(assignments)
