"""Basic HyperLogLog:

This implementation is from the website,
https://github.com/Parsely/python-pds, but has been modified to remove
the dependency on the "smhasher" module and so that it can be run
using the Anaconda Python distribution.

To find the modifications, look for inline comments that begin with '# !!! '
"""

import numpy as np
from sklearn import utils

class HyperLogLog(object):
    """ Basic Hyperloglog """

    def __init__(self, error_rate, seed=0):  # !!! Added argument, seed.
        b = int(np.ceil(np.log2((1.04 / error_rate) ** 2)))
        self.precision = 64
        self.alpha = self._get_alpha(b)
        self.b = b
        self.m = 1 << b
        self.M = np.zeros(self.m, dtype=np.uint8)
        self.bitcount_arr = [ 1L << i for i in range(self.precision - b + 1) ]
        #self.hashes = get_raw_hashfunctions()
        self.hashes = utils.murmurhash3_32  # !!! Modified line above
        self.seed = seed  # !!! Added attribute

    @staticmethod
    def _get_alpha(b):
        if not (4 <= b <= 16):
            raise ValueError("b=%d should be in range [4 : 16]" % b)
        if b == 4:
            return 0.673
        if b == 5:
            return 0.697
        if b == 6:
            return 0.709
        return 0.7213 / (1.0 + 1.079 / (1 << b))

    def _get_rho(self, w, arr):
        """ Return the least signifiant bit
            O(N) in the worst case
        """
        lsb = 0
        while not (w & arr[lsb]):
            lsb += 1
        return lsb+1

    def add(self, uuid):
        """ Adds a key to the HyperLogLog """
        if uuid:
            # Computing the hash
            try:
                #x = smhasher.murmur3_x86_64(uuid)
                x = utils.murmurhash3_32(uuid, self.seed, True)  # !!! Modified line above
            except UnicodeEncodeError:
                #x = smhasher.murmur3_x86_64(uuid.encode('ascii', 'ignore'))
                x = utils.murmurhash3_32(uuid.encode('ascii', 'ignore'), self.seed, True)  # !!! Modified line above
            # Finding the register to update by using thef first b bits as an index
            j = x & ((1 << self.b) - 1)
            # Remove those b bits
            w = x >> self.b
            # Find the first 0 in the remaining bit pattern
            self.M[j] = max(self.M[j], self._get_rho(w, self.bitcount_arr))

    def __len__(self, M = None):
        """ Returns the estimate of the cardinality """
        return self.estimate()

    def __or__(self, other_hll):
        """  Perform a union with another HLL object. """
        other_hll_M = other_hll.M
        self.M = reduce(lambda x,y: np.maximum(x,y), [self.M,other_hll_M]).astype(np.int16)
        return self

    def estimate(self):
        """ Returns the estimate of the cardinality """
        E = self.alpha * float(self.m ** 2) / np.power(2.0, -self.M).sum()
        if E <= 2.5 * self.m:             # Small range correction
            V = self.m - np.count_nonzero(self.M)
            return int(self.m * np.log(self.m / float(V))) if V > 0 else int(E)
        elif E <= float(1L << self.precision) / 30.0:  #intermidiate range correction -> No correction
            return int(E)
        else:
            return int(-(1L << self.precision) * np.log(1.0 - E / (1L << self.precision)))
