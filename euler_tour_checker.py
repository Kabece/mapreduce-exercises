from mrjob.job import MRJob

class EulerTourChecker(MRJob):

    def mapper(self, _, line):
        for node in line.split():
            yield (node, 1)

    def reducer(self, node, count):
        yield (node, sum(count) % 2 == 0)

if __name__ == '__main__':
    EulerTourChecker.run()