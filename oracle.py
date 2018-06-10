
class Query:
    def __init__(self, machine, input, probability):
        self.machine = machine
        self.input = input
        self.probability = probability

class KOracle:
    def __init__(self, k):
        self.k = k

    def ask(self, query):
        machine = query.machine
        # TODO: Oracle here is not self, it's a fake oracle.
        result = machine('', oracle=self, steps=self.k)
        return result

class Oracle:
    def __init__(self):
        pass

    def ask(self, query):
        k = 0

# @return [List<String>] The output after running for `steps` steps.
def eventual_truth(input, *, oracle, steps):
    counter = 10
    for _ in range(steps):
        if counter == 0:
            return True
        counter -= 1

    return None

if __name__ == "__main__":
    oracle = KOracle(11)
    print(
      oracle.ask(Query(eventual_truth, '', 0.8))
    )
