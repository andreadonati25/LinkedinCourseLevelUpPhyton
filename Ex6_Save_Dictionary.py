import pickle

def save_dict(dictionary, path):
    with open(path, "wb") as file:
        pickle.dump(dictionary, file)

def load_dict(path):
    with open(path, "rb") as file:
        dictionary = pickle.load(file)

    return dictionary

test_dict = {1:'a', 2:'b', 3:'c'}
save_dict(test_dict, "Ex6_dict.pickle")
print(load_dict("Ex6_dict.pickle"))