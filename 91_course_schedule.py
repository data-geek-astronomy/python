def can_finish(num_courses, prerequisites):
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    state = [0] * num_courses  # 0=unvisited, 1=visiting, 2=done

    def has_cycle(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = 2
        return False

    return not any(has_cycle(c) for c in range(num_courses))

if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
