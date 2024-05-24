from dataclasses import dataclass, field
import random as rand

@dataclass
class Article:
    id: int
    place: int

@dataclass
class Problem:
    n_articles: int
    n_places: int
    n_searched_articles: int
    data: list[Article]|None = None

    def init_problem(self):
        self.data=[]
        places = self.init_places()
        for id in range(self.n_articles):
            self.data.append(
                Article(
                    id = id,
                    place = places[id]
                )
            )

    def init_places(self):
        places = []
        ix = 0
        while ix<self.n_articles:
            for p in range(self.n_places):
                places.append(p)
                ix+=1
        places=rand.sample(population=places, k=self.n_articles)
        return places

    def search_articles(self):
        return rand.sample(population=self.data, k=self.n_searched_articles)
    
    def calc_place_counts(self, search_list: list[Article])->dict[int,float]:
        res = {}
        for a in search_list:
            if a.place in res:
                res[a.place]+=1.0
            else:
                res[a.place]=1.0
        return res
    
    @staticmethod
    def get_number_of_visited_places(input: dict[int,int]):
        return len(input.keys())

@dataclass
class MC:
    problem: Problem
    n_runs: int=0
    stat: dict[int,int] = field(default_factory=lambda:{})
    probabilities: list[int, float] = field(default_factory=lambda:[])

    def add_run_to_stat(self):
        self.problem.init_problem()
        n_v_p = self.problem.get_number_of_visited_places(
            self.problem.calc_place_counts(
                self.problem.search_articles()
                )
            )
        if n_v_p in self.stat.keys():
            self.stat[n_v_p]+=1
        else:
            self.stat[n_v_p]=1
        self.n_runs+=1

    def calc_probabilities(self):
        for r in sorted(self.stat.keys()):
            self.probabilities.append([r, self.stat[r]/self.n_runs])

def test():
    p = Problem(n_articles=10, n_places=2, n_searched_articles=5)
    mc = MC(problem=p)
    print(mc)
    while mc.n_runs<10000:
        mc.add_run_to_stat()
    mc.calc_probabilities()
    print(mc.probabilities)

def calc_MC(n_articles: int, n_places: int, n_searched_articles: int, n_MC_runs: int)->None:
    p = Problem(n_articles=n_articles, n_places=n_places, n_searched_articles=n_searched_articles)
    mc = MC(problem=p)
    while mc.n_runs<n_MC_runs:
        mc.add_run_to_stat()
    mc.calc_probabilities()
    print(mc)
    print(mc.probabilities)


def main():
    pass

if __name__=="__main__":
    main()