from markdown import markdown
from ssg.content import Content

from ssg import hooks


class Parser:
    base_ext = ".html"
@@ -45,7 +47,8 @@ class MarkdownParser(Parser):
    def parse(self, path, source, dest):
        content = Content.load(self.read(path))
        html = markdown(content.body)
        self.write(path, dest, html)
        filtered = hooks.filter("generate_menu", html, self.base_ext)
        self.write(path, dest, filtered)
        sys.stdout.write(
            "\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content)
        )
@@ -57,7 +60,8 @@ class ReStructuredTextParser(Parser):
    def parse(self, path, source, dest):
        content = Content.load(self.read(path))
        html = publish_parts(content.body, writer_name="html5")
        self.write(path, dest, html["html_body"])
        filtered = hooks.filter("generate_menu", html["html_body"], self.base_ext)
        self.write(path, dest, filtered)
        sys.stdout.write(
            "\x1b[1;32m{} converted to HTML. Metadata: {}\n".format(path.name, content)
        )
