import json
import os

input_path = r'c:\Users\user\OneDrive\Documents\antigravity+n8n\WhatsApp Agent With Booking json.json'
output_path = r'c:\Users\user\OneDrive\Documents\antigravity+n8n\case-study-1-workflow.json'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Rename the workflow
data['name'] = "Case 1: WhatsApp AI Booking Concierge"

# Recursively strip credentials and sensitive info
def clean_node(node):
    if 'credentials' in node:
        for cred_type in node['credentials']:
            node['credentials'][cred_type] = {
                "id": "",
                "name": "[REDACTED]"
            }
    # Optional: Clear hardcoded IDs in parameters if they look like credentials
    if 'parameters' in node:
        params = node['parameters']
        if 'documentId' in params and isinstance(params['documentId'], dict):
            if params['documentId'].get('mode') == 'list':
                params['documentId']['value'] = "YOUR_GOOGLE_SHEET_ID"
        if 'calendar' in params and isinstance(params['calendar'], dict):
            if params['calendar'].get('mode') == 'list':
                params['calendar']['value'] = "YOUR_CALENDAR_ID"

for node in data.get('nodes', []):
    clean_node(node)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Cleaned JSON saved to {output_path}")
