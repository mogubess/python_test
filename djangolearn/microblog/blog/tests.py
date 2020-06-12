from django.test import TestCase,Client

class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')
        
        # status code => 200 ok
        # status code => Not found
        # 302 Redirect
        self.assertEqual( 200, res.status_code)

    def test_fail_access(self):
        # self.assert_(False) いきなり失敗させる
        res = self.c.get('/unknown')
        self.assertEqual( 404, res.status_code )