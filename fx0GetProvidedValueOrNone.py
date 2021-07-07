from .zNotProvided import zNotProvided;

def fx0GetProvidedValueOrNone(xzValue):
  return xzValue if xzValue is not zNotProvided else None;
