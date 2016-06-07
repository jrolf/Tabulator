


# A Counter mechanism to keep track of
# all incidences of a vote.
class FB_Tabulator:
    def __init__(self):
        self.tab = {}
        self.SUM = 0

    # Adds multiple counts of one name to the tabulator:
    def add(self,name,Num=1.0):
        self.SUM += Num
        if name in self.tab: self.tab[name]+= Num
        else:                self.tab[name] = Num

    # Returns the number of counted instances of 'name':
    def num(self,name):
        if name in self.tab: number = self.tab[name]
        else:                number = 0
        return number

    # Returns the name of the item with the highest count:
    def best(self):
        name = 0
        topV = 0
        for a in self.tab:
            val = self.tab[a]
            if val > topV:
                topV = val
                name = a
        return name

    # Returns list of accounts sorted by
    # highest count to lowest.
    def results(self):
        Results = []
        for a in self.tab:
            val = self.tab[a]
            Results.append([val,a])
        Results.sort()
        Results.reverse()
        return Results
    
    # Returns all account names:
    def accounts(self):
        return [a for a in self.tab]

    # Returns List of names of top N accounts:
    def topN(self,N=3):
        tops = nlargest(N, list(self.tab.items()), key=itemgetter(1))
        return [a[0] for a in tops]
        
        
