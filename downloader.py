from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(only_audio=True).first()
        streams.download(output_path=save_path)
        print("Audio downloaded succesfully!")
    except Exception as e:
        print(e)

def open_file_diaglog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a youtube url to download audio: ")
    save_dir = open_file_diaglog()

    if not save_dir:
        print("please select a folder...")
    else:
        download_video(video_url, save_dir)