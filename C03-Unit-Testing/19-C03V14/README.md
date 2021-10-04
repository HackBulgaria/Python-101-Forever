# C03V12 - Debugging with breakpoint

In this video we show the built-in `breakpoint`, which can be configured via env variables.

Quick configuration cheatsheet:

```
# Disables breakpoint
export PYTHONBREAKPOINT=0

# Sets ipdb as the default debugger
export PYTHONBREAKPOINT=ipdb.set_trace

# Return the default behavior
export PYTHONBREAKPOINT=
```

## Materials

* [Video](https://www.youtube.com/watch?v=LsFUpRYLuu8)

## Additional materials

* PEP 553 - <https://www.python.org/dev/peps/pep-0553/>
* <https://www.andreagrandi.it/2018/10/16/using-ipdb-with-python-37-breakpoint/>
