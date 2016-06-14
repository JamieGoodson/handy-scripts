import sys
import subprocess

ffmpeg_path = "C:\\Program Files (x86)\\ffmpeg\\ffmpeg-20160610-git-0a9e781-win64-static\\bin\\ffmpeg.exe" # Point to ffmpeg.exe location

#print("Arguments:", str(sys.argv))

print("|==========================|")
print("|=== CONVERT MKV TO MP4 ===|")
print("|==========================|\n")

if len(sys.argv) > 1:
    input_file_path = sys.argv[1]
    output_file_path = input_file_path.replace(".mkv", ".mp4")
    #subprocess.call([ffmpeg_path, "-i", input_file_path, "-vcodec", "copy", "-acodec", "aac", output_file_path])
    #subprocess.call([ffmpeg_path, "-v", "9", -loglevel, "99", "-i", input_file_path], stdout=f)
    subprocess.call([ffmpeg_path, "-i", input_file_path, "-vcodec", "copy", "-c:a", "aac", "-map", "0", output_file_path])
else:
    print("Error: No input file given.\n\nDrag and drop a .mkv file onto this script and it will be converted to .mp4.\nPlease close this window and try again.")
    input()
