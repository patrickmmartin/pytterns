import unittest

import visitor

import fund
import organisation


Fund = fund.Fund
Organisation = organisation.Organisation
GraphBuilder = visitor.GraphBuilder




class BuilderTestCase(unittest.TestCase):
    def test_builder(self):
        v = GraphBuilder()
        graph = v.build(Fund())
        print(graph)


if __name__ == '__main__':
    unittest.main()
