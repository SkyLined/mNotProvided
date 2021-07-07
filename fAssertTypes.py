try: # mDebugOutput use is Optional
  from mDebugOutput import HideInCallStack;
except ModuleNotFoundError as oException:
  if oException.args[0] != "No module named 'mDebugOutput'":
    raise;
  HideInCallStack = lambda x: x;

from .fAssertType import fAssertType;

# We want any exceptions triggered in this function to be shown as coming from
# the function that called it, hence we hide it in the call stack
@HideInCallStack
def fAssertTypes(dtxValueAndValueTypes_by_sName):
  # Argument is {"name": (value, type, ....), ...}
  for (sName, txValueAndValueTypes) in dtxValueAndValueTypes_by_sName.items():
    # Call fAssertType for each entry in the dict.
    fAssertType(sName, *txValueAndValueTypes);
