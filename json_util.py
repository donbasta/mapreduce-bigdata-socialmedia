import json
import os
import datetime


def flatten_to_oneline(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(data)
    text = json.dumps(data, separators=(",", ":"))
    print(text)


def mapper_facebook(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data:
        created_time = d["created_time"]
        date = created_time.split("T")[0]
        print(f"facebook\t{date}\t1")


def process_twitter_date(created_time):
    month_str_to_int = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    tokens = created_time.split()
    year = tokens[5]
    month = month_str_to_int[tokens[1]]
    date = tokens[2]
    return f"{year}-{month}-{date}"


def mapper_twitter(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data:
        created_time = d["created_at"]
        date = process_twitter_date(created_time)
        print(f"twitter\t{date}\t1")


def mapper_youtube(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data:
        published_at_time = d["snippet"]["publishedAt"]
        date = published_at_time.split("T")[0]
        print(f"youtube\t{date}\t1")


def timestamp_to_YYYYMMDD(epoch):
    return datetime.datetime.utcfromtimestamp(epoch).strftime("%Y-%m-%d")


def mapper_instagram(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data:
        timestamp_create = d["created_time"]
        date = timestamp_to_YYYYMMDD(float(timestamp_create))
        print(f"instagram\t{date}\t1")


def mapper_byu(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(type(data))


def mapper_telkomsel(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(type(data))


def mapper_myxl(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(type(data))


def mapper_anaktester(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(type(data))


def mapper_gridoto(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(type(data))


TEST_FILE = "facebook_post_1641972260556_y83jramqg4.json"
# TEST_FILE = "twitter_status_1640814809426_oyjnbbjiue.json"
# TEST_FILE = "youtube_video_1627309440619_ab5d4imwbh.json"
# TEST_FILE = "instagram_comment_1627284368139_a2xc76mtf5.json"
# TEST_FILE = "byu.id.json.json"
# TEST_FILE = "gridoto_news.json.json"
# TEST_FILE = "anaktester_go.json.json"
# TEST_FILE = "myxl.json.json"
# TEST_FILE = "telkomsel.json.json"

if __name__ == "__main__":
    for file in os.listdir("./raw_json"):
        tokens = file.split(".")
        filename_without_ext = tokens[0]
        social_media_type = filename_without_ext.split("_")[0]
        if social_media_type == "youtube":
            if file == TEST_FILE:
                mapper_youtube(f"./raw_json/{file}")
        elif social_media_type == "byu":
            if file == TEST_FILE:
                mapper_byu(f"./raw_json/{file}")
        elif social_media_type == "telkomsel":
            if file == TEST_FILE:
                mapper_telkomsel(f"./raw_json/{file}")
        elif social_media_type == "twitter":
            if file == TEST_FILE:
                mapper_twitter(f"./raw_json/{file}")
        elif social_media_type == "facebook":
            if file == TEST_FILE:
                mapper_facebook(f"./raw_json/{file}")
        elif social_media_type == "myxl":
            if file == TEST_FILE:
                mapper_myxl(f"./raw_json/{file}")
        elif social_media_type == "instagram":
            if file == TEST_FILE:
                mapper_instagram(f"./raw_json/{file}")
        elif social_media_type == "anaktester":
            if file == TEST_FILE:
                mapper_anaktester(f"./raw_json/{file}")
        elif social_media_type == "gridoto":
            if file == TEST_FILE:
                mapper_gridoto(f"./raw_json/{file}")
