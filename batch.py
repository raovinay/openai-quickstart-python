import os

import openai
from dotenv import load_dotenv


def generate_prompt(prompt):
  return """Generate transliteration for the following text.
            Text: {}
            Transliteration:
          """.format(prompt.capitalize()
  )

if __name__ == '__main__':
  load_dotenv()
  openai.api_key = os.getenv("OPENAI_API_KEY")
  # read file loop
  with open('hindi.txt') as f:
    df = open('hindi_transliterated.txt','w')
    lines = []
    for line in f:
      lines.append(generate_prompt(line))

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=lines[:20],
      temperature=0.6,
    )

    for choice in response.choices:
      df.write(choice.text.strip())
      df.write('\n')
    df.close()
