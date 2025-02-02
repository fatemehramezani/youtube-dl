import csv
import subprocess

# Path to your CSV file
csv_file = "todownload.csv"

# Read the CSV file
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    values = [row[0] for row in reader]  # Assuming values are in the first column

# Base command for yt-dlp
base_command = 'yt-dlp -P "./MyVideos" -o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"'
base_command = base_command + ' -f "(bv*+ba/b)[protocol^=http][protocol!*=dash] / (bv*+ba/b)"'
base_command = base_command + ' --split-chapters'
base_command = base_command + ' --ffmpeg-location "./ffmpeg"'
#base_command = base_command + ' --cookies-from-browser chrome --cookies "./cookies.txt"'
base_command = base_command + '--cookies-from-browser Edge  --cookies "./cookies.txt"'
# base_command = base_command + ' --default-search "ytsearch"'
# base_command = base_command + '--proxy "socks5://127.0.0.1:7890"'
base_command = base_command + ' --sleep-interval 200'

# Iterate through values and run yt-dlp for each
for value in values:
    command = f'{base_command} "{value}"'  # Append the CSV value as an argument
    print(f"Running command: {command}")
    subprocess.run(command, shell=True)
