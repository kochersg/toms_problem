import math
import toms_problem.problem as problem
import copy

def calc_selection_probability(problem: problem.Problem, selection_distribution: list[int])->float:
    if len(selection_distribution)>problem.n_places:
        print("Selection invalid: more entries in selection_distribution than storage places")
        return 0.0
    if sum(selection_distribution)!=problem.n_searched_articles:
        print("Selection invalid: more searched articles in selection then number of searched articles in problem")
        return 0.0
    res = 1.0
    for sel in selection_distribution:
        res *= math.comb(problem.n_searched_articles, sel)
    return res / math.comb(problem.n_articles, problem.n_searched_articles)

def find_combinations(problem: problem.Problem) -> list[list[int]]:
    res = []
    ix = 0
    while True:
        r = numberToBase(ix, problem.n_searched_articles+1)
        print(r)
        if len(r)==problem.n_places:
            if r[0]==problem.n_searched_articles:
                break
        if sum(r)==problem.n_searched_articles:
            res.append(copy.deepcopy(r))
        ix += 1
    return res

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def math_test():
    p = problem.Problem(n_articles=21, n_places=3, n_searched_articles=5)
    print(calc_selection_probability(problem=p, selection_distribution=[3,1,1]))
    print(find_combinations(problem=p))



def main():
    pass

if __name__=="__main__":
    main()