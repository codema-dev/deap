from typing import Optional

import numpy as np


def calculate_thermal_bridging(
    wall_area: np.array,
    roof_area: np.array,
    floor_area: np.array,
    window_area: np.array,
    door_area: np.array,
    thermal_bridging_factor: Optional[float] = 0.05,
) -> np.array:
    """Calculate thermal bridging (DEAP 4.2.2 Fab!G22).

    Args:
        wall_area (np.array): m^2
        roof_area (np.array): m^2
        floor_area (np.array): m^2
        window_area (np.array): m^2
        door_area (np.array): m^2
        thermal_bridging_factor (float, optional): Thermal Bridging Factor. Defaults to 0.05

    Returns:
        np.array: W/K
    """
    total_area_of_plane_elements = (
        wall_area + roof_area + floor_area + window_area + door_area
    )

    return total_area_of_plane_elements * thermal_bridging_factor


def calculate_heat_loss_via_plane_elements(
    wall_area: np.array,
    roof_area: np.array,
    floor_area: np.array,
    window_area: np.array,
    door_area: np.array,
    wall_uvalue: np.array,
    roof_uvalue: np.array,
    floor_uvalue: np.array,
    window_uvalue: np.array,
    door_uvalue: np.array,
) -> np.array:
    """Calculate heat loss via plane elements (DEAP 4.2.2. Fab!F21).

    Args:
        wall_area (np.array): m^2
        roof_area (np.array):  m^2
        floor_area (np.array):  m^2
        window_area (np.array): m^2
        door_area (np.array):  m^2
        wall_uvalue (np.array): W/m^2.K
        roof_uvalue (np.array): W/m^2.K
        floor_uvalue (np.array): W/m^2.K
        window_uvalue (np.array): W/m^2.K
        door_uvalue (np.array): W/m^2.K

    Returns:
        np.array: W/K
    """
    wall_au = wall_area * wall_uvalue
    roof_au = roof_area * roof_uvalue
    floor_au = floor_area * floor_uvalue
    window_au = window_area * window_uvalue
    door_au = door_area * door_uvalue

    return wall_au + roof_au + floor_au + window_au + door_au


def calculate_fabric_heat_loss(
    heat_loss_via_plane_elements: np.array, thermal_bridging: np.array,
) -> np.array:
    """Calculate fabric heat loss (DEAP 4.2.2 Fab!F24)

    Args:
        heat_loss_via_plane_elements (np.array): W/K
        thermal_bridging (np.array): W/K

    Returns:
        np.array: W/K
    """
    return heat_loss_via_plane_elements + thermal_bridging


def calculate_heat_loss_coefficient(
    fabric_heat_loss: np.array, ventilation_heat_loss: np.array,
) -> np.array:
    """Calculate heat loss coefficient (DEAP 4.2.2 Fab!F27)

    Args:
        fabric_heat_loss (np.array): [description]
        ventilation_heat_loss (np.array): [description]

    Returns:
        np.array: [description]
    """

    return fabric_heat_loss + ventilation_heat_loss


def calculate_heat_loss_parameter(
    heat_loss_coefficient: np.array, total_floor_area: np.array,
) -> np.array:
    """Calculate heat loss parameter (DEAP 4.2.2 Fab!F28)

    Args:
        heat_loss_coefficient (np.array): W/K
        total_floor_area (np.array): m^2

    Returns:
        np.array: W.m^2/K
    """

    return heat_loss_coefficient / total_floor_area
