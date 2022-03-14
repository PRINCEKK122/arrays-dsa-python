import pytest

from custom_arrays import Array


@pytest.fixture
def items():
    arr: Array = Array()

    arr.insert(3)
    arr.insert(1)
    arr.insert(-5)

    return arr


def test_length_of_array(items):
    assert items.size() == 3


def test_remove_item_at_valid_index(items):
    assert items.remove_at(1) == 1
    assert items.size() == 2


def test_remove_item_at_invalid_index(items):
    with pytest.raises(IndexError):
        items.remove_at(3)


def test_reverse_items_in_array(items):
    assert items.reverse() == [-5, 1, 3]


def test_index_of_item_present_in_array(items):
    assert items.index_of(3) == 0


def test_index_of_item_not_present_in_array(items):
    assert items.index_of(10) == -1


def test_max_number_in_array(items):
    assert items.max() == 3


def test_insert_an_item_at_a_given_valid_index(items):
    items.insert_at(0, 0)

    assert items.index_of(0) == 0
    assert items.size() == 4


def test_insert_an_item_at_an_invalid_index(items):
    with pytest.raises(IndexError):
        items.insert_at(3, 0)


def test_common_elements_in_both_lists(items):
    assert items.intersect([-5, 3, -1]) == [3, -5]


