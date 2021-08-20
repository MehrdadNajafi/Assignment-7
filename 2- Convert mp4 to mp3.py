from moviepy import editor
video = editor.VideoFileClip('Eminem - Venom.mp4')
video.audio.write_audiofile('Eminem - Venom.mp3')