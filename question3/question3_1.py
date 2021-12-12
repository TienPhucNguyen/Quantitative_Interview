import copy


def layer(n):
    if n < 1:
        return []
    elif n == 1:
        return [1]
    else:
        current_layer = [1]
        for i in range(n-1):
            previous_layer = copy.deepcopy(current_layer)
            current_layer.append(1)
            for j in range(1, len(current_layer) -1):
                current_layer[j] = previous_layer[j-1] + previous_layer[j]
        return current_layer

print(layer(5))