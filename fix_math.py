import os, re

fixed_files = 0
fixed_equations = 0

for root, dirs, files in os.walk('content'):
    for fname in files:
        if not fname.endswith('.md'):
            continue
        path = os.path.join(root, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        lines = content.split('\n')
        new_lines = []

        for line in lines:
            stripped = line.strip()

            # Skip callout lines
            if stripped.startswith('>'):
                new_lines.append(line)
                continue

            # Skip frontmatter delimiters
            if stripped == '---':
                new_lines.append(line)
                continue

            # Case 1: $$ at line start with math content after (not just $$ alone)
            if stripped.startswith('$$') and len(stripped) > 2 and not stripped[2:].isspace():
                # Put content on next line
                content_after = line[line.index('$$')+2:].lstrip()
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append(indent + '$$')
                new_lines.append(indent + content_after)
                fixed_equations += 1
                continue

            # Case 2: Content before closing $$ at end of line
            if stripped.endswith('$$') and not stripped.startswith('$$') and len(stripped) > 2:
                content_before = line[:line.rindex('$$')].rstrip()
                new_lines.append(content_before)
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append(indent + '$$')
                fixed_equations += 1
                continue

            new_lines.append(line)

        content = '\n'.join(new_lines)
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_files += 1
            print(f'Fixed: {fname}')

print(f'Files: {fixed_files}, Equations: {fixed_equations}')
