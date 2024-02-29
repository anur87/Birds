from django.test import TestCase

class MyTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: вызывается один раз')

    def setUp(self):
        print('setUp: вызывается перед каждым тестом')

    def tearDown(self):
        print('tearDown: вызывается после каждого теста')

    def test1(self):
        print('Тест 1')
        self.assertFalse(False)

    def test2(self):
        print('Тест 2')
        self.assertTrue(True)

    def test3(self):
        print('Тест 3')
        self.assertEqual(18, 9 + 9)
