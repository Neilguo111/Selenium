from count import count,is_prime
import unittest


# class Test(unittest.TestCase):
#
#     def setUp(self):
#         print('test startup')
#
#     def test_case(self):
#         self.assertTrue(is_prime(7),msg = 'Is not peime')
#
#     def tearDown(self):
#         print('test end')
#
# if '__name__' == '__main__':
#     unittest.main()

class TestAdd(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_add(self):
        j = count(2,3)
        self.assertEqual(j.add(),7,msg='is wrong')

    def test_add2(self):
        j = count(41,76)
        self.assertEqual(j.add(),117)

    def tearDown(self):
        print('test end')

class TestSub(unittest.TestCase):

    def setUp(self):
        print('test start')

    def test_sub(self):
        j = count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j = count(71,46)
        self.assertEqual(j.sub(),25)

    def tearDown(self):
        print('test end')

if '__name__'=='__main__':
    #构造测试集
    suit = unittest.TestSuite()
    suit.addTest(TestAdd('test_add'))
    suit.addTest(TestAdd('test_add2'))
    suit.addTest(TestAdd('test_sub'))
    suit.addTest(TestAdd('test_sub2'))
    #运行测试集合
    rrunner = unittest.TextTestRuner()
    rrunner.run(suit)
