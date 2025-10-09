"""
    Tìm kiếm sâu: Depth First Search

    Bài toán đong nước:
        + b1, b2 với max dung tích là m, n. Cần đong k lít
        + Mỗi đỉnh là một trạng thái:
            + Là đối tượng: x, y, isVisited
            + Hàm chuyển trạng thái: đổ hết, đổ từ a->b, đổ đầy
        + Open là stack: có thể dùng list


"""
from collections import deque


class State:
    def __init__(self, b1=0, b2=0):
        self.b1 = b1
        self.b2 = b2
    def tap_lien_ke(self, m, n):
        # Sử dụng set để lưu tập liền kề, tránh giá trị trùng lặp
        T = set()
        x = self.b1
        y = self.b2

        state_doday1 = State(m, y)
        state_doday2 = State(x, n)

        state_dohet1 = State(0, y)
        state_dohet2 = State(x, 0)

        state_do1sang2 = State(0, x + y) if x + y <= n else State(x + y - n , n)

        state_do2sang1 = State(x + y, 0) if x + y <= m else State(m, x + y - m)

        T.update([state_dohet1, state_dohet2, state_doday1, state_doday2, state_do1sang2, state_do2sang1])

        return list(T)

    def __eq__(self, other):
        return isinstance(other, State) and self.b1 == other.b1 and self.b2 == other.b2

    def __hash__(self):
        return hash((self.b1, self.b2))


def in_duong_di(parent, goal, start):
    path = [goal]
    while goal != start:
        goal = parent[goal]
        path.append(goal)

    path.reverse()

    for index, state in enumerate(path):
        print(f"({state.b1}, {state.b2})", end="")
        if index != len(path) - 1:
            print(f" -> ", end="")
    print()

def depth_first_search(m, n, k):


    #1. Thêm start vào open
    start = State(b1=0, b2=0)
    open, close, parent = [start], set(), {}

    # 2. Chạy vòng lặp: lấy trong stack open ra nếu còn
    while open:
        current: State = open.pop()

        # Cho đỉnh vào close
        close.add(current)

        # 2.0 So sánh với goals
        if current.b1 == k or current.b2 == k:
            in_duong_di(parent, current, start)
            return

        # 2.1 Tìm tập các đỉnh kề (các trạng thái kế tiếp)
        # 2.2 Đưa các phần tử trong tập đỉnh kề vào open với điều kiện:
        for next in current.tap_lien_ke(m, n):
            if next not in open and next not in close:
                open.append(next)

                # 2.3 Ghi lại đường đi
                parent[next] = current

"""
    Tìm kiếm rộng:
        + Open: queue
"""
def breadth_first_search(m, n, k):
    #1. Thêm start vào open
    start = State(b1=0, b2=0)
    queue = deque()
    queue.append(start)

    close, parent = set(), {}

    # 2. Chạy vòng lặp: lấy trong stack open ra nếu còn
    while queue:
        current: State = queue.popleft()

        # Cho đỉnh vào close
        close.add(current)

        # 2.0 So sánh với goals
        if current.b1 == k or current.b2 == k:
            in_duong_di(parent, current, start)
            return

        # 2.1 Tìm tập các đỉnh kề (các trạng thái kế tiếp)
        # 2.2 Đưa các phần tử trong tập đỉnh kề vào open với điều kiện:
        for next in current.tap_lien_ke(m, n):
            if next not in queue and next not in close:
                queue.append(next)

                # 2.3 Ghi lại đường đi
                parent[next] = current

if __name__ == "__main__":
    print("Tìm kiếm sâu DFS:")
    depth_first_search(5, 4, 3)

    print("Tìm kiếm rộng BFS:")
    breadth_first_search(5, 4, 3)






