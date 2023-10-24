import openai

with open('hidden.txt') as file:
    openai.api_key = file.read()

def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequesncy_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )

        print(response)
    except Exception as e:
        print('ERROR:', e)

prompt = 'Hello! How can I assist you today?'
get_api_response()