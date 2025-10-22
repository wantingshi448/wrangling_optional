# src/simulate.py

from __future__ import annotations

import numpy as np
import pandas as pd


def create_simulated_data(
    n_households: int = 50,
    min_size: int = 1,
    max_size: int = 5,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Generate an *individual-level* simulated dataset.

    Each row represents a person and contains:
      - household_id: household identifier (int)
      - person: index of the person inside the household (1..size)
      - age: person's age (int)
      - income: person's income (int or None to simulate missingness)
      - female: whether the person is female (bool)

    The output will be used later to aggregate/group to a *household-level* table.

    Parameters
    ----------
    n_households : int
        Number of households to generate.
    min_size : int
        Minimum household size (inclusive).
    max_size : int
        Maximum household size (inclusive).
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        Columns: ["household_id", "person", "age", "income", "female"].
    """
    rng = np.random.default_rng(seed)

    # Draw a random household size for each household
    sizes = rng.integers(min_size, max_size + 1, size=n_households)

    rows: list[dict] = []

    # Start household_id at 100 just to make it obvious in demos
    next_household_id = 100

    for hh_idx, size in enumerate(sizes):
        hh_id = next_household_id + hh_idx

        # Create each person in the household
        for p in range(1, size + 1):
            # Age distributed roughly from 15 to 79
            age = int(rng.integers(15, 80))

            # Income loosely correlated with age; allow ~10% missing values
            base_income = max(0, int(rng.normal(loc=age * 1200, scale=8000)))
            income = None if rng.random() < 0.10 else base_income  # 10% missing

            # Female as a simple Bernoulli(0.5)
            female = bool(rng.integers(0, 2))

            rows.append(
                {
                    "household_id": hh_id,
                    "person": p,
                    "age": age,
                    "income": income,
                    "female": female,
                }
            )

    df = pd.DataFrame(rows, columns=["household_id", "person", "age", "income", "female"])
    return df
