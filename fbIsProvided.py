from .zNotProvided import zNotProvided;

def fbIsProvided(xzValue):
  # We don't want the user to directly compare a value that may be `zNotProvided`
  # to any other value, so we won't do it ourselves either. But every value in
  # Python has a unique id, so we can compare ids.
  return id(xzValue) != id(zNotProvided);
