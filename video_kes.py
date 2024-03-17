from moviepy.video.io.VideoFileClip import VideoFileClip

# Videoyu yükleyin
video = VideoFileClip("video.mp4")

# Belirli zaman aralığını kesmek için başlangıç ve bitiş zamanlarını belirtin
start_time = 10  # Başlangıç zamanı (saniye cinsinden)
end_time = 30    # Bitiş zamanı (saniye cinsinden)

# Belirtilen zaman aralığını kesin
trimmed_video = video.subclip(start_time, end_time)

# Kesilmiş videoyu kaydedin
trimmed_video.write_videofile("kesilmis_video.mp4")
