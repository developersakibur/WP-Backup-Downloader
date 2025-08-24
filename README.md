# WP Backup Downloader (All-in-One WP Migration)

A simple and reliable tool to safely download **All-in-One WP Migration `.wpress` backup files**, especially for **large files** that browsers may fail to download.  
The script uses **Google Colab** and **Google Drive** to ensure stable and fast downloads.

---

## Why Use This Tool
- Browsers often fail when downloading **large `.wpress` backup files** (>2–5GB).  
- This tool downloads backups safely using **Colab** and saves them to **Google Drive**.  
- Once saved in Drive, backups can be downloaded anytime without interruption.  

## Features
- Simple progress indicator: shows downloaded size and speed.  
- Saves backups automatically in **Google Drive → `Website Backups/`**.  
- Avoids overwriting by allowing **timestamped backup names** (if configured).  
- Optional local download for smaller files (<2–3GB).  
- Fully silent Google Drive mount — no distracting logs.  

## How to Use
1. Open [Google Colab](https://colab.research.google.com/).  
2. Copy and paste the following code into a cell **as-is**:

```python
url = "https://raw.githubusercontent.com/developersakibur/wp-backup-downloader/main/wp_backup_downloader.py"
!wget -q {url} -O temp_script.py
%run temp_script.py
```
3. Run the cell.
4. Then paste the .wpress backup file URL and boom:

## Notes
 - Ensure sufficient free space in Google Drive.
 - For extremely large files, skip Colab local download and download directly from Drive.
 - Timestamped backup names prevent overwriting older backups.
 - Works only with All-in-One WP Migration .wpress backup files.
 - Smaller backups (<2–3GB) can be downloaded directly via Colab.
 - Large backups (>5GB) should use Google Drive as a temporary storage for reliability.

## Requirements
- Google Colab
- Google Drive account
- Python 3.x (pre-installed in Colab)
