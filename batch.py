import os

import openai
from dotenv import load_dotenv


def generate_prompt(prompt):
  return """Generate transliteration for the following text.
            Text: {}
          """.format(prompt.capitalize()
  )

if __name__ == '__main__':
  load_dotenv()
  openai.api_key = os.getenv("OPENAI_API_KEY")
  # read file loop
  with open('hindi.txt') as f:
    df = open('hindi_transliterated.txt','w')
    for line in f:
      print(line)
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(line),
        temperature=0.6,
      )
      print(response.choices[0].text)
      df.write(response.choices[0].text)
      df.write('\n')
    df.close()
