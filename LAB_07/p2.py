import sys

N = 4  # Adjust for larger N

def find_min_cost(cost, workers, jobs, visited, worker):
    if worker >= N:
        return 0  # Base case: all workers assigned

    min_cost = sys.maxsize
    for job in range(N):
        if not visited[job]:
            visited[job] = True
            cost_with_current = cost[worker][job] + find_min_cost(cost, workers, jobs, visited, worker + 1)
            min_cost = min(min_cost, cost_with_current)
            visited[job] = False  # Backtrack
    return min_cost

def min_assignment_cost(cost):
    workers = [-1] * N
    jobs = [-1] * N
    visited = [False] * N

    return find_min_cost(cost, workers, jobs, visited, 0)

def main():
    cost = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]

    print("Minimum Assignment Cost:", min_assignment_cost(cost))

if __name__ == "__main__":
    main()