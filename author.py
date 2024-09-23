class Author:
  """
  A module that defines the Author class.
  Classes:
    Author: A class representing an author with a name attribute.
  Methods:
    __init__(self, name): Initializes the Author instance with a name.
    __str__(self): Returns the string representation of the Author instance.
  """
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name