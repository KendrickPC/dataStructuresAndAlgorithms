class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

    
# A class that produces an arithmetic progression.
class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


# A class that produces a geometric progression.
class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

# A class that produces a Fibonacci progression
class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first


    def _advanced(self):
        self._prev, self._current = self._current, self._prev + self._current


# Output of the unit tests from Code Fragment
if __name__ == '__main__':
    print('\nDefault progression:')
    Progression().print_progression(10)

    print('\nArithmetic Progression')
    ArithmeticProgression(5).print_progression(10)

    print('\nGeometric Progression with default base:')
    GeometricProgression().print_progression(10)

    print('\nGeometric Progression with default base:')
    GeometricProgression(3).print_progression(10)
    
    print('\nGeometric Progression with default base:')
    FibonacciProgression().print_progression(10)

    print('\nGeometric Progression with default base:')
    FibonacciProgression(4, 6).print_progression(10)


