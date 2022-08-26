from .zNotProvided import zNotProvided;

gbDebugOutput = False;

def fAssertType(sName, xValue, *txTypes):
  # This function checks the type of a variable on behalf of its caller and throws a descriptive exception if the
  # variable is of an incorrect type. Ideally, we would do this inline in the caller function and throw the exception
  # from there, but Python does not allow us to easily do that. So we hide this function in the stack in mDebugOutput:
  # This causes the exception throw from this function if the variable type is invalid to appear as if it was thrown
  mDebugOutput_HideInCallStack = True; # from the function calling this function.
  def fbIsOfType(xValue, *txTypes):
    for xType in txTypes:
      if xType is None:
        if xValue is None:
          return True;
        if gbDebugOutput: print("value %s is not None" % (repr(xValue),));
      elif id(xType) == id(zNotProvided):
        if id(xValue) == id(zNotProvided):
          return True;
        if gbDebugOutput: print("value %s is not zNotProvided" % (repr(xValue),));
      elif isinstance(xType, tuple):
        # Every element of the tuple must be of the correct type
        if isinstance(xValue, tuple):
          if len(xValue) > len(xType):
            if gbDebugOutput: print("tuple has %d superfluous elements" % (len(xValue) - len(xType),));
          elif len(xType) > len(xValue):
            if gbDebugOutput: print("tuple is missing %d elements" % (len(xType) - len(xValue),));
          else:
            for uIndex in range(len(xType)):
              xElement = xValue[uIndex];
              xElementType = xType[uIndex];
              if not fbIsOfType(xElement, xElementType):
                if gbDebugOutput: print("tuple element %d (%s) is not %s" % (
                  uIndex, 
                  repr(xElement),
                  fsCombineList(fasGetTypeDescriptions(xElementType)),
                ));
                break;
            else:
              return True;
      elif isinstance(xType, list):
        # Every element of the list must be any of the types provided in the list
        if isinstance(xValue, list):
          axElementTypes = xType;
          for xElement in xValue:
            if not fbIsOfType(xElement, *axElementTypes):
              if gbDebugOutput: print("list element %s is not %s" % (repr(xElement), fsCombineList(fasGetTypeDescriptions(*axElementTypes))));
              break;
          else:
            return True;
        if gbDebugOutput: print("value %s is not a list" % (repr(xValue),));
      elif isinstance(xType, dict):
        # Every key+value pair of the dict must be of the key+value types provided in the dict
        if isinstance(xValue, dict):
          dxKeyAndValueTypes = xType;
          for (xKey, xValue) in xValue.items():
            for (xKeyTypes, xValueTypes) in dxKeyAndValueTypes.items():
              if not fbIsOfType(xKey, xKeyTypes):
                break;
              if not fbIsOfType(xValue, xValueTypes):
                break;
            else:
              return True;
            if gbDebugOutput: print("dict element %s:%s is not %s" % (repr(xKey), repr(xValue), fsCombineList(fasGetTypeDescriptions(dxKeyAndValueTypes))));
        if gbDebugOutput: print("value %s is not a dict" % (repr(xValue),));
      else:
        try:
          if isinstance(xValue, xType):
            return True;
        except TypeError as oException:
          if oException.args[0] in (
            "isinstance() arg 2 must be a type or tuple of types",
            "isinstance() arg 2 must be a type, a tuple of types, or a union",
          ):
            raise AssertionError("fAssertType was called with %s as a possible type, but it is not a valid type" % repr(xType));
          raise;
        if gbDebugOutput: print("value %s is not %s" % (repr(xValue), fsCombineList(fasGetTypeDescriptions(xType))));
    return False;
  def fsCombineList(asValues):
    if len(asValues) == 1:
      return asValues[0];
    if len(asValues) == 2:
      return "%s or %s" % (asValues[0], asValues[1]);
    return "%s, or %s" % (", ".join(asValues[:-1]), asValues[-1]);
  def fasGetTypeDescriptions(*txTypes):
    asTypes = [];
    for xType in txTypes:
      if xType is None:
        asTypes.append("None");
      elif isinstance(xType, tuple):
        asTypes += fasGetTypeDescriptions(*xType);
      elif isinstance(xType, list):
        asTypes.append("[%s]" % fsCombineList(fasGetTypeDescriptions(*xType)));
      elif isinstance(xType, dict):
        asKeyValueTypes = [];
        for (xKeyTypes, xValueTypes) in xType.items():
          asKeyValueTypes.append("%s: %s" % (
            fsCombineList(fasGetTypeDescriptions(*xKeyTypes)),
            fsCombineList(fasGetTypeDescriptions(*xValueTypes)),
          ));
        asTypes.append("{%s}" % fsCombineList(asKeyValueTypes));
      elif id(xType) == id(zNotProvided):
        asTypes.append("zNotProvided");
      else:
        asTypes.append(repr(xType.__name__));
    return asTypes;
  assert fbIsOfType(xValue, *txTypes), \
      "%s must be %s, not %s (%s)" % (
        repr(sName), fsCombineList(fasGetTypeDescriptions(txTypes)),
        repr(type(xValue).__name__),
        repr(xValue)
      );
