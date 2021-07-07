# Various modules are expected to have local copies of this utility code.
# However, they should all agree on the value of "not provided". Therefore, the
# first copy of this code creates a global variable in the context of the
# __main__ module to store this value. Subsequent copies of this code will
# use that value as well, so they all agree on the value of "not provided".
import __main__;
if not hasattr(__main__, "__zNotProvided"):
  class czNotProvided(object):
    def __bool__(oSelf):
      # fbIsProvided() should be called to check if a value is provided.
      # example of bad code:
      #   not x;
      # replace with:
      #   not fbIsProvided(x)
      # The latter will throw the below assertion:
      raise AssertionError("You should not directly use this optional value as a boolean!");
    def __cmp__(oSelf):
      # fbIsProvided() should be called to check if a value is provided.
      # example bad code:
      #   x is zNotProvided;
      # replace with:
      #   not fbIsProvided(x)
      # The latter will throw the below assertion:
      raise AssertionError("You should not directly compare this optional value to anything!");
    def __repr__(oSelf):
      return "<not provided>";
    def __str__(oSelf):
      return "<not provided>";
  __main__.__zNotProvided = czNotProvided();
zNotProvided = __main__.__zNotProvided;
