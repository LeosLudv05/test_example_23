import pytest
from midterm_XX import count_area_weighted_letters

@pytest.mark.parametrize(
    ("shapes", "areas", "can_get_through_hole", "letter", "count"),
    [(['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'obdelnik'],
      [78.53981633974483, 106, 10, 201.06192982974676, 2, 13.860000000000001, 15.6, 14],
      [False, False, False, False, True, True, True, False],
      'h',
      58.92,),
     (['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'obdelnik'],
      [78.53981633974483, 106, 10, 201.06192982974676, 2, 13.860000000000001, 15.6, 14],
      [False, False, True, False, True, True, True, False],
      'o',
      70.92,),
     (['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'kruh', 'kruh', 'kruh'],
      [3.141592653589793, 20, 6, 12.566370614359172, 32, 6.3, 23.400000000000002, 28.274333882308138, 50.26548245743669, 153.93804002589985],
      [True, False, True, True, False, True, False, True, False, False],
      't',
      6.3,),
     ]
)


def test_assignment(shapes, areas, can_get_through_hole, letter, count):

    count_out = count_area_weighted_letters(shapes, areas, can_get_through_hole, letter)
    count_round = round(count)
    count_out_round = round(count_out)

    assert count_round == count_out_round
