import os
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_image(prompt):
    try:
        res = openai.Image.create(prompt=prompt, n=1, size='1024x1024')
        return res['data'][0]['url']
    except Exception as e:
        print('Image gen error:', e)
        return None
