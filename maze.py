import utils
import power

max_relocate = 300

def init_graph(size):
    size = get_world_size()
    graph = {}
    x, y = utils.get_pos()
    for i in range(size):
        for j in range(size):
            graph[(i,j)] = []
    return graph

def dfs(visited, graph):
    x, y = utils.get_pos()
    visited.add((x,y))
    for dx, dy in utils.VECTORS:
        xx, yy = x + dx, y + dy
        if (xx,yy) in visited:
            continue
        r = utils.move_to(xx,yy)
        if not r:
            continue
        graph[(x,y)].append((xx,yy))
        graph[(xx,yy)].append((x,y))
        r = dfs(visited, graph)
        if r:
            return True
        utils.move_to(x,y)

def pop_index(queue, treasure):
    result = 0
    min_cost = get_world_size()**2
    for i in range(len(queue)):
        pos = queue[i]
        dist = utils.dist(pos, treasure)
        if dist < min_cost:
            min_cost = dist
            result = i
    return result

def backtrack(trace, treasure):
    path = [treasure]
    node = treasure
    while node in trace:
        node = trace[node]
        path.append(node)
    return path[::-1]

def bfs(graph):
    pos = utils.get_pos()
    visited = {pos}
    queue = [pos]
    treasure = measure()
    trace = {}
    while queue:
        # qi = pop_index(queue, treasure)
        qi = 0
        time = get_time()
        pos = queue.pop(qi)
        if pos == treasure:
            path = backtrack(trace, treasure)
            return path
        for n in graph[pos]:
            if n in visited:
                continue
            queue.append(n)
            visited.add(n)
            trace[n] = pos
    return []

def update_graph(graph):
    pos = utils.get_pos()
    x, y = pos
    for i in range(len(utils.VECTORS)):
        dx, dy = utils.VECTORS[i]
        d = utils.DIRECTIONS[i]
        n = x + dx, y + dy
        if n not in graph[pos] and can_move(d):
            graph[pos].append(n)
            graph[n].append(pos)

def move_path(path, graph):
    for pos in path:
        x, y = pos
        utils.move_to(x, y)
        update_graph(graph)

def maze(size=8, goal=9863168):
    for i in range(2):
        print(".")
    amount = 2**5 * size
    x, y = utils.get_pos()
    while True:
        utils.move_to(x,y)
        plant(Entities.Bush)
        use_item(Items.Weird_Substance, amount)
        graph = init_graph(size)
        dfs(set(), graph)
        for i in range(max_relocate):
            path = bfs(graph)
            move_path(path, graph)
            use_item(Items.Weird_Substance, amount)
            if goal and num_items(Items.Gold) >= goal:
                return
        harvest()

def single():
    goal = 616448
    size = 8
    amount = 2**5 * size
    x, y = utils.get_pos()
    stats = {
        "time_bfs": 0,
        "time_move": 0,
        "num_moves": 0,
        "time_move_all": [],
        "num_moves_all": [],
    }
    
    while True:
        time = get_time()
        utils.move_to(x,y)
        plant(Entities.Bush)
        use_item(Items.Weird_Substance, amount)
        graph = init_graph(size)
        dfs(set(), graph)
        quick_print("dfs =", get_time() - time)

        for i in range(max_relocate):
            time = get_time()
            path = bfs(graph)
            stats["num_moves"] += len(path)
            stats["num_moves_all"].append(len(path))
            stats["time_bfs"] += get_time() - time

            time = get_time()
            move_path(path, graph)
            stats["time_move"] += get_time() - time
            stats["time_move_all"].append(get_time() - time)
            use_item(Items.Weird_Substance, amount)

            if num_items(Items.Gold) >= goal:
                for k in stats:
                    quick_print(k, "=", stats[k])
                return
        harvest()

def multi():
    cols, rows = 4, 4
    w = get_world_size() // cols
    h = get_world_size() // rows
    for i in range(cols):
        for j in range(rows):
            utils.move_to(i * w + w//2, j * h + h//2)
            spawn_drone(maze)
        move(East)

def main():
    cols, rows = 4, 4
    w = get_world_size() // cols
    h = get_world_size() // rows
    for i in range(cols):
        for j in range(rows):
            utils.move_to(i * w + w//2, j * h + h//2)
            if (i, j) == (cols-1, rows-1):
                break
            spawn_drone(maze)
        move(East)
    utils.idle(Items.Gold)


if __name__ == "__main__":
    single()
    # multi()
