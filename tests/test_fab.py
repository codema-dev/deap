import numpy as np
from numpy.testing import assert_array_equal

from seai_deap import fab


def test_calculate_thermal_bridging() -> None:

    expected_output = np.array(0.75)

    output = fab.calculate_thermal_bridging(
        wall_area=np.array(1),
        roof_area=np.array(1),
        floor_area=np.array(1),
        window_area=np.array(1),
        door_area=np.array(1),
        thermal_bridging_factor=np.array(0.15),
    )

    assert_array_equal(output, expected_output)

