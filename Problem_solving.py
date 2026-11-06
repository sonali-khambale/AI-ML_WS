# 1. Find the Second-Largest Unique Element Without sort() or max()
arr = [10, 20, 40, 30, 40, 50]

largest = None
second = None

for num in arr:
    if num == largest or num == second:
        continue

    if largest is None or num > largest:
        second = largest
        largest = num
    elif second is None or num > second:
        second = num

print("Second largest:", second)


# 2. Find All Pairs Whose Sum Equals a Target
arr = [2, 4, 3, 5, 7, 8, 1]
target = 9

seen = set()
pairs = set()

for num in arr:
    complement = target - num

    if complement in seen:
        pairs.add((min(num, complement),
                   max(num, complement)))

    seen.add(num)

print("Pairs:", pairs)


# 3. Move All Zeros to the End
arr = [0, 1, 0, 3, 12]

result = []

for num in arr:
    if num != 0:
        result.append(num)

zeros = len(arr) - len(result)

result.extend([0] * zeros)

print(result)


# 4. Find the Missing Number from 1 to N
arr = [1, 2, 4, 5, 6]
n = 6

total = n * (n + 1) // 2
actual = sum(arr)

missing = total - actual

print("Missing number:", missing)


# 5. Find Duplicate Elements Without Nested Loops
arr = [1, 2, 3, 2, 4, 5, 1]

seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", duplicates)


# 6. Find the First Non-Repeating Character
text = "swiss"

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating:", ch)
        break
else:
    print("No non-repeating character")


# 7. Check Anagrams Without sorted()
str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    frequency = {}

    for ch in str1:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in str2:
        if ch not in frequency:
            print("Not Anagrams")
            break

        frequency[ch] -= 1
    else:
        if all(value == 0 for value in frequency.values()):
            print("Anagrams")
        else:
            print("Not Anagrams")

# 8. Merge Two Sorted Arrays Without sort()
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

i = 0
j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print("Merged array:", result)


# 9. Rotate an Array to the Right by K Positions
arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)

result = arr[-k:] + arr[:-k]

print("Rotated array:", result)



# 10. Find Intersection of Two Arrays Including Duplicates
a = [1, 2, 2, 3, 4]
b = [2, 2, 4, 5]

frequency = {}

for num in a:
    frequency[num] = frequency.get(num, 0) + 1

result = []

for num in b:
    if frequency.get(num, 0) > 0:
        result.append(num)
        frequency[num] -= 1

print("Intersection:", result)



# 11. Maximum Sum of a Contiguous Subarray (Kadane's Algorithm)
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

for num in arr[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("Maximum subarray sum:", max_sum)



# 12. Longest Substring Without Repeating Characters
text = "abcabcbb"

seen = {}
start = 0
max_length = 0

for i, ch in enumerate(text):
    if ch in seen and seen[ch] >= start:
        start = seen[ch] + 1

    seen[ch] = i

    max_length = max(max_length, i - start + 1)

print("Longest length:", max_length)


# 13. Longest Common Prefix Among Multiple Strings
words = ["flower", "flow", "flight"]

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

        if prefix == "":
            break

print("Common prefix:", prefix)



# 14. Group Strings into Anagram Groups
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = tuple(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(list(groups.values()))


# 15. Find the Kth Largest Element in an Unsorted Array
arr = [3, 2, 1, 5, 6, 4]
k = 2

unique = list(set(arr))

for i in range(k):
    largest = unique[0]

    for num in unique:
        if num > largest:
            largest = num

    if i == k - 1:
        print("Kth largest:", largest)

    unique.remove(largest)



# 16. Find All Subarrays Whose Sum Equals a Target
arr = [1, 2, 3, -2, 5]
target = 5

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total += arr[j]

        if total == target:
            print(arr[i:j+1])


# 17. Merge Overlapping Intervals
intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

merged = [intervals[0]]

for start, end in intervals[1:]:
    last = merged[-1]

    if start <= last[1]:
        last[1] = max(last[1], end)
    else:
        merged.append([start, end])

print("Merged intervals:", merged)


# 18. Search an Element in a Rotated Sorted Array
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at index:", mid)
        break

    if arr[left] <= arr[mid]:
        if arr[left] <= target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1
else:
    print("Element not found")



# 19. Find the Longest Consecutive Sequence
arr = [100, 4, 200, 1, 3, 2]

nums = set(arr)
longest = 0

for num in nums:
    if num - 1 not in nums:
        count = 1

        while num + count in nums:
            count += 1

        longest = max(longest, count)

print("Longest consecutive sequence:", longest)



# 20. Find Trapped Rainwater Between Elevation Bars
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

left = 0
right = len(height) - 1

left_max = 0
right_max = 0
water = 0

while left < right:
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]

        left += 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]

        right -= 1

