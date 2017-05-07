import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # TODO: Implement create_dfs
    cell_index = random.randrange(0, m.total_cells)
    visited_cells = 1
    backtrack_stack = [cell_index]

    while visited_cells < m.total_cells:
        # print("visited_cells", visited_cells)
        # print("m.total_cells", m.total_cells)
        # print("Start loop. cell_index: ", cell_index)
        cell_neighbors = m.cell_neighbors(cell_index)
        # print("cell_neighbors of ", cell_index, ":", cell_neighbors)
        if len(cell_neighbors) > 0:
            new_cell = random.sample(cell_neighbors, 1)[0]
            # print("new_cell: ", new_cell)
            m.connect_cells(cell_index, new_cell[0], new_cell[1])
            cell_index = new_cell[0]
            backtrack_stack.append(cell_index)
            visited_cells += 1
        else:
            cell_index = backtrack_stack.pop(len(backtrack_stack) - 1)
        m.refresh_maze_view()
    print("Initiate solve...")
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    main()
