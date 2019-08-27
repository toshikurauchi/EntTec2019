import types
from tree import Tree
import search


#################################### SETUP ####################################


class CountCallFunc:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def reset_calls(self):
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

    def __str__(self):
        return str(self.func)

    def __repr__(self):
        return repr(self.func)


def count_calls(func):
    return CountCallFunc(func)


# Decorate functions
search.pre_order_recursive = count_calls(search.pre_order_recursive)
search.pre_order_iterative = count_calls(search.pre_order_iterative)
search.in_order_recursive = count_calls(search.in_order_recursive)
search.in_order_iterative = count_calls(search.in_order_iterative)
search.post_order_recursive = count_calls(search.post_order_recursive)
search.post_order_iterative = count_calls(search.post_order_iterative)
search.breadth_first = count_calls(search.breadth_first)

def assert_recursive(func, recursive):
    if recursive:
        assert func.calls > 1, 'Function should be recursive.'
    else:
        assert func.calls == 1, 'Function should be iterative. Called {0} times.'.format(func.calls)


def setup():
    search.pre_order_recursive.reset_calls()
    search.pre_order_iterative.reset_calls()
    search.in_order_recursive.reset_calls()
    search.in_order_iterative.reset_calls()
    search.post_order_recursive.reset_calls()
    search.post_order_iterative.reset_calls()
    search.breadth_first.reset_calls()


def build_perfect_tree():
    r'''
    Builds the following tree:

               __________0__________
              /                     \
         ____1____               ____2____
        /         \             /         \
      _3_         _4_         _5_         _6_
     /   \       /   \       /   \       /   \
    7     8     9    10    11    12    13    14
    '''
    return Tree(list(range(15)))


def build_unbalanced_tree():
    r'''
    Builds the following tree:

      ______________________0______________________
     /                                             \
    1__________                           __________2__________
               \                         /                     \
                3____                   4____                   5____
                     \                       \                       \
                     _6_                     _7_                     _8
                    /   \                   /   \                   /
                   9    10                11    12                13
    '''
    description = [
                                                                0,
                                    1,                                                       2,
                   None,                            3,                         4,                         5,
           None,           None,           None,          6,          None,          7,           None,          8,
        None, None,     None, None,     None, None,     9, 10,     None, None,     11, 12,     None, None,     13
    ]
    return Tree(description)


def apply_test(func, expected, with_perfect_tree, recursive):
    if with_perfect_tree:
        tree = build_perfect_tree()
    else:
        tree = build_unbalanced_tree()
    result = func(tree.root)
    assert_recursive(func, recursive)
    assert result == expected


#################################### TESTS ####################################

# PRE-ORDER

def test_pre_order_recursive_perfect_tree():
    expected = [0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 12, 6, 13, 14]
    apply_test(search.pre_order_recursive, expected, True, True)


def test_pre_order_recursive_unbalanced_tree():
    expected = [0, 1, 3, 6, 9, 10, 2, 4, 7, 11, 12, 5, 8, 13]
    apply_test(search.pre_order_recursive, expected, False, True)


def test_pre_order_iterative_perfect_tree():
    expected = [0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 12, 6, 13, 14]
    apply_test(search.pre_order_iterative, expected, True, False)


def test_pre_order_iterative_unbalanced_tree():
    expected = [0, 1, 3, 6, 9, 10, 2, 4, 7, 11, 12, 5, 8, 13]
    apply_test(search.pre_order_iterative, expected, False, False)


# IN-ORDER

def test_in_order_recursive_perfect_tree():
    expected = [7, 3, 8, 1, 9, 4, 10, 0, 11, 5, 12, 2, 13, 6, 14]
    apply_test(search.in_order_recursive, expected, True, True)


def test_in_order_recursive_unbalanced_tree():
    expected = [1, 3, 9, 6, 10, 0, 4, 11, 7, 12, 2, 5, 13, 8]
    apply_test(search.in_order_recursive, expected, False, True)


def test_in_order_iterative_perfect_tree():
    expected = [7, 3, 8, 1, 9, 4, 10, 0, 11, 5, 12, 2, 13, 6, 14]
    apply_test(search.in_order_iterative, expected, True, False)


def test_in_order_iterative_unbalanced_tree():
    expected = [1, 3, 9, 6, 10, 0, 4, 11, 7, 12, 2, 5, 13, 8]
    apply_test(search.in_order_iterative, expected, False, False)


# POST-ORDER

def test_post_order_recursive_perfect_tree():
    expected = [7, 8, 3, 9, 10, 4, 1, 11, 12, 5, 13, 14, 6, 2, 0]
    apply_test(search.post_order_recursive, expected, True, True)


def test_post_order_recursive_unbalanced_tree():
    expected = [9, 10, 6, 3, 1, 11, 12, 7, 4, 13, 8, 5, 2, 0]
    apply_test(search.post_order_recursive, expected, False, True)


def test_post_order_iterative_perfect_tree():
    expected = [7, 8, 3, 9, 10, 4, 1, 11, 12, 5, 13, 14, 6, 2, 0]
    apply_test(search.post_order_iterative, expected, True, False)


def test_post_order_iterative_unbalanced_tree():
    expected = [9, 10, 6, 3, 1, 11, 12, 7, 4, 13, 8, 5, 2, 0]
    apply_test(search.post_order_iterative, expected, False, False)


# BREADTH FIRST

def test_breadth_first_perfect_tree():
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    apply_test(search.breadth_first, expected, True, False)


def test_breadth_first_unbalanced_tree():
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    apply_test(search.breadth_first, expected, False, False)


if __name__ == "__main__":
    import sys
    import pytest

    pytest.main([sys.argv[0]])
