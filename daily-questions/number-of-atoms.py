from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        ind = 0

        def traverse():
            nonlocal ind, formula
            result = defaultdict(int)
            word, current, count = "", {}, 0
            while ind < len(formula) and formula[ind] != ")":
                if not formula[ind].isdigit() and formula[ind].isupper() or formula[ind] == "(":
                    for w, c in current.items():
                        result[w] += c * max(count, 1)
                if formula[ind].isdigit():
                    count = count * 10 + int(formula[ind])
                elif formula[ind].isupper():
                    word, current, count = formula[ind], {formula[ind]: 1}, 0
                elif formula[ind].islower():
                    word = word + formula[ind]
                    current, count = {word: 1}, 0
                else:
                    ind += 1
                    current, count = traverse(), 0
                ind += 1
            for w, c in current.items():
                result[w] += c * max(count, 1)

            return result

        res = traverse()
        return "".join((w + (str(c) if c > 1 else "")) for w, c in sorted(res.items()))


if __name__ == "__main__":
    print(Solution().countOfAtoms("Mg2(P2O5)3"))
