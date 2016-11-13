import unittest

import registry
import fund

Registry = registry.Registry
Fund = fund.Fund

class RegistryTestCase(unittest.TestCase):

    def test_type(self):
        f = Fund
        o =  f()
        self.assertIsInstance(o, Fund)

    def test_registry(self):
        r = Registry()
        r.clear()
        self.assertIsNone(r.get('Fund'))
        r.add('FundKey', Fund, ())
        f = r.get('FundKey')
        self.assertIsInstance(f, Fund)

if __name__ == '__main__':
    unittest.main()
