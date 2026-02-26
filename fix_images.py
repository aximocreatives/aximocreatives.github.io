import os
import re

workspace = r'e:\AXIMO CREATIVES\WEBSITE'
assets_dir = os.path.join(workspace, 'assets')
root_files = set(os.listdir(workspace))
asset_files = set(os.listdir(assets_dir))

supabase_map = {
    'https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/40009831-39d3-43f8-90a6-35761ddc22ed_1600w.jpg': 'assets/ashu_1.jpg',
    'https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/4d5e7091-b987-41ce-a90a-37ff79c1d78f_1600w.jpg': 'assets/balaji_1.jpg',
    'https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/22b7cac9-b5d6-4152-a0f8-4d92c49b2a5f_1600w.jpg': 'assets/urban_calm_1.jpg',
    'https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/8c7e0533-064c-40de-92ec-1b14ae736d40_1600w.jpg': 'assets/office_1.jpg',
    'https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/723135be-5b19-40ac-9bff-80a4ece8529e_3840w.jpg': 'luxury-living-living-room.jpg',
    'https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/016ea5a6-1518-427b-b184-2df9702cb60e_1600w.jpg': 'aximo_logo.jpg'
}

html_files = [f for f in root_files if f.endswith('.html')]

def replacer(match):
    src = match.group(1)
    
    if src in supabase_map:
        return f'src="{supabase_map[src]}"'
        
    if src in asset_files and src not in root_files:
        return f'src="assets/{src}"'
        
    return match.group(0)

for hf in html_files:
    path = os.path.join(workspace, hf)
    print(f'Checking {hf}')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'src=\"([^\"]+)\"', replacer, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {hf}')

print("Done")
