from youtube_transcript_api import YouTubeTranscriptApi
video_id='Y6e_m9iq-4Q'
transcript=YouTubeTranscriptApi.get_transcript(video_id)
for entry in transcript:
    print(entry['text'])
with open('subtitles.tst','w', encoding='utf-8') as f :
    for entry in transcript:
        f.write(entry['text']+'\n')

# quotes = ['Be yourself; everyone else is already taken.',
#           'In the middle of difficulty lies opportunity.',
#           'Life is what happens when you\'re busy making other plans.'
#           ]

# with open('quotes.txt','w',encoding='utf-8') as f:
#     for quote in quotes:
#         f.write(quote+'\n')


from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator
video_id='Y6e_m9iq-4Q'
transcript=YouTubeTranscriptApi.get_transcript(video_id)
translator = Translator()
for entry in transcript:
    original = entry ['text']
    translated = translator.translate(original, src = 'en', dest='ko').text
    print(f"[en]{original}")
    print(f"[ko]{translated}\n")

