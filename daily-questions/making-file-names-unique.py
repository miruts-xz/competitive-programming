class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        smallest = defaultdict(int)
        res = []
        for name in names:
            if name in smallest:
                pname = f'{name}({smallest[name]})'
                while pname in smallest:
                    smallest[name] += 1
                    pname = f'{name}({smallest[name]})'
                res.append(f'{name}({smallest[name]})')
                smallest[f'{name}({smallest[name]})'] += 1
            else:
                res.append(name)
            smallest[name] += 1
        return res
