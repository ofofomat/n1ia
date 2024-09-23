class Genre:
  """
  A class used to represent a Genre.
  Attributes
  ----------
  name : str
    the name of the genre
  Methods
  -------
  __str__()
    Returns the string representation of the genre.
  """
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name