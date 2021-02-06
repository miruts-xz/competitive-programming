"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_subor = [[]] * 2001
        for e in employees:
            id_subor[e.id] = [e.importance, e.subordinates]
        return self.countImportance(id_subor, id)

    def countImportance(self, id_subor, id: int) -> int:
        data = id_subor[id]
        if data[1]:
            m = []
            for s in data[1]:
                m.append(self.countImportance(id_subor, s))
            return data[0] + sum(m)
        return data[0]
