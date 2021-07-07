# Offers a way to provide a value for a variable or argument that indicates
# there is no value provided. This is useful for optional function arguments
# that can have many different types of value, or which may not be provided.
# This module can be used to pass the concept of "not provided" as a value, and
# check if the caller did indeed provide "not provided" as a value.
# Example use:

# from mOptional import *;
# def fPrintVariableIfProvided(xzOptionalArgument = zNotProvided):
#   if fbIsProvided(xzOptionalArgument):
#     print repr(xzOptionalArgument);
#
# fPrintVariableIfProvided();     # does not print anything;
# fPrintVariableIfProvided(None); # prints "None";

from .zNotProvided import zNotProvided;
from .fAssertType import fAssertType;
from .fAssertTypes import fAssertTypes;
from .fbIsProvided import fbIsProvided;
from .fxGetFirstProvidedValue import fxGetFirstProvidedValue;
from .fxzGetFirstProvidedValueIfAny import fxzGetFirstProvidedValueIfAny;
from .fx0GetFirstProvidedValueOrNone import fx0GetFirstProvidedValueOrNone;
from .fx0GetProvidedValueOrNone import fx0GetProvidedValueOrNone;

__all__ = [
  "fAssertType",
  "fAssertTypes",
  "fbIsProvided",
  "fx0GetFirstProvidedValueOrNone",
  "fx0GetProvidedValueOrNone",
  "fxGetFirstProvidedValue",
  "fxzGetFirstProvidedValueIfAny",
  "zNotProvided",
];