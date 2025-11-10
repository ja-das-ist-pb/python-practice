# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# for _ in range(q):
#     l, r = map(int, input().split())
#     l = l-1
#     ave = sum(a[l:r]) / (r - l + 1)
#     var = 0
#     for i in range(r-l+1):
#         var += (a[i] - ave)**2
#     var /= r-l+1
#     print("ans", round(var))

def calculate_variance(a, l, r):
    """
    Calculate variance for elements a[l] to a[r] (1-indexed)
    Formula: Var = (1/(r-l+1)) * sum((a_i - mean)^2)
    """
    # Convert to 0-indexed
    l_idx = l - 1
    r_idx = r - 1
    
    # Extract subset
    subset = a[l_idx:r_idx + 1]
    n = len(subset)
    
    # Calculate mean
    mean = sum(subset) / n
    
    # Calculate variance
    variance = sum((x - mean) ** 2 for x in subset) / n
    
    # Round to nearest integer
    return round(variance)


# Read input
first_line = input().split()
N = int(first_line[0])
Q = int(first_line[1])

# Read sequence a
a = list(map(int, input().split()))

# Process Q queries
for _ in range(Q):
    query = list(map(int, input().split()))
    l = query[0]
    r = query[1]
    
    result = calculate_variance(a, l, r)
    print(result)