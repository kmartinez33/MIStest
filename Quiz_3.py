ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self_title = name
        winning_states= [ELECTORS]

        

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return 
    

    def win_state(self, state):
        """Adds a tate to winning_states and updates votes.
        state: a string of state abbreviation
        """
        pass


def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'])
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()