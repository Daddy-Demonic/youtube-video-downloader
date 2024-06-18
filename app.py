import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import moviepy.editor as mp
import os

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        download_path = filedialog.askdirectory()
        if download_path:
            stream.download(output_path=download_path)
            messagebox.showinfo("Success", f"Video downloaded successfully to {download_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def download_audio():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        download_path = filedialog.askdirectory()
        if download_path:
            audio_file = stream.download(output_path=download_path)
            base, ext = os.path.splitext(audio_file)
            mp3_file = base + '.mp3'
            clip = mp.AudioFileClip(audio_file)
            clip.write_audiofile(mp3_file)
            clip.close()
            os.remove(audio_file)
            messagebox.showinfo("Success", f"Audio downloaded successfully to {download_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Create and place the URL entry widget
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the download buttons
video_button = tk.Button(root, text="Download Video (MP4)", command=download_video)
video_button.pack(pady=5)

audio_button = tk.Button(root, text="Download Audio (MP3)", command=download_audio)
audio_button.pack(pady=5)

# Start the main event loop
root.mainloop()
