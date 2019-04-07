"""
Stores information about the UCO-LAEO database

(c) MJMJ/2018
"""


class UcoLAEOdb():

    def __init__(self, partition=1):

        self.partition = partition

    def getPartitionConfig(self):

        if self.partition == 1:   #   CVPR'2019
                validationVids = ['got01', 'got03',
                                  'mr01',  'mr03',
                                  'sv02', 'sv04',
                                  'twd01', 'twd02']

                testVids = ['got05', 'got06', 'got08',
                            'mr04', 'mr05', 'mr06', 'mr10',
                            'sv03', 'sv06', 'sv10',
                            'twd03', 'twd04', 'twd05', 'twd06', 'twd07']

        return validationVids, testVids
