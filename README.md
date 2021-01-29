Provides a global value that can be used to determine if an optional function
argument was not provided by the caller and that a default value should be used.

This code was created to make it easier for a function to accept a wide range
of types and values in an optional argument and still make it easy to determine
if the argument should use the provided value or a default value.

`zNotProvided`
--------------
A value for optional arguments that indicates it was not provided by the caller
and a default value should be used.

Example usage:
```
  def fPrintArgumentIfProvided(xzArgument = zNotProvided):
    if xzArgument is not zNotProvided:
      print str(xzArgument);
```

`fbIsProvided(xzValue)`
-----------------------
Returns `True` if xzValue is NOT `zNotProvided`.

Example usage:
```
  def fPrintArgumentIfProvided(xzArgument = zNotProvided):
    if fbIsProvided(xzArgument):
      print str(xzArgument);
```

`fx0GetProvidedValueOrNone(xzValue)`
-----------------------------------
Returns the argument if it is NOT `zNotProvided`.
If the argument is `zNotProvided`, return `None`.

`fx0GetFirstProvidedValueOrNone(xzValue0[, xzValue1[, ...]])`
-------------------------------------------------------------
Returns the first argument that is NOT `zNotProvided`. Returns `None` if no
arguments are passed or if all arguments are `zNotProvided`.

Example usage:
```
  def fs0GetUserIdentifier(szAlias = zNotProvided, szName = zNotProvided, szEmail = zNotProvided):
    return fx0GetFirstProvidedValueOrNone(szAlias, szName, szEmail);
```

`fxGetFirstProvidedValue(xzValue0[, xzValue1[, xzValue2]])`
-----------------------------------------------------------
Returns the first argument that is NOT `zNotProvided`. Throws an
`AssertionError` if no arguments are passed or if all arguments are
`zNotProvided`.

`fxzGetFirstProvidedValueIfAny(xzValue0[, xzValue1[, xzValue2]])`
-----------------------------------------------------------
Returns the first argument that is NOT `zNotProvided`. Returns `zNotProvided`
if no arguments are passed or if all arguments are `zNotProvided`.
