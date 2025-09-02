# TODO: 사용자 모듈 import
from jiaco_funcs import even_num, average, find_max, find_min

# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.

def test_even_num():
    assert "even" == even_num(4)
    assert "even" == even_num(14)
    assert "odd" == even_num(3)
    assert "odd" == even_num(7)


def test_average():
    assert 3 == average([1, 2, 3, 4, 5])
    assert 5 == average([1,3,5,7,9])
        

def test_find_max():
    assert 4 == (find_max([1, 2, 3, 4]))
    assert-2 == (find_max([-5, -2, -10]))

def test_find_min():
    assert 1 == (find_min([1, 2, 3, 4]))
    assert -10 == (find_min([-5, -2, -10]))