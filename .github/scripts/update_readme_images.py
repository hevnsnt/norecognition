#!/usr/bin/env python3
"""
Update README.md with the latest anomaly images from GCS.

This script reads a list of anomaly image URLs from 'anomalies.txt',
generates an HTML table with 3 columns and 3 rows (9 images total),
and updates the README.md file between the marker comments.
"""

import re
import sys
from pathlib import Path

def generate_image_table(urls):
    """Generate an HTML table with anomaly images (3x3 grid)."""
    if len(urls) < 9:
        print(f"Warning: Only {len(urls)} anomaly URLs found, expected 9")
        # Pad with empty cells if needed
        urls = urls + [''] * (9 - len(urls))

    # Only use first 9
    urls = urls[:9]

    table = '<table align="center" style="border-collapse:collapse; border-spacing:0; padding:0; margin:0;">\n'

    # Create 3 rows with 3 images each
    for row in range(3):
        table += '  <tr>\n'
        for col in range(3):
            idx = row * 3 + col
            if idx < len(urls) and urls[idx]:
                # Extract filename from URL for alt text
                filename = urls[idx].split('/')[-1]
                table += f'    <td style="padding:0; margin:0;"><a href="{urls[idx]}"><img src="{urls[idx]}" alt="{filename}" width="200" style="display:block; margin:0; padding:0;"></a></td>\n'
            else:
                # Empty cell
                table += '    <td style="padding:0; margin:0; width:200px;"></td>\n'
        table += '  </tr>\n'

    table += '</table>'
    return table

def update_readme(table_html):
    """Update README.md with the new image table."""
    readme_path = Path('README.md')

    if not readme_path.exists():
        print("Error: README.md not found")
        sys.exit(1)

    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if markers exist
    if '<!-- RECENT_ANOMALIES_START -->' not in content or '<!-- RECENT_ANOMALIES_END -->' not in content:
        print("Error: Markers not found in README.md")
        print("Please add the following markers to README.md:")
        print("<!-- RECENT_ANOMALIES_START -->")
        print("<!-- RECENT_ANOMALIES_END -->")
        sys.exit(1)

    # Replace content between markers
    pattern = r'(<!-- RECENT_ANOMALIES_START -->).*?(<!-- RECENT_ANOMALIES_END -->)'
    replacement = f'\\1\n{table_html}\n\\2'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Write back to README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ README.md updated successfully with latest anomaly images")

def main():
    """Main function."""
    anomalies_file = Path('anomalies.txt')

    if not anomalies_file.exists():
        print("Error: anomalies.txt not found")
        sys.exit(1)

    # Read URLs from file
    with open(anomalies_file, 'r') as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]

    print(f"📊 Processing {len(urls)} anomaly URLs...")

    if len(urls) == 0:
        print("Warning: No anomaly URLs found in anomalies.txt")
        sys.exit(0)

    # Generate table HTML
    table_html = generate_image_table(urls)

    # Update README
    update_readme(table_html)

    print(f"✨ Updated README.md with {min(len(urls), 9)} images")

if __name__ == '__main__':
    main()
