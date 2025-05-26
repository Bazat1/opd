import unittest
from app import app, RATES


class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_usd_to_rub_conversion(self):
        # Тест конвертации USD в RUB
        self.assertAlmostEqual(100 * RATES['USD']['RUB'], 7550.0, places=2)

    def test_eur_to_usd_conversion(self):
        #Тест конвертации EUR в USD
        self.assertAlmostEqual(50 * RATES['EUR']['USD'], 54.5, places=2)

    def test_invalid_currency(self):
        #Тест обработки несуществующей валюты
        with self.assertRaises(KeyError):
            invalid_rate = RATES['BTC']['USD']

if __name__ == '__main__':
    unittest.main()
