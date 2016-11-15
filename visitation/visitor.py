

class GraphBuilder(object):

    def process_child(self, item, graph):
        graph['test'].append('hey')
        return graph

    def do_visit(self, item, graph):
        for child in item.items():
            graph = self.process_child(child, graph)
        return graph

    def build(self, root):
        graph = { 'test' : []}
        return self.do_visit(root, graph)
