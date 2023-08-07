import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")

    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

import markdown2
def convert_markdown_to_html(markdown_text):
    return markdown2.markdown(markdown_text)


import re
def convert_markdown_to_html2(markdown_text):
    # Convert headings
    markdown_text = re.sub(r'# (.+)', r'<h1>\1</h1>', markdown_text)
    markdown_text = re.sub(r'## (.+)', r'<h2>\1</h2>', markdown_text)
    # Convert boldface text
    markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', markdown_text)
    # Convert unordered lists
    markdown_text = re.sub(r'\n\* (.+)', r'<li>\1</li>', markdown_text)
    markdown_text = re.sub(r'<li>(.+)</li>', r'<ul><li>\1</li></ul>', markdown_text)
    # Convert links
    markdown_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown_text)
    # Convert paragraphs
    markdown_text = re.sub(r'\n\n(.+?)\n\n', r'<p>\1</p>', markdown_text, flags=re.DOTALL)
    
    return markdown_text

