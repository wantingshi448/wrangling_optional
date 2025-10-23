# src/household.py
from __future__ import annotations
import pandas as pd
import numpy as np

def household_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate individual-level rows into a household-level table.

    Input columns expected:
      - household_id (int)
      - age (int)
      - income (float, may contain NaN)
      - female (bool)

    Output columns:
      household_id, size_hh, mean_age, min_age, max_age,
      nr_children, nr_female, mean_income, total_income, main_earner_female
    """

    # basic aggregations
    g = df.groupby("household_id", dropna=False)

    size_hh     = g.size().rename("size_hh")
    mean_age    = g["age"].mean().rename("mean_age")
    min_age     = g["age"].min().rename("min_age")
    max_age     = g["age"].max().rename("max_age")
    nr_children = g["age"].apply(lambda s: (s < 18).sum()).rename("nr_children")
    nr_female   = g["female"].sum().rename("nr_female")  # True as 1, False as 0
    mean_income = g["income"].mean().rename("mean_income")
    total_income= g["income"].sum().rename("total_income")

    # who is the main earner (ignore NaN)
    # if all NaN in a household, mark as NaN -> then fill False
    def _main_earner_is_female(group: pd.DataFrame) -> bool:
        inc = group["income"]
        if inc.notna().any():
            idx = inc.idxmax()  # index of max income
            return bool(group.loc[idx, "female"])
        else:
            return np.nan

    main_earner_female = g.apply(_main_earner_is_female).rename("main_earner_female")
    main_earner_female = main_earner_female.fillna(False)

    out = pd.concat(
        [size_hh, mean_age, min_age, max_age,
         nr_children, nr_female, mean_income, total_income, main_earner_female],
        axis=1
    ).reset_index()

    return out
