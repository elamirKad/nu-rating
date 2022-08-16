import requests
import json

def return_rating(link):
    cookies = {
        '__stripe_mid': '7b95eb48-7e92-492c-bc68-f080d4700cdc527ad7',
        'csrftoken': '9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj',
        'c_a_u': 'ZWxhbWlya2Fk:1oNd3S:iLsnvAfAKpYVLmVkpz4aHeWaPd0',
        'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk0MDA0MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjFiZWFiMzc0ZDE0NmNjMDgxYzljNWY2ODFjMjljNjkxYTRkYWE4YzIiLCJpZCI6Mzk0MDA0MiwiZW1haWwiOiJlbGFtaXJrYWRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJlbGFtaXJrYWQiLCJ1c2VyX3NsdWciOiJlbGFtaXJrYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2MDE0NDExMC5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NjA0MTAzNDYsImlwIjoiODcuMjU1LjIxNi43NSIsImlkZW50aXR5IjoiNGNhNDJmNzhmZGE0Mzc1ODJlNzdiOWY5YTQ1YzMzNzYiLCJzZXNzaW9uX2lkIjoyNTY4Njg5OH0.-rE2i8MIp42u4t5xdhLd0ikTgvREcM73w1UAkPPelIM',
    }

    headers = {
        'authority': 'leetcode.com',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,es;q=0.6',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__stripe_mid=7b95eb48-7e92-492c-bc68-f080d4700cdc527ad7; csrftoken=9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj; c_a_u=ZWxhbWlya2Fk:1oNd3S:iLsnvAfAKpYVLmVkpz4aHeWaPd0; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk0MDA0MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjFiZWFiMzc0ZDE0NmNjMDgxYzljNWY2ODFjMjljNjkxYTRkYWE4YzIiLCJpZCI6Mzk0MDA0MiwiZW1haWwiOiJlbGFtaXJrYWRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJlbGFtaXJrYWQiLCJ1c2VyX3NsdWciOiJlbGFtaXJrYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2MDE0NDExMC5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NjA0MTAzNDYsImlwIjoiODcuMjU1LjIxNi43NSIsImlkZW50aXR5IjoiNGNhNDJmNzhmZGE0Mzc1ODJlNzdiOWY5YTQ1YzMzNzYiLCJzZXNzaW9uX2lkIjoyNTY4Njg5OH0.-rE2i8MIp42u4t5xdhLd0ikTgvREcM73w1UAkPPelIM',
        'origin': 'https://leetcode.com',
        'referer': 'https://leetcode.com/ressley/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
        'x-csrftoken': '9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj',
        'x-kl-ajax-request': 'Ajax_Request',
    }
    #\n    query userContestRankingInfo($username: String!) {\n  userContestRanking(username: $username) {\n    attendedContestsCount\n    rating\n    topPercentage\n    }\n  }\n

    json_data = {
        'query': '\n    query userContestRankingInfo($username: String!) {\n  userContestRanking(username: $username) {\n    attendedContestsCount\n    rating\n    globalRanking\n    totalParticipants\n    topPercentage\n    badge {\n      name\n    }\n  }\n  userContestRankingHistory(username: $username) {\n    attended\n    trendDirection\n    problemsSolved\n    totalProblems\n    finishTimeInSeconds\n    rating\n    ranking\n    contest {\n      title\n      startTime\n    }\n  }\n}\n    ',
        'variables': {
            'username': link,
        },
    }

    response = requests.post('https://leetcode.com/graphql/', cookies=cookies, headers=headers, json=json_data)
    data = json.loads(response.text)
    print(data['data']['userContestRankingHistory'][-2])
    try:
        temp = round(data["data"]["userContestRanking"]["rating"])
    except:
        temp = 0
    try:
        contests_num = data["data"]["userContestRanking"]["attendedContestsCount"]
    except:
        contests_num = 0
    try:
        percentage = data["data"]["userContestRanking"]['topPercentage']
    except:
        percentage = 0

    return temp, contests_num, percentage
return_rating('sulrz')


