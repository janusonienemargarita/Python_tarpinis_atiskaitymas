# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD,
# tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def wasExpensive(self):
        if self.budget > 100000000:
            print("TRUE",",", "movie was expensive")
        else:
            print("FALSE",",", "movie was on budget")

    
drama = Movie("Vikings", "Andrey Kravchuk", 4500000000)
action = Movie("Indiana Jones","James Mangold", 2100000)
    
    
drama.wasExpensive()
action.wasExpensive()