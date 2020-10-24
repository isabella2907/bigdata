from mrjob.job import MRJob
from mrjob.step import MRStep
import csv


class MostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_finf_max)
        ]

    # mapper
    def mapper_get_ratings(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split('\t')
        yield movie_id, 1
        pass

    # first reducer
    def reducer_count_ratings(self, movie_id, count):
        yield 1, (sum(count), movie_id)
        pass

    # second reducer
    def reducer_find_max'(self, movie_id, rating):
        yield max(values)
        pass


if __name__ == '__main__':
    MostPopularMovie.run()
