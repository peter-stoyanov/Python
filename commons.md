### Python helpers

# Inspect modules
- dir(math)
- help(math.log10)
- from astropy.table import * = imports all definitions and functions + adds them to current namespace
- import foo.bar = still needs namespace when calling like foo.xxxx
- add search path for modules to the standard places
    import sys
    sys.path.insert(0, '/my/path/python/packages')
- pdb.set_trace() = Set a trace using Python Debugger
- print(*some imported module*.__file__)
- import this or antigravity

# Notes
- chain compaisons: 1 < 2 > 0 is True
- indexing [incl, excl)
- range() is generator - does not keep numbers in memory




