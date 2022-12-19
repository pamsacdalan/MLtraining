import openai
import os

OPENAI_API_KEY = 'OPEN_API_KEY'


def main():
    open_ai_api_key = os.getenv(OPEN_API_KEY)
    if open_ai_api_key == None:
        print('OPEN_API_KEY required')
        exit(-1)
    
    print("Pychat v0.1")
    query = input('Input: ')
    
    completion = openai.Completion.create(engine='text-davinci-003', prompt=query, max_tokens=4000)
    
    output = completion.choices[0].text
    print("Output: {}".format(output))    
    
if __name__ == '__main__':
    main()