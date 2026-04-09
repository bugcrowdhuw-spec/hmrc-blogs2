#!/usr/bin/env python3
"""Convert blog-posts/*.md to Hugo content format with front matter."""

import os
import re
from datetime import datetime, timedelta

# Image mapping by topic
IMAGE_MAP = {
    # Group 1: High-Intent (software/automation)
    "04-": "diagram-hmrc-workflow.svg",
    "05-": "diagram-gross-vs-net.svg",
    "06-": "diagram-manual-vs-automated.svg",
    "07-": "diagram-hmrc-workflow.svg",
    "08-": "diagram-hmrc-workflow.svg",
    "09-": "diagram-gross-vs-net.svg",
    # Group 2: MTD
    "10-": "diagram-mtd-timeline-new.svg",
    "11-": "diagram-mtd-timeline-new.svg",
    "12-": "diagram-mtd-timeline-new.svg",
    "13-": "diagram-mtd-timeline-new.svg",
    "14-": "diagram-mtd-timeline-new.svg",
    "15-": "diagram-mtd-timeline-new.svg",
    # Group 3: Airbnb/STR
    "16-": "diagram-gross-vs-net.svg",
    "17-": "diagram-gross-vs-net.svg",
    "18-": "diagram-gross-vs-net.svg",
    "19-": "diagram-manual-vs-automated.svg",
    "20-": "diagram-gross-vs-net.svg",
    "21-": "diagram-hmrc-workflow.svg",
    # Group 4: Fear/Penalty
    "22-": "diagram-penalty-structure.svg",
    "23-": "diagram-penalty-structure.svg",
    "24-": "diagram-penalty-structure.svg",
    "25-": "diagram-penalty-structure.svg",
    "26-": "diagram-penalty-structure.svg",
    "27-": "diagram-mtd-timeline-new.svg",
    # Group 5: Problem-Solution
    "28-": "diagram-hmrc-workflow.svg",
    "29-": "diagram-manual-vs-automated.svg",
    "30-": "diagram-manual-vs-automated.svg",
    "31-": "diagram-hmrc-workflow.svg",
    "32-": "diagram-hmrc-workflow.svg",
    "33-": "diagram-hmrc-workflow.svg",
}

# Publishing dates (spread across weeks)
BASE_DATE = datetime(2026, 4, 7)  # Start publishing Monday 7 April

def get_slug(filename):
    """Convert filename to URL slug."""
    # Remove number prefix and .md
    name = re.sub(r'^\d+-', '', filename.replace('.md', ''))
    return name

def extract_meta_description(content):
    """Extract meta description from the bottom of the file."""
    match = re.search(r'\*\*Meta description:\*\*\s*(.+)', content)
    if match:
        return match.group(1).strip()
    return ""

def extract_tags(content):
    """Extract tags from the bottom of the file."""
    match = re.search(r'\*\*Tags:\*\*\s*(.+)', content)
    if match:
        tags = [t.strip().strip('"') for t in match.group(1).split(',')]
        return tags
    return []

def extract_title(content):
    """Extract H1 title."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Untitled"

def clean_content(content):
    """Remove the Tags and Meta description lines from content."""
    content = re.sub(r'\*\*Tags:\*\*\s*.+\n?', '', content)
    content = re.sub(r'\*\*Meta description:\*\*\s*.+\n?', '', content)
    # Remove trailing whitespace
    content = content.rstrip() + '\n'
    return content

def convert_file(src_path, dst_path, filename, index):
    """Convert a single blog post to Hugo format."""
    with open(src_path, 'r') as f:
        content = f.read()

    title = extract_title(content)
    meta_desc = extract_meta_description(content)
    tags = extract_tags(content)
    clean = clean_content(content)
    slug = get_slug(filename)

    # Get image
    prefix = filename[:3]  # e.g. "04-"
    image = IMAGE_MAP.get(prefix, "diagram-hmrc-workflow.svg")

    # Calculate publish date (staggered)
    pub_date = BASE_DATE + timedelta(days=(index // 3) * 2)  # ~3 posts per 2 days

    # Build front matter
    tags_str = ', '.join(f'"{t}"' for t in tags)

    front_matter = f"""---
title: "{title}"
date: {pub_date.strftime('%Y-%m-%d')}
draft: false
description: "{meta_desc}"
tags: [{tags_str}]
image: "/images/{image}"
slug: "{slug}"
---

"""

    # Write Hugo content
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w') as f:
        f.write(front_matter + clean)

    print(f"  ✅ {filename} → {pub_date.strftime('%Y-%m-%d')}")

def main():
    src_dir = '/root/.openclaw/workspace/blog-posts'
    dst_dir = '/root/.openclaw/workspace/hmrc-blog/content/posts'

    # Get all blog posts (04-33)
    files = sorted([f for f in os.listdir(src_dir)
                    if f.endswith('.md') and re.match(r'^\d{2}-', f)
                    and int(f[:2]) >= 4])

    print(f"Converting {len(files)} blog posts to Hugo format...\n")

    for i, filename in enumerate(files):
        src = os.path.join(src_dir, filename)
        dst = os.path.join(dst_dir, filename)
        convert_file(src, dst, filename, i)

    print(f"\n✅ Done! {len(files)} posts converted and ready for Hugo.")

if __name__ == '__main__':
    main()
