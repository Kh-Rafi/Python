import re
import sys

def solve_html_parser_final():
    try:
        n = int(input().strip())
    except (EOFError, ValueError):
        return

    lines = []
    for _ in range(n):
        try:
            lines.append(input())
        except EOFError:
            break
            
    html_content = "\n".join(lines)
    
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
    
    tag_pattern = re.compile(r'<([a-zA-Z0-9]+)([^>]*?)>', flags=re.DOTALL)
    
    attr_pattern = re.compile(r'([\w-]+)\s*=\s*(?:["\'](.*?)["\']|([^\s>]+))', flags=re.DOTALL)
    
    for match in tag_pattern.finditer(html_content):
        tag_name = match.group(1)
        attrs_part = match.group(2).strip()
        
        print(tag_name)
        
        if attrs_part.endswith('/'):
            attrs_part = attrs_part[:-1].strip()
            
        attrs = attr_pattern.findall(attrs_part)
        for attr in attrs:
            attr_name = attr[0]
            attr_value = attr[1] if attr[1] != '' else attr[2]
            
            print(f"-> {attr_name} > {attr_value}")

if __name__ == '__main__':
    solve_html_parser_final()
