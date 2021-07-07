from .zNotProvided import zNotProvided;

def fxzGetFirstProvidedValueIfAny(*txzValues):
  for xzValue in txzValues:
    if xzValue is not zNotProvided:
      return xzValue;
  return zNotProvided;

