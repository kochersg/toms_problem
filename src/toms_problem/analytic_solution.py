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
    articles_per_place=distribute_articles_on_places(problem = problem)
    for ix, sel in enumerate(selection_distribution):
        res *= math.comb(articles_per_place[ix], sel)
    return res / math.comb(problem.n_articles, problem.n_searched_articles)

def distribute_articles_on_places(problem: problem.Problem) -> list[int]:
    res = [0 for _ in range(problem.n_places)]
    for ix in range(problem.n_articles):
        res[ix%problem.n_places]+=1
    return res
    

def find_combination_list(problem: problem.Problem) -> list[list[int]]:
    res = []
    ix = 0
    while True:
        r = numberToBase(ix, problem.n_searched_articles+1)
        if len(r)==problem.n_places:
            if r[0]==problem.n_searched_articles:
                res.append(r)
                break
        if sum(r)==problem.n_searched_articles:
            res.append(copy.deepcopy(r))
        ix += problem.n_searched_articles
    return res

def get_combi_length(combi: list[int]) -> int:
    l = 0
    for c in combi:
        if c != 0:
            l += 1
    return l

def sort_combinations_to_number_of_searches(combinations: list[int]):
    res = {}
    for c in combinations:
        combi_len = get_combi_length(combi=c)
        if combi_len in res.keys():
            res[combi_len].append(c)
        else:
            res[combi_len]=[c]
    return res

def calc_prob_of_selection_list(problem: problem.Problem, sel_list: list[list[int]]) -> float:
    res = 0.0
    for combi in sel_list:
        res+=calc_selection_probability(problem=problem, selection_distribution=combi)
    return res


def calc_probability_distribution(problem: problem.Problem, combi_dict: dict[int, list[list[int]]]) -> list[int, int]:
    res = []
    for c in combi_dict:
        res.append([c, calc_prob_of_selection_list(problem=problem, sel_list = combi_dict[c])])
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
    p = problem.Problem(n_articles=105, n_places=7, n_searched_articles=10)
    print(c:=find_combination_list(problem=p))
    print(d:=sort_combinations_to_number_of_searches(combinations=c))
    print(r:=calc_probability_distribution(problem=p, combi_dict=d))
    print(sum([c[1] for c in r]))

def calc_solution(n_articles: int, n_places: int, n_searched_articles: int) -> None:
    p = problem.Problem(n_articles=n_articles, n_places=n_places, n_searched_articles=n_searched_articles)
    c=find_combination_list(problem=p)
    d=sort_combinations_to_number_of_searches(combinations=c)
    r=calc_probability_distribution(problem=p, combi_dict=d)
    print(r)
    # print(sum([c[1] for c in r]))





def main():
    pass

if __name__=="__main__":
    main()