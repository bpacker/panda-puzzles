panda-puzzles
=============

Solvers for Panda Magazine puzzles

## Setup
1. clone the repo
2. cd balance-point-estimation-prototype
3. mkvirtualenv balancepoint
4. pip install -r requirements.txt

### Backstabbing wives

#### Run the backstabbing wives constraint solver
`> python backstab.py`

#### Configuring
At the top of `backstab.py`, you can edit `MAX_STABBINGS` to be lower than 30 to allow for a faster and less 
memory-intensive run that doesn't fully solve the problem because it doesn't consider solutions with numbers above 
that threshold.