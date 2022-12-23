def ai_text(prompt):
    import os
    from dotenv import load_dotenv
    import openai
    openai.api_key = os.getenv('API_KEY')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text').strip()
    codes = f'<!-- wp:paragraph --><p>{output}</p> <!-- /wp:paragraph -->'
    return codes

def text_formating(text):
    text = text.replace('.','.---').split('---')
    retun_text1 = '<!-- wp:paragraph --><p>' + ''.join(text[0:2]) + '</p><!-- /wp:paragraph -->'
    retun_text2 = '<!-- wp:paragraph --><p>' + ''.join(text[2:4]) + '</p><!-- /wp:paragraph -->'
    retun_text3 = '<!-- wp:paragraph --><p>' + ''.join(text[4:]) + '</p><!-- /wp:paragraph -->'
    return retun_text1+retun_text2+retun_text3

def wp_paragraph(text):
    codes = f'<!-- wp:paragraph --><p>{text}</p> <!-- /wp:paragraph -->'
    return codes

def heading_two(text):
    codes= f'<!-- wp:heading --> <h2>{text}</h2> <!-- /wp:heading -->'
    return codes

def heading_three(text):
    codes= f'<!-- wp:heading --> <h3>{text}</h3> <!-- /wp:heading -->'
    return codes

def headers(username, password):
    import base64
    credential = f'{username}: {password}'
    token = base64.b64encode(credential.encode())
    code = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return code

