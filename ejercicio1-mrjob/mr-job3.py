from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
       
        try:
            yield (line.split(',')[0]), int(line.split(',')[1])
        except:
            yield line.split(',')[0], 0

    def reducer(self, key, values):
        lista = []
        for item in values:
            if not item in lista:
                lista.append(item)
        yield key, len(lista)
    


MRWordFrequencyCount.run()
