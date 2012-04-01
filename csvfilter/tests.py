import unittest

from csvfilter import Processor

SAMPLE_CSV = ['a,b,c', 'd,e,f', 'g,h,i']
SAMPLE_PSV = ['a|b|c', 'd|e|f', 'g|h|i']

SAMPLE_QUOTED_CSV = [
'"Pcode","Locality","State","Comments","DeliveryOffice","PresortIndicator","ParcelZone","BSPnumber","BSPname","Category","Lat","Long"',
'"0200","AUSTRALIAN NATIONAL UNIVERSITY","ACT","PO Boxes","AUSTRALIAN NATIONAL UNI LPO x","150","N2 ","019","CANBERRA","Post Office Boxes ","-35.277272","149.117136"',
'"0221","BARTON","ACT","LVR Special Mailing",,"150","N2 ","019","CANBERRA","LVR ","-35.201372","149.095065"'
]


class ProcessorTests(unittest.TestCase):

    def test_no_config_does_no_processing(self):
        p = Processor()
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], output)

    def test_single_col_plucking(self):
        p = Processor(fields=[0])
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['a'], ['d'], ['g']], output)

    def test_validator(self):
        p = Processor()
        p.add_validator(lambda row: row[0] == 'a')
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['a', 'b', 'c']], output)

    def test_multiple_col_plucking(self):
        p = Processor(fields=[0, 2])
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['a', 'c'], ['d', 'f'], ['g', 'i']], output)

    def test_multiple_col_plucking_with_reordering(self):
        p = Processor(fields=[2, 1])
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['c', 'b'], ['f', 'e'], ['i', 'h']], output)

    def test_single_col_dropping(self):
        p = Processor(fields=[1], invert=True)
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['a', 'c'], ['d', 'f'], ['g', 'i']], output)

    def test_multiple_col_dropping(self):
        p = Processor(fields=[0,2], invert=True)
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['b'], ['e'], ['h']], output)

    def test_single_col_plucking_with_skip(self):
        p = Processor(fields=[0], skip=1)
        output = [row for row in p.process(SAMPLE_CSV)]
        self.assertEqual([['d'], ['g']], output)

    def test_pluck_with_pipes(self):
        p = Processor(fields=[0], delimiter='|')
        output = [row for row in p.process(SAMPLE_PSV)]
        self.assertEqual([['a'], ['d'], ['g']], output)

    def test_quoted_pluck(self):
        p = Processor(fields=[0, 10, 11], skip=1)
        output = [row for row in p.process(SAMPLE_QUOTED_CSV)]
        expected = [['0200', '-35.277272', '149.117136'], ['0221', '-35.201372', '149.095065']]
        self.assertEqual(expected, output)
