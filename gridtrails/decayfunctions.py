import math

def make_linear_decay_function(ratio):
    def linear_decay_function(heat):
        return math.floor(heat / ratio)
    return linear_decay_function