import heapq
import tkinter as tk
from tkinter import ttk

SIZE = 10
CELL = 48
DEFAULT_BLOCKS = {(1, 3), (2, 3), (3, 3), (4, 3), (4, 6), (5, 6), (6, 6), (2, 7)}

class EvacuationApp:
    def __init__(self, root):
        self.root = root
        root.title('A* Emergency Evacuation Route Planner')
        root.resizable(False, False)
        self.mode = tk.StringVar(value='block')
        self.status = tk.StringVar(value='Choose a tool, edit the grid, then click Find Route.')
        self.start = (0, 0)
        self.goal = (9, 9)
        self.blocked = set(DEFAULT_BLOCKS)
        self.path = []
        self.explored = []
        self.steps = []
        self.step_index = 0
        self.build_ui()
        self.draw()

    def build_ui(self):
        frame = ttk.Frame(self.root, padding=14)
        frame.pack()
        ttk.Label(frame, text='Emergency Evacuation Route Planner', font=('Arial', 18, 'bold')).pack(anchor='w')
        ttk.Label(frame, text='A* heuristic search | Click the grid to change the scenario').pack(anchor='w', pady=(2, 10))
        controls = ttk.Frame(frame)
        controls.pack(fill='x', pady=(0, 8))
        for value, title in [('block', 'Block / Unblock'), ('start', 'Set Student'), ('goal', 'Set Exit')]:
            ttk.Radiobutton(controls, text=title, variable=self.mode, value=value).pack(side='left', padx=(0, 12))
        self.canvas = tk.Canvas(frame, width=SIZE * CELL, height=SIZE * CELL, bg='white', highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.click)
        actions = ttk.Frame(frame)
        actions.pack(fill='x', pady=10)
        ttk.Button(actions, text='Find Route', command=self.find_route).pack(side='left', padx=(0, 8))
        ttk.Button(actions, text='Next Search Step', command=self.next_step).pack(side='left', padx=(0, 8))
        ttk.Button(actions, text='Clear Path', command=self.clear_path).pack(side='left', padx=(0, 8))
        ttk.Button(actions, text='Reset Grid', command=self.reset).pack(side='left')
        ttk.Label(frame, text='Green: student  |  Blue: exit  |  Red: blocked  |  Yellow: route  |  Pale blue: explored').pack(anchor='w')
        ttk.Label(frame, textvariable=self.status, wraplength=480, justify='left').pack(anchor='w', pady=(8, 0))

    def click(self, event):
        cell = (event.y // CELL, event.x // CELL)
        if not all(0 <= n < SIZE for n in cell):
            return
        mode = self.mode.get()
        if mode == 'block' and cell not in (self.start, self.goal):
            if cell in self.blocked:
                self.blocked.remove(cell)
            else:
                self.blocked.add(cell)
        elif mode == 'start' and cell != self.goal and cell not in self.blocked:
            self.start = cell
        elif mode == 'goal' and cell != self.start and cell not in self.blocked:
            self.goal = cell
        else:
            self.status.set('Cannot place a start, exit, or obstacle on that cell.')
            return
        self.clear_path()

    def heuristic(self, cell):
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])

    def search(self):
        queue = [(self.heuristic(self.start), 0, self.start)]
        distance = {self.start: 0}
        parent = {self.start: None}
        explored = []
        closed = set()
        while queue:
            f, g, cell = heapq.heappop(queue)
            if cell in closed or g != distance[cell]:
                continue
            closed.add(cell)
            explored.append((cell, g, self.heuristic(cell), f))
            if cell == self.goal:
                path = []
                while cell is not None:
                    path.append(cell)
                    cell = parent[cell]
                return path[::-1], explored
            r, c = cell
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                nxt = (nr, nc)
                if not (0 <= nr < SIZE and 0 <= nc < SIZE) or nxt in self.blocked or nxt in closed:
                    continue
                ng = g + 1
                if ng < distance.get(nxt, float('inf')):
                    distance[nxt] = ng
                    parent[nxt] = cell
                    heapq.heappush(queue, (ng + self.heuristic(nxt), ng, nxt))
        return [], explored

    def find_route(self):
        self.path, self.steps = self.search()
        self.explored = [s[0] for s in self.steps]
        self.step_index = len(self.steps)
        if self.path:
            self.status.set(f'Route found! {len(self.path) - 1} moves; {len(self.steps)} cells explored. Change obstacles to test again.')
        else:
            self.status.set(f'No route available. {len(self.steps)} cells explored. Remove obstacles and try again.')
        self.draw()

    def next_step(self):
        if not self.steps or self.step_index >= len(self.steps):
            self.path = []
            _, self.steps = self.search()
            self.step_index = 0
        self.step_index += 1
        self.explored = [s[0] for s in self.steps[:self.step_index]]
        cell, g, h, f = self.steps[self.step_index - 1]
        self.status.set(f'Step {self.step_index}/{len(self.steps)}: expanded {cell}; g={g}, h={h}, f={f}.')
        self.draw()

    def clear_path(self):
        self.path = []
        self.explored = []
        self.steps = []
        self.step_index = 0
        self.status.set('Grid updated. Click Find Route or Next Search Step.')
        self.draw()

    def reset(self):
        self.start = (0, 0)
        self.goal = (9, 9)
        self.blocked = set(DEFAULT_BLOCKS)
        self.clear_path()

    def draw(self):
        self.canvas.delete('all')
        path_set = set(self.path)
        explored_set = set(self.explored)
        for r in range(SIZE):
            for c in range(SIZE):
                cell = (r, c)
                color = '#F5F7FA'
                label = ''
                if cell in explored_set:
                    color = '#D7EAF9'
                if cell in path_set:
                    color = '#FFE58A'
                if cell in self.blocked:
                    color = '#F4B6B6'
                    label = 'X'
                if cell == self.start:
                    color, label = '#A6DFB4', 'S'
                elif cell == self.goal:
                    color, label = '#A8D6F0', 'E'
                x, y = c * CELL, r * CELL
                self.canvas.create_rectangle(x, y, x + CELL, y + CELL, fill=color, outline='#B9C4CE')
                if label:
                    self.canvas.create_text(x + CELL / 2, y + CELL / 2, text=label, font=('Arial', 16, 'bold'))

if __name__ == '__main__':
    root = tk.Tk()
    EvacuationApp(root)
    root.mainloop()
