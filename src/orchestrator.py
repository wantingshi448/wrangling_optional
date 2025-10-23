# src/orchestrator.py
from __future__ import annotations
import pandas as pd

from src.simulate import create_simulated_data
from src.household import household_features

def generate_household_level_data(
    n_households: int = 50,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Orchestration entrypoint.

    1) Create simulated individual-level data
    2) Aggregate/group to household-level features

    Parameters
    ----------
    n_households : int
        Number of households to simulate.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    pd.DataFrame
        Household-level table with columns like:
        household_id, size_hh, mean_age, min_age, max_age,
        nr_children, nr_female, mean_income, total_income, main_earner_female
    """
    df_individual = create_simulated_data(n_households=n_households, seed=seed)
    df_household = household_features(df_individual)
    return df_household


if __name__ == "__main__":
    # Quick manual run:
    demo = generate_household_level_data(n_households=4, seed=42)
    print(demo.to_string(index=False))

