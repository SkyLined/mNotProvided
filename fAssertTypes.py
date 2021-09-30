from .fAssertType import fAssertType;

def fAssertTypes(dtxValueAndValueTypes_by_sName):
  # This function checks the type of a variable on behalf of its caller and throws a descriptive exception if the
  # variable is of an incorrect type. Ideally, we would do this inline in the caller function and throw the exception
  # from there, but Python does not allow us to easily do that. So we hide this function in the stack in mDebugOutput:
  # This causes the exception throw from this function if the variable type is invalid to appear as if it was thrown
  __mDebugOutput_HideInCallStack = True; # from the function calling this function.
  # Argument is {"name": (value, type, ....), ...}
  for (sName, txValueAndValueTypes) in dtxValueAndValueTypes_by_sName.items():
    # Call fAssertType for each entry in the dict.
    fAssertType(sName, *txValueAndValueTypes);
