from secrets import secrets
import praw
import urllib.request


def fileExtention(inUrl):
    if inUrl.endswith('jpg'):
        extention = 'jpg'
    elif inUrl.endswith('jpeg'):
        extention = 'jpg'
    elif inUrl.endswith('png'):
        extention = 'png'
    elif inUrl.endswith('gif'):
        extention = 'gif'
    return extention


reddit = praw.Reddit(
    client_id= secrets['client_id'],
    client_secret= secrets['client_secret'],
    user_agent=secrets['user_agent'],
    username= secrets['username'],
    password=secrets['password']
)

# subreddit = r.subreddit("meme")
count = 0
limmit_amount =30
for submission in reddit.subreddit("meme").top(limit=limmit_amount):
    title = submission.title
    url = submission.url
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png") or url.endswith("gif"):
        print(url)
        filetype = fileExtention(str(url))
        urllib.request.urlretrieve(url, f"./memes/image{count}.{filetype}")
        count += 1
        if count == limmit_amount:
           break
