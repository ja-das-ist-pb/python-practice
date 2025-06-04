def bfs(n, m, a):
    queue = []
    walked = [[False] * m for _ in range(n)]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue.append((0, 0, 1))
    walked[0][0] = True

    while queue:
        x, y, step = queue.pop(0)

        if x == m - 1 and y == n - 1:
            return step

        for movex, movey in direction:
            nx = x + movex
            ny = y + movey

            if 0 <= nx < m and 0 <= ny < n and not walked[ny][nx] and a[ny][nx] == 0:
                queue.append((nx, ny, step + 1))
                walked[ny][nx] = True

    return -1

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(bfs(n, m, a))