import os
import zipfile

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def zip_all(top_dir, extensions, output_file):
  with zipfile.ZipFile(output_file, 'w') as zipf:
    for root, dirs, files in os.walk(top_dir):
      for file in files:
        if any(file.endswith(ext) for ext in extensions):
          file_path = os.path.join(root, file)
          zipf.write(file_path, os.path.relpath(file_path, top_dir))

# Example usage
if __name__ == "__main__":
  zip_all('my_stuff', ['.jpg', '.txt'], 'my_stuff.zip')