print("Trapped rainwater:", water)



# 21. Find Median of Two Sorted Arrays in O(log(m+n)) Time
def find_median(a, b):
    if len(a) > len(b):
        a, b = b, a

    m = len(a)
    n = len(b)

    low = 0
    high = m

    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i

        left_a = float('-inf') if i == 0 else a[i-1]
        right_a = float('inf') if i == m else a[i]

        left_b = float('-inf') if j == 0 else b[j-1]
        right_b = float('inf') if j == n else b[j]

        if left_a <= right_b and left_b <= right_a:
            if (m + n) % 2 == 0:
                return (max(left_a, left_b) +
                        min(right_a, right_b)) / 2

            return max(left_a, left_b)

        elif left_a > right_b:
            high = i - 1
        else:
            low = i + 1

    return None


a = [1, 3]
b = [2]

print("Median:", find_median(a, b))


# 22. Maximum Product of a Contiguous Subarray
arr = [2, 3, -2, 4]

max_product = arr[0]
min_product = arr[0]
result = arr[0]

for num in arr[1:]:
    if num < 0:
        max_product, min_product = min_product, max_product

    max_product = max(num, max_product * num)
    min_product = min(num, min_product * num)

    result = max(result, max_product)

print("Maximum product:", result)



# 23. Find the Smallest Missing Positive Integer
arr = [3, 4, -1, 1]

nums = set(arr)
smallest = 1

while smallest in nums:
    smallest += 1

print("Smallest missing positive:", smallest)


# 24. Count Subarrays Whose Sum Equals K
arr = [1, 1, 1]
k = 2

frequency = {0: 1}
total = 0
count = 0

for num in arr:
    total += num

    count += frequency.get(total - k, 0)

    frequency[total] = frequency.get(total, 0) + 1

print("Number of subarrays:", count)


# 25. Find the Longest Increasing Subsequence
arr = [10, 9, 2, 5, 3, 7, 101, 18]

dp = [1] * len(arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print("Longest increasing subsequence length:", max(dp))



# 26. Coin Change Problem Using Dynamic Programming
coins = [1, 2, 5]
amount = 11

dp = [float('inf')] * (amount + 1)

dp[0] = 0

for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print("Change not possible")
else:
    print("Minimum coins:", dp[amount])



# 27. Word Break Problem Using Dynamic Programming
def word_break(text, word_dict):
    dp = [False] * (len(text) + 1)

    dp[0] = True

    for i in range(1, len(text) + 1):
        for j in range(i):
            if dp[j] and text[j:i] in word_dict:
                dp[i] = True
                break

    return dp[len(text)]


text = "applepenapple"

word_dict = {"apple", "pen"}

print(word_break(text, word_dict))


# 28. Minimum Number of Jumps to Reach the Last Index
arr = [2, 3, 1, 1, 4]

jumps = 0
current_end = 0
farthest = 0

for i in range(len(arr) - 1):
    farthest = max(farthest, i + arr[i])

    if i == current_end:
        if farthest == current_end:
            jumps = -1
            break

        jumps += 1
        current_end = farthest

print("Minimum jumps:", jumps)


# 29. Maximum Profit from Buying and Selling Stocks with Multiple Transactions
prices = [7, 1, 5, 3, 6, 4]

profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]

