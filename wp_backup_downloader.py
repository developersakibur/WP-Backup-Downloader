# Install requests
!pip install requests --quiet

import os, time, requests, shutil, sys, io, contextlib
from google.colab import drive, files

# 🔹 Step 1: Ask for URL
url = input("URL: ").strip()

# 🔹 Step 2: Extract filename
filename = url.split("/")[-1]

# 🔹 Step 3: Start download with simple text progress
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))
block_size = 1024 * 1024  # 1 MB

start_time = time.time()
downloaded = 0

with open(filename, "wb") as f:
    for chunk in response.iter_content(block_size):
        if chunk:
            f.write(chunk)
            downloaded += len(chunk)

            elapsed = time.time() - start_time
            speed = downloaded / 1024 / 1024 / elapsed if elapsed > 0 else 0

            print(f"\r📥 {filename}: {downloaded/1024/1024:.2f} MB | Speed: {speed:.2f} MB/s", end="")
print("")

# 🔹 Step 4: Mount Google Drive
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
      drive.mount('/content/drive', force_remount=False)

# 🔹 Step 5: Create "Website Backups" folder
backup_folder = "/content/drive/My Drive/Website Backups"
os.makedirs(backup_folder, exist_ok=True)

# 🔹 Step 6: Move file into Drive folder
drive_path = os.path.join(backup_folder, filename)
shutil.move(filename, drive_path)
print(f"✅ Saved to Drive → {drive_path}")

# 🔹 Step 7: Trigger local download
print(f"⬇️ Starting Download → {filename}")
files.download(drive_path)
