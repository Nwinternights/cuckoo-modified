# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.common.abstracts import Package

class PPT(Package):
    """PowerPoint analysis package."""
    PATHS = [
        ("ProgramFiles", "Microsoft Office", "POWERPNT.EXE"),
        ("ProgramFiles", "Microsoft Office", "Office*", "POWERPNT.EXE"),
    ]

    def start(self, path):
        powerpoint = self.get_path_glob("Microsoft Office PowerPoint")
        return self.execute(powerpoint, "/s \"%s\"" % path, path)
