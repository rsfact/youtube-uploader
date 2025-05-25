import os


def get_temp_dir():
    temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    return temp_dir

def sanitize_filename(title):
    filename = title.replace(' ', '_')
    filename = ''.join(c for c in filename if c.isalnum() or c in ('_', '-', '.'))
    return filename

def get_temp_file_path(filename):
    temp_dir = get_temp_dir()
    return os.path.join(temp_dir, filename)

def cleanup_temp_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def cleanup_temp_dir():
    temp_dir = get_temp_dir()
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def open_temp_dir():
    temp_dir = get_temp_dir()
    os.startfile(temp_dir)

def format_upload_message(title, url):
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'uploaded.txt')
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    return template.format(title=title, url=url)
