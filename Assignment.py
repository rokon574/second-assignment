import requests
from wp_function import ai_text, wp_paragraph, heading_two, headers

with open('keyword.txt', 'r+') as file:
    read_line = file.readlines()
    for keyword in read_line:
        body = []
        intro = ai_text(f'Write a intro about {keyword}')
        buying_guide_heading = heading_two(f'why {keyword} is Necessary  ')
        heading_text = ai_text(f'write about {buying_guide_heading}')
        choice_heading = heading_two('How to Choose best one')
        choice_text = ai_text(f'write about Choose {keyword}')
        features_heading = heading_two(f'what features should you consider while buying {keyword}')
        features = ai_text(f'write 200 words long paragraph about {keyword} ')
        conclusion_h = heading_two('Conclusion')
        conclusion_text = ai_text(f'write a fency 200 words long conclusion about {keyword}')
        title = f'Buying Guide of {keyword}'
        slug = keyword.replace(' ', '-')

        content = f'{intro}{buying_guide_heading}{heading_text}{choice_heading}{choice_text}{features_heading}{features}{conclusion_h}{conclusion_text}'
        data = {'title': title.title(),
                'slug': slug,
                'status': 'draft',
                'content': content,
                'categories': '1',
                'author': '1',
                'format': 'standard',
                }
        headers = headers("admin", "UZYD UGIp CjsE lN4Y 6ySH P3bY")
        endpoints = 'https://my-site.local/wp-json/wp/v2/posts'
        r = requests.post(endpoints, headers=headers, data=data, verify=False)
        print(r)
