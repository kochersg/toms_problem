from dataclasses import dataclass
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


def main():
    pass

if __name__=="__main__":
    main()