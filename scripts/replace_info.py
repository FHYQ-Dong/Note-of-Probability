import os, json

conf = json.load(open('scripts/config.json', 'r', encoding='utf-8'))
secrets = json.load(open('scripts/secrets.json', 'r', encoding='utf-8'))

for root, dirs, files in os.walk(os.getcwd()):
    if os.path.split(root)[-1] in conf['exclude_dirs']:
        continue
    for file in files:
        if not os.path.splitext(file)[-1] in conf['track_filetypes']:
            continue
        if file in conf['exclude_files']:
            continue
        content, new_content = '', ''
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            content = f.read()
            new_content = content
        for k, v in secrets.items():
            new_content = new_content.replace(k, v)
        if new_content != content:
            print(f'Updating {os.path.join(root, file)}')
            with open(os.path.join(root, file), 'w', encoding='utf-8') as f:
                f.write(new_content)
