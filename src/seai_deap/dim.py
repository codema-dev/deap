import numpy as np


def calculate_building_volume(
    ground_floor_area: np.array,
    first_floor_area: np.array,
    second_floor_area: np.array,
    third_floor_area: np.array,
    ground_floor_height: np.array,
    first_floor_height: np.array,
    second_floor_height: np.array,
    third_floor_height: np.array,
) -> np.array:
    """Calculate building volume (DEAP 4.2.2 Dim!F10)

    Args:
        ground_floor_area (np.array): [description]
        first_floor_area (np.array): [description]
        second_floor_area (np.array): [description]
        third_floor_area (np.array): [description]
        ground_floor_height (np.array): [description]
        first_floor_height (np.array): [description]
        second_floor_height (np.array): [description]
        third_floor_height (np.array): [description]

    Returns:
        np.array: [description]
    """
    ground_floor_volume = ground_floor_area * ground_floor_height
    first_floor_volume = first_floor_area * first_floor_height
    second_floor_volume = second_floor_area * second_floor_height
    third_floor_volume = third_floor_area * third_floor_height

    return (
        ground_floor_volume
        + first_floor_volume
        + second_floor_volume
        + third_floor_volume
    )


def calculate_total_floor_area(
    ground_floor_area: np.array,
    first_floor_area: np.array,
    second_floor_area: np.array,
    third_floor_area: np.array,
) -> np.array:
    """Calculate total floor area (DEAP 4.2.2 Dim!D9)

    Args:
        ground_floor_area (np.array): m^2
        first_floor_area (np.array): m^2
        second_floor_area (np.array): m^2
        third_floor_area (np.array): m^2

    Returns:
        np.array: m^2
    """
    return ground_floor_area + first_floor_area + second_floor_area + third_floor_area
