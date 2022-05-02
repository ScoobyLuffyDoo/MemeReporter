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

def topMemeDownloader(active =None):
    count = 0
    limmit_amount =30
    if active == True:
        for memes in reddit.subreddit("meme").top(limit=limmit_amount):
            # title = submission.title
            url = memes.url
            if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png") or url.endswith("gif"):
                print(url)
                filetype = fileExtention(str(url))
                urllib.request.urlretrieve(url, f"./memes/image{count}.{filetype}")
                count += 1
                if count == limmit_amount:
                    break


def learnPythonTopics(active = None):
    limmit_amount = 20
    if active == True:
        for count, topics in enumerate(reddit.subreddit("Python").hot(limit=limmit_amount)):
            title = topics.title
            url = topics.url
            print(count,title,url)


if __name__ == "__main__":
    topMemeDownloader(False)
    learnPythonTopics(True)