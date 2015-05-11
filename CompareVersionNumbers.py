#!/usr/bin/env python
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        list_1 = map(int, version1.split('.'))
        list_2 = map(int, version2.split('.'))
        length1, length2 = len(list_1), len(list_2)
        if length1 < length2:
            list_1.extend([0 for i in range(length2-length1)])
        if length1 > length2:
            list_2.extend([0 for i in range(length1-length2)])
        for x, y in zip(list_1, list_2):
            if x > y:
                return 1
            elif x < y:
                return -1
        return 0
    '''
    def compareVersion(self, version1, version2):
        v1 = (int(n) for n in version1.split('.'))
        v2 = (int(n) for n in version2.split('.'))
        for n1, n2 in izip_longest(v1, v2, fillvalue=0):
            if n1> n2:
                return 1
            elif n1< n2:
                return -1
        else:
            return 0
    '''