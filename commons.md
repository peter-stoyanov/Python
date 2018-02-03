### Python helpers

# Inspect modules
- dir(math)
- help(math.log10)
- from astropy.table import * = imports all definitions and functions + adds them to current namespace
- add search path for modules to the standard places
    import sys
    sys.path.insert(0, '/my/path/python/packages')
- pdb.set_trace() = Set a trace using Python Debugger
- print(*some imported module*.__file__)
- import this or antigravity
- import statistics
    import statistics as s
        from statistics import mean
        from statistics import mean, median
            from statistics import mean as m
            from statistics import mean as m, median as d
                from statistics import *

# Notes
- chain compaisons: 1 < 2 > 0 is True
- indexing [incl, excl)
- range() is generator - does not keep numbers in memory




