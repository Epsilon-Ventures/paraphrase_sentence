import os
import openai
from dotenv import load_dotenv


def paraphrase_sentece(sentence_list):
  """
  Returns a list of paraphrased sentences
  @param sentence_list: list of sentences to paraphrase
  """
  load_dotenv()  
  openai.api_key = os.getenv("OPENAI_API_KEY")

  for sentence in sentence_list:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Paraphrase the sentence: {sentence}",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

  print(response.choices[0].text.strip())

paraphrase_sentece(['This is a test sentence'])