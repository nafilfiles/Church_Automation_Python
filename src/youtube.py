from datetime import datetime

class Video:
  def __init__(self, title, speaker):
    self.title = title
    self.speaker = speaker
    self.date = datetime.now()
    self.youtube_id = None

# v1 = Video("title", "speaker")

# print(v1.title)
# print(v1.speaker)
# print(v1.date)
# print(v1.youtube_id)

print(datetime.now())