import unittest
from main import reverse_str, reverse_str_in_order

class TestRever(unittest.TestCase):
    def test_reverse_str(self):
        self.assertEqual(reverse_str('aninmal'), 'lamnina')
        self.assertEqual(reverse_str('planet'), 'tenalp')
        self.assertEqual(reverse_str('planet'), 'tenalp')
        self.assertEqual(reverse_str('veneration'), 'noitarenev')
        self.assertEqual(reverse_str('acclaimed'), 'demialcca')
        self.assertEqual(reverse_str('mendacity'), 'yticadnem')
        self.assertEqual(reverse_str('incursion'), 'noisrucni')
        self.assertEqual(reverse_str('equable'), 'elbauqe')
        self.assertEqual(reverse_str('duress'), 'sserud')
        self.assertEqual(reverse_str('forgery'), 'yregrof')

    
    def test_reverse_str_in_order(self):
        self.assertCountEqual(reverse_str_in_order('to be or not to be'), 'ot eb ro ton ot eb')
        self.assertCountEqual(reverse_str_in_order('she is nice'), 'ehs si ecin')
        self.assertCountEqual(reverse_str_in_order('she is nice'), 'ehs si ecin')
        self.assertCountEqual(reverse_str_in_order('keep on going never give up'), 'peek no gniog reven evig pu')
        self.assertCountEqual(reverse_str_in_order('believe in yourself'), 'eveileb ni flesruoy')
        self.assertCountEqual(reverse_str_in_order('action speak louder than words'), 'noitca kaeps reduol naht sdrow')
        self.assertCountEqual(reverse_str_in_order('never say die'), 'revne yas eid')
        self.assertCountEqual(reverse_str_in_order('winners do what losers don not want to do'), 'srenniw od tahw sresol nod ton tnaw ot od')
        self.assertCountEqual(reverse_str_in_order('judge not from appearances'), 'egduj ton morf secnaraeppa')
        self.assertCountEqual(reverse_str_in_order('life is but a span'), 'efil si tub a naps')

if __name__ == "__main__":
    unittest.main()