def return_tasks(username):

    cookies = {
        '__stripe_mid': '7b95eb48-7e92-492c-bc68-f080d4700cdc527ad7',
        'csrftoken': '9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj',
        'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk0MDA0MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjFiZWFiMzc0ZDE0NmNjMDgxYzljNWY2ODFjMjljNjkxYTRkYWE4YzIiLCJpZCI6Mzk0MDA0MiwiZW1haWwiOiJlbGFtaXJrYWRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJlbGFtaXJrYWQiLCJ1c2VyX3NsdWciOiJlbGFtaXJrYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2MDE0NDExMC5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NjA1ODM2NzcsImlwIjoiODcuMjU1LjIxNi44OCIsImlkZW50aXR5IjoiNGNhNDJmNzhmZGE0Mzc1ODJlNzdiOWY5YTQ1YzMzNzYiLCJzZXNzaW9uX2lkIjoyNTY4Njg5OH0.p4IKIdJwy5m8HoSy9PPsFbzk8lBVKgN30WtbaHizQz0',
    }

    headers = {
        'authority': 'leetcode.com',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,es;q=0.6',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__stripe_mid=7b95eb48-7e92-492c-bc68-f080d4700cdc527ad7; csrftoken=9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk0MDA0MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjFiZWFiMzc0ZDE0NmNjMDgxYzljNWY2ODFjMjljNjkxYTRkYWE4YzIiLCJpZCI6Mzk0MDA0MiwiZW1haWwiOiJlbGFtaXJrYWRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJlbGFtaXJrYWQiLCJ1c2VyX3NsdWciOiJlbGFtaXJrYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2MDE0NDExMC5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NjA1ODM2NzcsImlwIjoiODcuMjU1LjIxNi44OCIsImlkZW50aXR5IjoiNGNhNDJmNzhmZGE0Mzc1ODJlNzdiOWY5YTQ1YzMzNzYiLCJzZXNzaW9uX2lkIjoyNTY4Njg5OH0.p4IKIdJwy5m8HoSy9PPsFbzk8lBVKgN30WtbaHizQz0',
        'origin': 'https://leetcode.com',
        'referer': 'https://leetcode.com/aseiilkhan/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
        'x-csrftoken': '9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj',
        'x-kl-ajax-request': 'Ajax_Request',
    }

    json_data = {
        'query': '\n    query userProblemsSolved($username: String!) {\n  matchedUser(username: $username) {\n    submitStatsGlobal {\n      acSubmissionNum {\n        difficulty\n        count\n      }\n    }\n  }\n}\n    ',
        'variables': {
            'username': username,
        },
    }

    response = requests.post('https://leetcode.com/graphql/', cookies=cookies, headers=headers, json=json_data)
    data = json.loads(response.text)
    arr = data["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
    easy = arr[1]["count"]
    medium = arr[2]["count"]
    hard = arr[3]["count"]
    return easy,medium,hard

def get_image(username):
    import requests

    cookies = {
        '__stripe_mid': '7b95eb48-7e92-492c-bc68-f080d4700cdc527ad7',
        'csrftoken': '9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj',
        'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk0MDA0MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjFiZWFiMzc0ZDE0NmNjMDgxYzljNWY2ODFjMjljNjkxYTRkYWE4YzIiLCJpZCI6Mzk0MDA0MiwiZW1haWwiOiJlbGFtaXJrYWRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJlbGFtaXJrYWQiLCJ1c2VyX3NsdWciOiJlbGFtaXJrYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2MDE0NDExMC5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NjA1ODM2NzcsImlwIjoiMTg1LjQ4LjE0OC4xODgiLCJpZGVudGl0eSI6IjRjYTQyZjc4ZmRhNDM3NTgyZTc3YjlmOWE0NWMzMzc2Iiwic2Vzc2lvbl9pZCI6MjU2ODY4OTh9.nEXCBrK0EImkWB4UsuOJZJAaCWJtEQva-eAAybw0eUk',
    }

    headers = {
        'authority': 'leetcode.com',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,es;q=0.6',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__stripe_mid=7b95eb48-7e92-492c-bc68-f080d4700cdc527ad7; csrftoken=9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMzk0MDA0MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjFiZWFiMzc0ZDE0NmNjMDgxYzljNWY2ODFjMjljNjkxYTRkYWE4YzIiLCJpZCI6Mzk0MDA0MiwiZW1haWwiOiJlbGFtaXJrYWRAZ21haWwuY29tIiwidXNlcm5hbWUiOiJlbGFtaXJrYWQiLCJ1c2VyX3NsdWciOiJlbGFtaXJrYWQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2MDE0NDExMC5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NjA1ODM2NzcsImlwIjoiMTg1LjQ4LjE0OC4xODgiLCJpZGVudGl0eSI6IjRjYTQyZjc4ZmRhNDM3NTgyZTc3YjlmOWE0NWMzMzc2Iiwic2Vzc2lvbl9pZCI6MjU2ODY4OTh9.nEXCBrK0EImkWB4UsuOJZJAaCWJtEQva-eAAybw0eUk',
        'origin': 'https://leetcode.com',
        'referer': 'https://leetcode.com/sulrz/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
        'x-csrftoken': '9LNO9dIUeEQy2OlTzzdCjWiE7hAbV5l7lZMuJbHu5zjcF8ljvAdVlbrqrd4ZfKPj',
        'x-kl-ajax-request': 'Ajax_Request',
    }

    json_data = {
        'query': '\n    query userProfile($username: String!) {\n  matchedUser(username: $username) {\n  profile {\n       userAvatar\n      }\n  }\n}\n    ',
        'variables': {
            'username': username,
        },
    }

    response = requests.post('https://leetcode.com/graphql/', cookies=cookies, headers=headers, json=json_data)
    data = json.loads(response.text)
    return data["data"]["matchedUser"]["profile"]["userAvatar"]