import typer

from ssg.site import Site
import ssg.parsers
from ssg import extensions

def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest,
        "parsers": [
            ssg.parsers.ResourceParser(),
            ssg.parsers.MarkdownParser(),
            ssg.parsers.ReStructuredTextParser(),
        ],
    }

    Site(**config).build()


typer.run(main)
