import requests
import os

api_key = os.environ.get('YOUTUBE_API_KEY')
api_url = 'https://www.googleapis.com/youtube/v3/commentThreads'


def get_comment_threads(video_id, next_page_token=None):
    querystring = {
        'part': 'snippet',
        'videoId': video_id,
        'maxResults': 100,
        'textFormat': 'plainText',
        'key': api_key
    }

    if next_page_token != None:
        print('adding nextPageToken')
        querystring['pageToken'] = next_page_token

    response = requests.get(api_url, params=querystring).json()

    comment_data = []

    for item in response['items']:
        snippet = item['snippet']['topLevelComment']['snippet']

        comment = {}
        comment['text_display'] = snippet['textDisplay']
        # comment['text_original'] = snippet['textOriginal']
        comment['author_display_name'] = snippet['authorDisplayName']
        comment['author_profile_image_url'] = snippet['authorProfileImageUrl']
        comment['published_at'] = snippet['publishedAt']
        comment['updated_at'] = snippet['updatedAt']

        comment_data.append(comment)

    next_page_token = response['nextPageToken']
    print('total results: ' + str(response['pageInfo']['totalResults']))

    return [comment_data, next_page_token]
