import os
import requests

def download_files(start_url, output_dir):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  os.chdir(script_dir)
  
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  
  base_url = start_url[:-7]  # Remove the last 7 characters (e.g., '001.jpg')
  for i in range(1, 51):
    file_number = f'{i:03}'  # Format the number with leading zeros (e.g., '001', '002', ...)
    file_url = f'{base_url}{file_number}.jpg'
    file_path = os.path.join(output_dir, f'image{file_number}.jpg')
    
    response = requests.get(file_url)
    if response.status_code == 200:
      with open(file_path, 'wb') as file:
        file.write(response.content)
      print(f'Downloaded: {file_url}')
    else:
      print(f'Failed to download: {file_url}')

# Example usage:
# download_files('http://699340.youcanlearnit.net/image001.jpg', './images')

if __name__ == '__main__':
    download_files('http://699340.youcanlearnit.net/image001.jpg', './images')