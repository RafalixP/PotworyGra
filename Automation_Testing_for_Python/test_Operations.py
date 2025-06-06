import Operations

import pytest
@pytest.mark.parametrize('x, y, result',
                         [
                             (7,3,10),
                             ('Hello', 'World', 'HelloWorld'),
                             (10.5,25.5,37)
                         ]
)

def test_add(x,y,result):
    assert Operations.add(x,y) == result
    
# def test_add():
#     assert Operations.add(7,3) == 10
#     assert Operations.add(7,) == 9
#     assert Operations.add(5) == 7

# def test_product():
#     assert Operations.product(5,3) == 15