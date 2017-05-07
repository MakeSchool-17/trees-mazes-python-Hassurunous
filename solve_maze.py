import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    backtrack_stack = list()
    curr_cell = 0
    visited_cells = 0
    goal = len(m.maze_array) - 1

    while curr_cell != goal:
        # print("Onward! To victory!")
        cell_neighbors = m.cell_neighbors(curr_cell)
        if len(cell_neighbors) > 0:
            new_cell = random.sample(cell_neighbors, 1)[0]
            m.visit_cell(curr_cell, new_cell[0], new_cell[1])
            backtrack_stack.append(curr_cell)
            curr_cell = new_cell[0]
            visited_cells += 1
        else:
            m.backtrack(curr_cell)
            curr_cell = backtrack_stack.pop(len(backtrack_stack) - 1)
        m.refresh_maze_view()
    m.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    queue = list()
    curr_cell = 0
    visited_cells = 0
    in_direction = 0b0000
    goal = len(m.maze_array) - 1
    queue.append((curr_cell, in_direction))

    while curr_cell != goal and len(queue) > 0:
        next_queued_item = queue.pop(0)
        curr_cell, in_direction = next_queued_item[0], next_queued_item[1]
        m.bfs_visit_cell(curr_cell, in_direction)
        visited_cells += 1
        m.refresh_maze_view

        for cell in m.cell_neighbors(curr_cell):
            queue.append(cell)

    for cell in queue:
        m.reconstruct_solution(cell[0])

    m.state = 'idle'


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('bfs')
