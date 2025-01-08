import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/calculate', data=dict(num1=2, num2=3, operation='add'))
        self.assertIn(b'Result: 5.0', response.data)

    # Añade más tests para las otras operaciones

if __name__ == '__main__':
    unittest.main()
