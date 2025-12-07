from matchers import And, All, Or, Not, HasFewerThan, HasAtLeast, PlaysIn
import matchers

class QueryBuilder:
    def __init__(self, matcher=None):
        if matcher is None:
            self.matcher = All()
        else:
            self.matcher = matcher

    def plays_in(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))

    def one_of(self, *builders: 'QueryBuilder'):
        return QueryBuilder(Or(*[builder.build() for builder in builders]))

    def build(self):
        return self.matcher
