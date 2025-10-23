# wrangling\_optional

Optional data wrangling exercise



\## Objective



Recreate the simulated \*\*individual-level\*\* data from Lecture 2 and transform it into a \*\*household-level\*\* table via feature engineering.





\## Project layout



wrangling\_optional/

├─ src/

│ ├─ simulate.py # create\_simulated\_data(): build individual-level table

│ ├─ household.py # household\_features(): aggregate to household level

│ └─ orchestrator.py # generate\_household\_level\_data(): end-to-end entry point



\## How to run locally



```bash

\# 1) Activate env and cd to repo root

conda activate fun\_ds

cd ~/projects/wrangling\_optional  # Windows: cd %USERPROFILE%\\projects\\wrangling\_optional



\# 2) Generate the household-level table

python -c "from src.orchestrator import generate\_household\_level\_data; print(generate\_household\_level\_data(4,42).to\_string(index=False))"





