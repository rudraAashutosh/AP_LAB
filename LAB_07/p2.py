#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

#define N 4  // Adjust for larger N

int findMinCost(vector<vector<int>> &cost, vector<int> &workers, vector<int> &jobs, vector<bool> &visited, int worker) {
    if (worker >= N) return 0; // Base case: all workers assigned

    int minCost = INT_MAX;
    for (int job = 0; job < N; job++) {
        if (!visited[job]) {
            visited[job] = true;
            int costWithCurrent = cost[worker][job] + findMinCost(cost, workers, jobs, visited, worker + 1);
            minCost = min(minCost, costWithCurrent);
            visited[job] = false; // Backtrack
        }
    }
    return minCost;
}

int minAssignmentCost(vector<vector<int>> &cost) {
    vector<int> workers(N, -1);
    vector<int> jobs(N, -1);
    vector<bool> visited(N, false);

    return findMinCost(cost, workers, jobs, visited, 0);
}

int main() {
    vector<vector<int>> cost = {
        {9, 2, 7, 8},
        {6, 4, 3, 7},
        {5, 8, 1, 8},
        {7, 6, 9, 4}
    };

    cout << "Minimum Assignment Cost: " << minAssignmentCost(cost) << endl;
    return 0;
}