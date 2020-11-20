import numpy as np
from numpy.testing import assert_array_equal

from seai_deap import dim


def test_calculate_building_volume() -> None:

    expected_output = np.array(4)

    output = dim.calculate_building_volume(
        ground_floor_area=np.array(1),
        first_floor_area=np.array(1),
        second_floor_area=np.array(1),
        third_floor_area=np.array(1),
        ground_floor_height=np.array(1),
        first_floor_height=np.array(1),
        second_floor_height=np.array(1),
        third_floor_height=np.array(1),
    )

    assert_array_equal(output, expected_output)


def test_calculate_total_floor_area() -> None:

    expected_output = np.array((4))

    output = dim.calculate_total_floor_area(
        ground_floor_area=np.array(1),
        first_floor_area=np.array(1),
        second_floor_area=np.array(1),
        third_floor_area=np.array(1),
    )

    assert_array_equal(output, expected_output)
