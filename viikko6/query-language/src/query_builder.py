from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or


class QueryBuilder:
    def __init__(self):
        self._all = All()
        self._and = And(self._all)

    def build(self):
        return self._and

    def playsIn(self, team):
        self._and = And(self._and, PlaysIn(team))
        return self._and

    def hasAtLeast(self, value, attr):
        self._all = HasAtLeast(value, attr)

    def hasFewerThan(self, value, attr):
        self._all = HasFewerThan(value, attr)
