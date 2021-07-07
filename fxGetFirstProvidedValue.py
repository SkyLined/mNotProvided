from .zNotProvided import zNotProvided;
def fxGetFirstProvidedValue(*txzValues):
  for xzValue in txzValues:
    if xzValue is not zNotProvided:
      return xzValue;
  raise AssertionError("No value has been provided");
