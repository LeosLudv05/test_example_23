import pytest
from midterm_XX import main

@pytest.mark.parametrize(
    ("shapes_parameters", "hole_diameter", "letter", "return_shapes", "count", "shapes"),
    [([(6,), (3, 5), (5, 3), (3,), (3, 1), (3, 4, 5), (5, 12, 13)],
      5,
      'j',
      True,
      6.0,
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik'],),
     ([(5,), (53, 2), (5, 2), (8,), (1, 2), (3.6, 7.7, 8.5), (3.9, 8.0, 8.9), (7, 2)],
      6,
      'n',
      False,
      12.0,
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'obdelnik'],),
     ]
)

def test_midterm_E_4(shapes_parameters, hole_diameter, letter, return_shapes, count, shapes):

    if return_shapes:
        count_out, shapes_out = main(shapes_parameters, hole_diameter, letter, return_shapes)
        count_round = round(count)
        count_out_round = round(count_out)
        assert count_round == count_out_round
        assert shapes_out == shapes

    else:
        count_out = main(shapes_parameters, hole_diameter, letter)
        count_round = round(count)
        count_out_round = round(count_out)
        assert count_round == count_out_round

