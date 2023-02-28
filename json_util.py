import json
import os
import datetime
import time


def flatten_to_oneline(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        text = json.dumps(data, separators=(",", ":"))
        with open(f"{json_file}.flatten.json", "w") as f:
            f.write(text)
    except:
        pass


def mapper_facebook(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data:
            created_time = d["created_time"]
            date = created_time.split("T")[0]
            print(f"facebook\t{date}\t1")
    except:
        pass


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
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data:
            created_time = d["created_at"]
            date = process_twitter_date(created_time)
            print(f"twitter\t{date}\t1")
    except:
        pass


def mapper_youtube(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data:
            published_at_time = d["snippet"]["publishedAt"]
            date = published_at_time.split("T")[0]
            print(f"youtube\t{date}\t1")
    except:
        pass


def timestamp_to_YYYYMMDD(epoch):
    return datetime.datetime.utcfromtimestamp(epoch).strftime("%Y-%m-%d")


def mapper_instagram(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data:
            timestamp_create = d["created_time"]
            date = timestamp_to_YYYYMMDD(float(timestamp_create))
            print(f"instagram\t{date}\t1")
    except:
        pass


def mapper_byu(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data["GraphImages"]:
            timestamp_taken = d["taken_at_timestamp"]
            date = timestamp_to_YYYYMMDD(timestamp_taken)
            print(f"byu\t{date}\t1")
    except:
        pass


def mapper_telkomsel(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data["GraphImages"]:
            timestamp_taken = d["taken_at_timestamp"]
            date = timestamp_to_YYYYMMDD(timestamp_taken)
            print(f"telkomsel\t{date}\t1")
    except:
        pass


def mapper_myxl(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data["GraphImages"]:
            timestamp_taken = d["taken_at_timestamp"]
            date = timestamp_to_YYYYMMDD(timestamp_taken)
            print(f"myxl\t{date}\t1")
    except:
        pass


def mapper_anaktester(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data["GraphImages"]:
            if "taken_at_timestamp" not in d.keys():
                continue
            timestamp_taken = d["taken_at_timestamp"]
            date = timestamp_to_YYYYMMDD(timestamp_taken)
            print(f"anaktester\t{date}\t1")
    except:
        pass


def mapper_gridoto(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        for d in data["GraphImages"]:
            timestamp_taken = d["taken_at_timestamp"]
            date = timestamp_to_YYYYMMDD(timestamp_taken)
            print(f"gridoto\t{date}\t1")
    except:
        pass


if __name__ == "__main__":
    START_TIME = time.time()

    for file in os.listdir("./raw_json"):
        tokens = file.split(".")
        filename_without_ext = tokens[0]
        social_media_type = filename_without_ext.split("_")[0]

        if social_media_type == "youtube":
            mapper_youtube(f"./raw_json/{file}")
        elif social_media_type == "byu":
            mapper_byu(f"./raw_json/{file}")
        elif social_media_type == "telkomsel":
            mapper_telkomsel(f"./raw_json/{file}")
        elif social_media_type == "twitter":
            mapper_twitter(f"./raw_json/{file}")
        elif social_media_type == "facebook":
            mapper_facebook(f"./raw_json/{file}")
        elif social_media_type == "myxl":
            mapper_myxl(f"./raw_json/{file}")
        elif social_media_type == "instagram":
            mapper_instagram(f"./raw_json/{file}")
        elif social_media_type == "anaktester":
            mapper_anaktester(f"./raw_json/{file}")
        elif social_media_type == "gridoto":
            mapper_gridoto(f"./raw_json/{file}")

    END_TIME = time.time()
