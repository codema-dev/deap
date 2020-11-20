import numpy as np
from numpy.testing import assert_array_equal

from seai_deap import vent


def test_calculate_ventilation_heat_loss() -> None:

    expected_output = np.array(0.165)

    output = vent.calculate_ventilation_heat_loss(
        volume=np.array(1),
        ventilation_heat_loss_constant=0.33,
        effective_air_rate_change=0.5,
    )

    assert_array_equal(output, expected_output)
