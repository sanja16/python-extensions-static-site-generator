@@ -1,6 +1,8 @@
import sys
from pathlib import Path

from ssg import extensions, hooks


class Site:
    def __init__(self, source, dest, parsers=None):
@@ -27,6 +29,8 @@ def run_parser(self, path):
            )

    def build(self):
        extensions.load_bundled()
        hooks.event("collect_files", self.source, self.parsers)
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
