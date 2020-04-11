from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
       
        try:
            yield (line.split(',')[0]), int(line.split(',')[1])
        except:
            yield line.split(',')[0], 0

    def reducer(self, key, values):
        yield key, len(list(values))
    


MRWordFrequencyCount.run()