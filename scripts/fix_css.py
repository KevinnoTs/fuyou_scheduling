
import os

filepath = 'static/css/style.css'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """
.btn-outline:hover {
    background-color: var(--primary-color);
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}
"""

replacement = """
.btn-outline:hover {
    background-color: var(--primary-color);
    color: #FFFFFF !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}
"""

# Normalize validation (strip creates robustness against surrounding newlines)
if target.strip() in content:
    new_content = content.replace(target.strip(), replacement.strip())
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("CSS updated successfully via exact match.")
else:
    # Fallback: manual line reconstruction if block match fails
    print("Block match failed, trying line-by-line replacement...")
    lines = content.splitlines()
    found = False
    for i, line in enumerate(lines):
        if '.btn-outline:hover {' in line:
            # Check next few lines
            if 'background-color: var(--primary-color);' in lines[i+1] and \
               'color: #FFFFFF;' in lines[i+2]:
                lines[i+2] = '    color: #FFFFFF !important;'
                found = True
                break
    
    if found:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print("CSS updated successfully via line replacement.")
    else:
        print("Could not find target CSS to patch.")
