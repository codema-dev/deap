import numpy as np


def calculate_ventilation_heat_loss(
    volume: np.array,
    ventilation_heat_loss_constant: float = 0.33,
    effective_air_rate_change: float = 0.5,
) -> np.array:
    """Calculate ventilation heat loss (DEAP 4.2.2 Vent!G34)

    Args:
        volume (np.array): m^3
        ventilation_heat_loss_constant (float, optional): [description]. Defaults to 0.33.
        effective_air_rate_change (float, optional): [description]. Defaults to 0.5.

    Returns:
        np.array: W/K
    """
    return ventilation_heat_loss_constant * effective_air_change_rate * volume
