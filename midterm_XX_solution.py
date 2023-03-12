import math
PI = math.pi
SHAPE_KRUH = 'kruh'
SHAPE_OBDELNIK = 'obdelnik'
SHAPE_PRAVOUHLY_TROJUHELNIK = 'pravouhly trojuhelnik'



def get_shapes_and_areas(shapes_parameters):

    names_list = []
    areas_list = []
    for shape_params in shapes_parameters:
        if len(shape_params) == 1:
            names_list.append(SHAPE_KRUH)
            areas_list.append(PI * shape_params[0] ** 2)
        elif len(shape_params) == 2:
            names_list.append(SHAPE_OBDELNIK)
            areas_list.append(shape_params[0] * shape_params[1])
        elif len(shape_params) == 3:
            names_list.append(SHAPE_PRAVOUHLY_TROJUHELNIK)
            areas_list.append(shape_params[0] * shape_params[1] / 2)

    return names_list, areas_list


def check_if_can_get_through_hole(shapes_parameters, names_list, hole_diameter):
    can_get_through_hole_list = []
    for shape_params, shape_name in zip(shapes_parameters, names_list):
        if shape_name == SHAPE_KRUH:
            can_get_through_hole_list.append(shape_params[0] * 2 <= hole_diameter)
        elif shape_name == SHAPE_OBDELNIK:
            can_get_through_hole_list.append((shape_params[0] ** 2 + shape_params[1] ** 2) ** 0.5 <= hole_diameter)
        elif shape_name == SHAPE_PRAVOUHLY_TROJUHELNIK:
            can_get_through_hole_list.append(shape_params[2] <= hole_diameter)

    return can_get_through_hole_list


def count_area_weighted_letters(names_list, areas_list, can_get_through_hole_list, letter):
    total_value = 0
    for shape_name, shape_area, can_get_through_hole in zip(names_list, areas_list, can_get_through_hole_list):
        if can_get_through_hole:
            for char in shape_name:
                if char == letter:
                    total_value = total_value + shape_area

    return total_value

def main(shapes_parameters, hole_diameter, letter, return_shape_names=False):

    names_list, areas_list = get_shapes_and_areas(shapes_parameters)
    can_get_through_hole_list = check_if_can_get_through_hole(shapes_parameters, names_list, hole_diameter)
    total_value = count_area_weighted_letters(names_list, areas_list, can_get_through_hole_list, letter)

    if return_shape_names:
        return total_value, names_list
    else:
        return total_value



if __name__ == '__main__':
    shapes_parameters = [(6,), (3, 5), (5, 3), (3,), (3, 1), (3, 4, 5), (5, 12, 13)]
    hole_diameter = 5
    letter = 'j'

    print(main(shapes_parameters, hole_diameter, letter))
    print(main(shapes_parameters, hole_diameter, letter, True))

