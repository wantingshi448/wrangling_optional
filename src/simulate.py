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
    生成“个人层级”的模拟数据，包含：
    - household_id: 家庭ID
    - person: 家庭内第几位成员（1..size）
    - age: 年龄
    - income: 收入（带少量缺失）
    - female: 是否女性（布尔）

    你可以 later 用这个表做聚合，得到“家庭层级”的宽表。
    """
    rng = np.random.default_rng(seed)

    # 随机每个家庭的人数
    sizes = rng.integers(min_size, max_size + 1, size=n_households)

    rows = []
    next_household_id = 100
    for hh_idx, size in enumerate(sizes):
        hh_id = next_household_id + hh_idx
        for p in range(1, size + 1):
            age = int(rng.integers(15, 80))  # 15~79
            # 收入与年龄弱相关，加入噪声；并制造 ~10% 的缺失
            base_income = max(0, int(rng.normal(loc=age * 1200, scale=8000)))
            income = None if rng.random() < 0.10 else base_income
            female = bool(rng.integers(0, 2))  # 0/1 -> False/True
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


# 方便在命令行快速预览
if __name__ == "__main__":
    df = create_simulated_data(n_households=8, seed=0)
    print(df.head(12))
