import itertools
def print_permutation(string):
    permutations=itertools.permutations(string)
    for perm in permutations:
        print(''.join(perm))