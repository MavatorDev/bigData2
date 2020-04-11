from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
       
        try:
            yield (line.split(',')[1]), int(line.split(',')[2])
        except:
            yield line.split(',')[1], 0

    def reducer(self, key, values):
        lista = []
        for item in values:
            lista.append(item)
        yield key, sum(lista)/len(lista)
    


MRWordFrequencyCount.run()