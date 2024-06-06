class Community:
  """
  A class to represent members of a communinty anchored by neighbours

  Attributes
  ----------
  members : set of (int,int)
    Coordinates of unique community members.
  community : list of [int]
    A matrix of integers the same size as the input matrix, with
    a value of 0 or 1 to indicate members
  neighbours : list of (int,int)
    A list of the neighbour coordinates that anchor the community

  Methods
  -------
  __init__
    constructor
  get_count()
    Returns the number of members in the community
  find_neighbours()
    Returns a list of row,col coordinates of matrix values > 0
  build_community()
    Mark coordinates within distance of the neighbours as members.
  """
  def __init__(self, matrix, distance):
    """
    Constructor - Initialize the community and members set, find neighbours, and mark the members.

    Parameters
    ----------
    matrix : list of [int]
      2-D array of integers.
      Numbers > 0 are neighbours that anchor the community.
    distance : int
      the distance from neighbours that should be countd in the community.
    """
    self.members = set()
    self.community = [[0] * len(row) for row in matrix]
    self.neighbours = self.find_neighbours(matrix)
    self.build_community(distance)


  def find_neighbours(self, matrix):
    """
    Find neighbours (value > 0) and return coordinates.
    """
    neighbours = []
    for row in range(len(matrix)):
      for col in range(len(matrix[row])):
        if matrix[row][col] > 0:
          neighbours.append((row,col))
    return neighbours

    
  def build_community(self, distance):
    """
    Mark coordinates within distance as 1.
    """
    for row, col in self.neighbours:
      for i in self.get_range(row, distance, self.community):
        for j in self.get_range(col, distance, self.community[i]):
          if 0 <= abs(i - row) + abs(j - col) <= distance:
            self.members.add((i,j))
            self.community[i][j] = 1


  def get_range(self, coord, distance, boundary):
    """
    Get a bounded range for iteration
    """
    return filter(lambda x: 0 <= x < len(boundary), range(coord - distance, coord + distance + 1))


  def build_community1(self, matrix, distance):
    """
    Mark coordinates within distance as 1.
    """
    for neighbour in self.neighbours:
      for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if 0 <= abs(neighbour[0] - i) + abs(neighbour[1] - j) <= distance:
              self.members.add((i,j))
              self.community[i][j] = 1


  def get_count(self):
    """
    Get the number of members in the community.
    """
    return len(self.members)

