import openai

# with open('hidden.txt') as file:
    
openai.api_key = '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'

def get_api_response(messages: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequesncy_penalty=0,
            presence_penalty=0,
            stop=['user:', 'assistant:']
        )

        print(response)
    except Exception as e:
        print('ERROR:', e)

messages=[
    {
      "role": "user",
      "content": "Tell the world about the ChatGPT API in the style of a pirate in one sentence."
    },
    {
      "role": "assistant",
      "content": "Arr, mateys! Allow me to regale ye with this wonderous tale of the ChatGPT API, a mighty tool that lets ye parley with a vessel of language, transforming yer words into a treasure trove of responses and knowledge!"
    }
  ]

get_api_response(messages)