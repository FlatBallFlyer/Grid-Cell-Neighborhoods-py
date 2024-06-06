# Grid-Cell-Neighborhoods

This is a python3+pytest Koan that requires you to solve the Grid-Cell Neighborhoods problem. Update the methods in community.py to make the pytest tests in test_community.py pass.

## Prerequisits

- [Python](https://docs.python-guide.org/starting/installation/)
- [Pipenv](https://pipenv.pypa.io/en/latest/installation.html)

## Install Dependencies

``` shell
pipenv run install
```

## Run Tests

``` shell
pipenv run unittest
```

## Solution

This solution works by

- Creating a community matrix of all 0s the same size as the input matrix
- Finding all the anchor neighbors
- Iterating, for each neighbor, over a matrix of (2 x distance) * (2 x distance)
- Marking each cell in the smaller matrix that satisfies the member condition
- Adding the coordinates of members to a set
- Returning the length of the member set

## Instructions

The community constructor is provided with a matrix and a distance. The matrix is a 2-dimensional array of numbers. Numbers > zero indicate neighbors that will anchor communities.

All points in the matrix that are within the specified distance of a neighbor should be counted in the community. You calculate distance​ between two points as the sum of row delta and col delta. I.E. from (2,1) to (0,4) would be the sum of the differences in the two dimensions: |2-0| + |1-4| = 2 + 3 = 5

The array dimensions do not wrap. That is, the first column should not be considered adjacent to the last column, and the top row should not be considered adjacent to the bottom row.

## Hints

The test data in [test_community.py](./test_community.py) uses -1 to show what the expected community should look like. These values are ingored by your code, but reviewing them can help you to visualize the distance calculations.

## Solved

There are many different ways to solve this problem, try to work it out yourself before looking at any other code. That being said there are several branches with hints and different solutions. If you change the branch to look at a solution, check out the README

If you have a novel approach that is not represented in those branches, please create and push a branch on the repo with an appropriate name!
