import os, openai
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_chat_response(prompt):
    try:
        res = openai.ChatCompletion.create(
            model='gpt-4o-mini',
            messages=[{'role':'user','content':prompt}],
            max_tokens=300
        )
        return res.choices[0].message['content'].strip()
    except Exception as e:
        return f'OpenAI error: {e}'
