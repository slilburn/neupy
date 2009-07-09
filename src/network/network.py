class Neuron:
    test_string = "Hello"
    def __init__(self):
        pass
    def __unicode__(self):
        return test_string

class Network:
    network = []
    def __init__(self, template = [3,5,3]):
        self.network = []
        layers = len(template)
        current_layer = []
        for i in range(layers):
            current_layer = []
            neurons_in_layer = template[i]
            for j in range(neurons_in_layer):
                a = "Hello" # test
                current_layer.append(a)
            self.network.append(current_layer)
