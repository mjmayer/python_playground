import unittest
import pdb


def countingValleys(n, s):
    # creatoes generator that outputs 1 if the step is U and -1 else
    stepasint = (1 if x == 'U' else -1 for x in s)
    sealevel = 0
    valleys = 0
    previouslevel = 0
    for x in stepasint:
        sealevel += x
        print("Sealevel: " + str(sealevel))
        print("Previouslevel: " + str(previouslevel))
        if sealevel == 0 and previouslevel == -1:
            valleys += 1
        previouslevel = sealevel
    return(valleys)


class countingValleysTest(unittest.TestCase):

    def testcase1(self):
        # pdb.set_trace()
        self.assertEquals(countingValleys(8, 'UDDDUDUU'), 1)

    def testcase2(self):
        # pdb.set_trace()
        self.assertEquals(countingValleys(12, 'DDUUDDUDUUUD'), 2)

    def testcaste3(self):
        pdb.set_trace()
        self.assertEqual(countingValleys(10, 'DUDDDUUDUU'), 2)
