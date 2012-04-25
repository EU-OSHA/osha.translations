#!/usr/bin/env python

# Author: Wolfgang Thomas <thomas@syslab.com>

"""%(program)s: Check that all po files are sound and don't break when they
are compiled

usage:    %(program)s editor filename
editor    the editor command to use, such as mate or kate
filename  the filename to open in every language, such as osha_ew.po
"""

import sys
import os
import re
from popen2 import popen3
# import polib

# Define here the patterns for all error messages you want to ignore
messages_to_ignore = [
  '.*?entry ignored',
  '^msgfmt: found .*',
]
ignore = [re.compile(patt) for patt in messages_to_ignore]


def usage(stream, msg=None):
    if msg:
        print >> stream, msg
        print >> stream
    program = os.path.basename(sys.argv[0])
    print >> stream, __doc__ % {"program": program}
    sys.exit(0)

if len(sys.argv) < 3:
    usage(sys.stderr, "\nERROR: Not enough arguments")
editor = sys.argv[1]
filename = sys.argv[2]

dirs = [x for x in os.listdir('.') if len(x) == 2 and os.path.isdir(x)]
paths = list()
for dirname in dirs:
    path = "%s/LC_MESSAGES" % dirname
    names = [x for x in os.listdir(path) if x.endswith('po')]
    for name in names:
        if name == filename:
            paths.append(dirname)
            paths.append('%s/%s' % (path, filename))
        #print "\nchecking", name

cmd = "%s %s" % (editor, " ".join(paths))
stout, stdin, stderr = popen3(cmd)
