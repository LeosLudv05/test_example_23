import pytest
from midterm_XX import check_if_can_get_through_hole

@pytest.mark.parametrize(
    ("shapes_parameters", "shapes", "hole_diameter","can_get_through_hole"),
    [([(6,), (3, 5), (5, 3), (3,), (3, 1), (3, 4, 5), (5, 12, 13)],
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik'],
      5,
      [False, False, False, False, True, True, False]),
     ([(6,), (3, 5), (5, 3), (3,), (3, 1), (3, 4, 5), (5, 12, 13)],
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik'],
      3,
      [False, False, False, False, False, False, False]),
     ([(1,), (4, 5), (3, 2), (2,), (8, 4), (2.8, 4.5, 5.3), (6.5, 7.2, 9.7), (3,), (4,), (7,)],
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'kruh', 'kruh', 'kruh'],
      7,
      [True, True, True, True, False, True, False, True, False, False],),
     ([(1,), (4, 5), (3, 2), (2,), (8, 4), (2.8, 4.5, 5.3), (6.5, 7.2, 9.7), (3,), (4,), (7,)],
      ['kruh', 'obdelnik', 'obdelnik', 'kruh', 'obdelnik', 'pravouhly trojuhelnik', 'pravouhly trojuhelnik', 'kruh', 'kruh', 'kruh'],
      4,
      [True, False, True, True, False, False, False, False, False, False],)
     ]
)


def test_midterm_E_2(shapes_parameters, shapes, hole_diameter,can_get_through_hole):
    can_get_through_hole_out = check_if_can_get_through_hole(shapes_parameters, shapes, hole_diameter)
    assert can_get_through_hole == can_get_through_hole_out