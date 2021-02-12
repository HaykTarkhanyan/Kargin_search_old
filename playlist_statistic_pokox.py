
from googleapiclient.discovery import build
import pandas as pd
from datetime import timedelta
import re

api_key = 'AIzaSyCnmYbeQyboORylrdE3ljoOP9pJE9lOedg'
youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'PLC4FFB3F0AFB8146C'

videos = []

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')


nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part=["statistics", "contentDetails"],
        id=','.join(vid_ids)
    )


    vid_response = vid_request.execute()

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()



        vid_views = item['statistics']['viewCount']
        likes = item['statistics']['likeCount']
        dislikes = item['statistics']['dislikeCount']
        comments = item['statistics']['commentCount']
        duration = video_seconds

        vid_id = item['id']
        yt_link = f'https://youtu.be/{vid_id}'

        videos.append(
            {
                'url': yt_link,
                'views': int(vid_views),
                'likes': int(likes),
                'dislikes': int(dislikes),
                'comments': int(comments),
                'duration': duration
            }
        )

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

videos.sort(key=lambda vid: vid['views'], reverse=True)


df = pd.DataFrame(videos)
df.to_csv('kargin_playlis_stats.csv')

print ('one')
