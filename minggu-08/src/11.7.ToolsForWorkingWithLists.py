# Modul array menyediakan array() objek yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih kompak
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
# 26932         output
a[1:3]
array('H', [10, 700])


# Modul collection smenyediakan deque() objek yang seperti daftar dengan penambahan dan kemunculan yang lebih cepat dari sisi kiri tetapi pencarian yang lebih lambat di tengah
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
# Handling task1            output

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)


# Selain implementasi daftar alternatif, perpustakaan juga menawarkan alat lain seperti bisect modul dengan fungsi untuk memanipulasi daftar yang diurutkan
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores
# [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]           output


# Modul heapq menyediakan fungsi untuk mengimplementasikan tumpukan berdasarkan daftar reguler.
# Entri bernilai terendah selalu disimpan di posisi nol
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries
# [-5, 0, 1]                       output