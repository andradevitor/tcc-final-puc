import csv
import os
import clients.youtube_api_client as youtube_api_client

csv_path = os.path.dirname(__file__) + '/csv/data.csv'

def save_comments(data):
    with open(csv_path, 'w', encoding='UTF8', newline='') as f:
        fieldnames = list(data[0].keys()) 
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(data)

def fetch_data():
    horizon_video_id = 'Lq594XmpPBg'

    all_comment_data = []

    [comment_data, next_page_token] = youtube_api_client.get_comment_threads(
        horizon_video_id)

    all_comment_data += comment_data

    while next_page_token != None or len(all_comment_data) < 10000:
        [comment_data, next_page_token] = youtube_api_client.get_comment_threads(
            horizon_video_id, next_page_token
        )
        all_comment_data += comment_data
        print('npt: ' + next_page_token)
        save_comments(all_comment_data)

fetch_data()

