import pytest
from midterm_XX import get_shapes_and_areas

@pytest.mark.parametrize(
    ("shapes_parameters", "shapes", "areas"),
    [([(6,), (3, 5), (5, 3), (3,), (3, 1), (3, 4, 5), (5, 12, 13)],
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik'],
      [113.09733552923255, 15, 15, 28.274333882308138, 3, 6.0, 30.0],),
     ([(1,), (4, 5), (3, 2), (2,), (8, 4), (2.8, 4.5, 5.3), (6.5, 7.2, 9.7), (3,), (4,), (7,)],
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'kruh', 'kruh', 'kruh'],
      [3.141592653589793, 20, 6, 12.566370614359172, 32, 6.3, 23.400000000000002, 28.274333882308138, 50.26548245743669, 153.93804002589985],),
     ([(5,), (53, 2), (5, 2), (8,), (1, 2), (3.6, 7.7, 8.5), (3.9, 8.0, 8.9), (7, 2)],
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'obdelnik'],
      [78.53981633974483, 106, 10, 201.06192982974676, 2, 13.860000000000001, 15.6, 14],),
     ]
)

def test_midterm_E_1(shapes_parameters, shapes, areas):
    shapes_out, areas_out = get_shapes_and_areas(shapes_parameters)

    assert shapes == shapes_out
    areas_round = [round(x) for x in areas]
    areas_out_round = [round(x) for x in areas_out]

    assert areas_round == areas_out_round