print("Maximum profit:", profit)


# 30. Implement LRU Cache with O(1) get() and put()
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))

cache.put(3, 30)

print(cache.get(2))


# 31. Implement Min Stack with O(1) Operations
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        if self.stack:
            return self.stack[-1]

        return None

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

        return None


s = MinStack()

s.push(5)
s.push(2)
s.push(8)
s.push(1)

print("Minimum:", s.getMin())
s.pop()
print("Minimum:", s.getMin())
print("Top:", s.top())


# 32. Find Number of Islands Using DFS
grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["0", "0", "0", "0"]
]

rows = len(grid)
cols = len(grid[0])

def dfs(i, j):
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return

    if grid[i][j] == "0":
        return

    grid[i][j] = "0"

    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)


count = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "1":
            count += 1
            dfs(i, j)

print("Number of islands:", count)



# 35. Detect a Cycle in a Directed and Undirected Graph
# A. Directed graph
def has_cycle(graph):
    visited = set()
    path = set()

    def dfs(node):
        visited.add(node)
        path.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

            elif neighbor in path:
                return True

        path.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


graph = {
    0: [1],
    1: [2],
    2: [0],
    3: []
}

print("Cycle detected:", has_cycle(graph))


# B. Undirected graph
def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True

            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

print("Cycle detected:", has_cycle(graph))




# 36. Implement Topological Sorting
from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

indegree = {node: 0 for node in graph}

for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

queue = deque()

for node in indegree:
    if indegree[node] == 0:
        queue.append(node)

result = []

while queue:
    node = queue.popleft()
    result.append(node)

    for neighbor in graph[node]:
        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)

if len(result) == len(graph):
    print("Topological order:", result)
else:
    print("Graph contains a cycle")




# 37. Solve the N-Queens Problem
def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]

    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False

        for i, j in zip(range(row-1, -1, -1),
                        range(col-1, -1, -1)):
            if board[i][j] == "Q":
                return False

        for i, j in zip(range(row-1, -1, -1),
                        range(col+1, n)):
            if board[i][j] == "Q":
                return False

        return True

    def solve(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"

                solve(row + 1)

                board[row][col] = "."

    solve(0)

    return solutions


for solution in solve_n_queens(4):
    for row in solution:
        print(row)
    print()



# 38. Generate All Unique Permutations
def permutations(arr):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        used = set()

        for i in range(len(remaining)):
            if remaining[i] in used:
                continue

            used.add(remaining[i])

            backtrack(
                path + [remaining[i]],
                remaining[:i] + remaining[i+1:]
            )

    backtrack([], arr)

    return result


arr = [1, 2, 2]

print("Permutations:")

for p in permutations(arr):
    print(p)



# 39. Serialize and Deserialize a Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def serialize(root):
    if root is None:
        return "#"

    return (
        str(root.value) + "," +
        serialize(root.left) + "," +
        serialize(root.right)
    )


def deserialize(data):
    values = iter(data.split(","))

    def build():
        value = next(values)

        if value == "#":
            return None

        node = Node(int(value))

        node.left = build()
        node.right = build()

        return node

    return build()


# Create tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.right.left = Node(4)
root.right.right = Node(5)

# Serialize
data = serialize(root)

print("Serialized:", data)

# Deserialize
new_root = deserialize(data)

print("Deserialized root:", new_root.value)



# 40. Find Lowest Common Ancestor in a Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)

    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# Create binary tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

p = root.left.left
q = root.left.right

result = lowest_common_ancestor(root, p, q)

if result:
    print("Lowest Common Ancestor:", result.value)
else:
    print("Ancestor not found")
