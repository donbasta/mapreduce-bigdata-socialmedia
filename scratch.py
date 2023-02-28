import datetime
import json
import os


def flatten_to_oneline(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(data)
    text = json.dumps(data, separators=(",", ":"))
    print(text)


def mapper_facebook(json_file):
    with open(json_file) as f:
        data = json.load(f)
    print(type(data))
    print(len(data))
    for d in data:
        created_time = d["created_time"]
        date = created_time.split("T")[0]
        print(f"facebook\t{date}\t1")

    # dict_keys(['shares', 'crawler_target', 'created_time', 'updated_time', 'comments', 'attachments', 'status_type', 'from', 'id', 'message', 'likes'])
    # print(data[0]["shares"])
    # print(data[0]["crawler_target"])
    # print(data[0]["created_time"])
    # print(data[0]["updated_time"])
    # print(data[0]["comments"])
    # print(data[0]["comments"].keys())
    # print(data[0]["comments"]["summary"])
    # print(type(data[0]["comments"]["data"]))
    # print(len(data[0]["comments"]["data"]))
    # print(data[0]["comments"]["data"][0])
    # print(type(data[0]["comments"]["summary"]))
    # print(data[0]["comments"]["summary"])
    # print(type(data[0]["comments"]))
    # print(data[0]["status_type"])
    # print(data[0]["from"])
    # print(data[0]["id"])
    # print(data[0]["message"])
    # print(data[0]["likes"].keys())
    # print(data[0]["likes"])
    # text = json.dumps(data, indent=4)
    # print(text)


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
    # print(type(data))
    # print(len(data))
    # print(data[0].keys())
    # print(data[0]["snippet"].keys())
    # print(data[0]["crawler_target"])
    # print(data[0]["kind"])
    # print(data[0]["etag"])
    # print(data[0]["id"])
    # print(data[0]["statistics"])


def timestamp_to_YYYYMMDD(epoch):
    return datetime.datetime.utcfromtimestamp(epoch).strftime("%Y-%m-%d")


def mapper_instagram(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data:
        timestamp_create = d["created_time"]
        date = timestamp_to_YYYYMMDD(float(timestamp_create))
        print(f"instagram\t{date}\t1")

    print(type(data))
    print(len(data))
    print(data[0].keys())
    print(data[0]["crawler_target"])
    print(data[0]["created_time"])
    print(data[0]["parent"])
    print(data[0]["comment"])
    print(data[0]["id"])
    print(data[0]["text"])
    print(data[0]["user"])
    print(data[0]["likes"])


def mapper_byu(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data["GraphImages"]:
        timestamp_taken = d["taken_at_timestamp"]
        date = timestamp_to_YYYYMMDD(timestamp_taken)
        print(f"byu\t{date}\t1")

    print(type(data))
    print(data.keys())
    print(type(data["GraphImages"]))
    print(len(data["GraphImages"]))
    print(type(data["GraphImages"][0]))
    print(data["GraphImages"][0].keys())
    print(data["GraphImages"][0]["taken_at_timestamp"])


def mapper_telkomsel(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data["GraphImages"]:
        timestamp_taken = d["taken_at_timestamp"]
        date = timestamp_to_YYYYMMDD(timestamp_taken)
        print(f"telkomsel\t{date}\t1")


def mapper_myxl(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data["GraphImages"]:
        timestamp_taken = d["taken_at_timestamp"]
        date = timestamp_to_YYYYMMDD(timestamp_taken)
        print(f"myxl\t{date}\t1")


def mapper_anaktester(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data["GraphImages"]:
        timestamp_taken = d["taken_at_timestamp"]
        date = timestamp_to_YYYYMMDD(timestamp_taken)
        print(f"anaktester\t{date}\t1")


def mapper_gridoto(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for d in data["GraphImages"]:
        timestamp_taken = d["taken_at_timestamp"]
        date = timestamp_to_YYYYMMDD(timestamp_taken)
        print(f"gridoto\t{date}\t1")


# TEST_FILE = "facebook_post_1641972260556_y83jramqg4.json"
# TEST_FILE = "twitter_status_1640814809426_oyjnbbjiue.json"
# TEST_FILE = "youtube_video_1627309440619_ab5d4imwbh.json"
# TEST_FILE = "youtube_comment_1644855992219_ncv8vn0axf.json"
# TEST_FILE = "instagram_comment_1627284368139_a2xc76mtf5.json"
# TEST_FILE = "instagram_post_1641997533866_pfutcq3ovp.json"
# TEST_FILE = "instagram_media_1643019353547.json"
# TEST_FILE = "instagram_status_1643951410051.json"
# TEST_FILE = "byu.id.json.json.flatten.json"
# TEST_FILE = "gridoto_news.json.json.flatten.json"
# TEST_FILE = "anaktester_go.json.json.flatten.json"
# TEST_FILE = "myxl.json.json.flatten.json"
TEST_FILE = "telkomsel.json.json.flatten.json"

if __name__ == "__main__":
    for file in os.listdir("./raw_json"):
        tokens = file.split(".")
        filename_without_ext = tokens[0]
        social_media_type = filename_without_ext.split("_")[0]
        if social_media_type == "youtube":
            pass
        elif social_media_type == "byu":
            pass
        elif social_media_type == "telkomsel":
            pass
        elif social_media_type == "twitter":
            pass
        elif social_media_type == "facebook":
            if file == TEST_FILE:
                mapper_facebook(f"./raw_json/{file}")
        elif social_media_type == "myxl":
            pass
        elif social_media_type == "instagram":
            pass
        elif social_media_type == "anaktester":
            pass
        elif social_media_type == "gridoto":
            pass

        # if file == TEST_FILE:
        #     convert_to_oneline(f"./raw_json/{file}")
