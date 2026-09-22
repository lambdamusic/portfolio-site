"""
Helpers for reading and rewriting YAML-ish list blocks in the blog markdown
frontmatter.

The blog posts are the source of truth for their own metadata (see
TAGS_PLAN.md), so the consolidation commands edit these blocks in place. Only
the block being targeted is ever touched: the rest of the frontmatter and the
whole body are copied through byte for byte.

A block looks like this, and `tags:` / `categories:` behave identically:

    ---
    title: "..."
    categories:
      - "computermusic"
    tags:
      - "livecoding"
    ---

Used by: manage.py tags_apply, manage.py categories_apply
"""

LIST_INDENT = "  "


def split_frontmatter(lines, key):
    """Locate the `<key>:` list block inside the frontmatter.

    Returns a (start, end) pair of line indexes covering the `<key>:` line and
    its `- "..."` items, or None if the post has no such block.
    """
    fences = [i for i, l in enumerate(lines) if l.rstrip("\n") == "---"]
    if len(fences) < 2:
        return None
    head_start, head_end = fences[0], fences[1]

    prefix = key + ":"
    for i in range(head_start + 1, head_end):
        line = lines[i]
        if line.startswith(prefix) and not line[len(prefix):].strip():
            end = i + 1
            while end < head_end and lines[end].strip().startswith("-"):
                end += 1
            return (i, end)
    return None


def read_list(lines, block):
    """Read the values out of a block located by split_frontmatter()."""
    start, end = block
    return [
        lines[i].replace("- ", "", 1).strip().strip('"').lower()
        for i in range(start + 1, end)
    ]


def render_list(values, header):
    """Render a block, preserving the file's own `<key>:` header line.

    Items are indented with LIST_INDENT to match the surrounding frontmatter -
    the parser accepts any indentation, but a gratuitous reformat makes the
    git diff unreadable.
    """
    if not values:
        return []
    return [header] + [f'{LIST_INDENT}- "{v}"\n' for v in values]
