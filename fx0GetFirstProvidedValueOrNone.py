from .zNotProvided import zNotProvided;

def fx0GetFirstProvidedValueOrNone(*txzValues):
  for xzValue in txzValues:
    if xzValue is not zNotProvided:
      return xzValue;
  return None;
