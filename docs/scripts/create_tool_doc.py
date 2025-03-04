#!/usr/bin/env python3
import os
from datetime import datetime

def create_tool_documentation(tool_name, tool_type):
    # Read template
    with open('_templates/tool_template.md', 'r') as f:
        template = f.read()
    
    # Create tool-specific content
    content = template.replace('[Tool Name]', tool_name)
    content = content.replace('[tool-name]', tool_name.lower().replace(' ', '-'))
    content = content.replace('[YYYY-MM-DD]', datetime.now().strftime('%Y-%m-%d'))
    
    # Create tool-specific HTML include file
    html_content = f"""<!-- {tool_name} 3D Model Embed -->
<div class="sketchfab-embed-wrapper">
    <iframe 
        title="{tool_name}"
        frameborder="0"
        allowfullscreen
        mozallowfullscreen="true"
        webkitallowfullscreen="true"
        allow="autoplay; fullscreen; xr-spatial-tracking"
        xr-spatial-tracking
        execution-while-out-of-viewport
        execution-while-not-rendered
        web-share
        src="[SKETCHFAB_MODEL_URL]">
    </iframe>
</div>"""
    
    # Create files
    os.makedirs('tools', exist_ok=True)
    os.makedirs('_includes/tools', exist_ok=True)
    
    with open(f'tools/{tool_name.lower().replace(" ", "-")}.md', 'w') as f:
        f.write(content)
    
    with open(f'_includes/tools/{tool_name.lower().replace(" ", "-")}.html', 'w') as f:
        f.write(html_content)
    
    print(f"Created documentation for {tool_name}")

if __name__ == "__main__":
    tool_name = input("Enter tool name: ")
    tool_type = input("Enter tool type (power/hand/other): ")
    create_tool_documentation(tool_name, tool_type) 