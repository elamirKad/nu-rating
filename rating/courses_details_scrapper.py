import requests


def get_course_details(course):
    cookies = {
        '__ddg1_': 'X1MzoMM14pIu4729BQea',
        'has_js': '1',
    }

    headers = {
        'authority': 'registrar.nu.edu.kz',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,es;q=0.6',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__ddg1_=X1MzoMM14pIu4729BQea; has_js=1',
        'origin': 'https://registrar.nu.edu.kz',
        'referer': 'https://registrar.nu.edu.kz/course-catalog',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'method': 'getSearchData',
        'searchParams[formSimple]': 'false',
        'searchParams[limit]': '10',
        'searchParams[page]': '1',
        'searchParams[start]': '0',
        'searchParams[quickSearch]': course,
        'searchParams[sortField]': '-1',
        'searchParams[sortDescending]': '-1',
        'searchParams[semester]': '-1',
        'searchParams[schools]': '',
        'searchParams[departments]': '',
        'searchParams[levels]': '',
        'searchParams[subjects]': '',
        'searchParams[instructors]': '',
        'searchParams[breadths]': '',
        'searchParams[abbrNum]': '',
        'searchParams[credit]': '',
    }

    response = requests.post('https://registrar.nu.edu.kz/my-registrar/public-course-catalog/json', cookies=cookies, headers=headers, data=data)
    try:
        return response.json()['data'][0]
    except:
        print("Course do not exists, Do it by yourself")