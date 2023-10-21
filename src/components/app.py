#include <iostream>
#include <vector>
#include <sstream>
#include <functional>

using namespace std;

class Solution {
public:
int longestIncreasingPath(vector<vector<int>>& grid) {
if (grid.empty() || grid[0].empty()) {
return 0;
}

int rows = grid.size();
int cols = grid[0].size();
vector<vector<int>> dp(rows, vector<int>(cols, 0));
vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
int max_path_length = 1;

auto is_valid = [&](int x, int y, int prev_val) {
return x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] > prev_val;
};

std::function<int(int, int)> dfs = [&](int x, int y) {
if (dp[x][y] != 0) {
return dp[x][y];
}

int max_length = 1;
for (const auto& dir : directions) {
int new_x = x + dir.first;
int new_y = y + dir.second;
if (is_valid(new_x, new_y, grid[x][y])) {
int length = 1 + dfs(new_x, new_y);
max_length = max(max_length, length);
}
}

dp[x][y] = max_length;
return max_length;
};

for (int i = 0; i < rows; i++) {
for (int j = 0; j < cols; j++) {
if (grid[i][j] != 0) {
max_path_length = max(max_path_length, dfs(i, j));
}
}
}

return max_path_length;
}
};

int main() {
Solution solution;
vector<vector<int>> grid(3, vector<int>(3));

cout << "Enter a 3x3 matrix (one row at a time, values separated by ','):" << endl;

for (int i = 0; i < 3; i++) {
string row;
getline(cin, row);
istringstream iss(row);

for (int j = 0; j < 3; j++) {
string value;
if (getline(iss, value, ',')) {
grid[i][j] = stoi(value);
}
}
}

int result = solution.longestIncreasingPath(grid);
cout << "The longest increasing path length is: " << result << endl;

return 0;
}
