import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
from fileMethod import filemethod
from createFiles import createfiles
# from resetPath import resetpath
answerPath = r"C:\Users\eyash\Projects\Programming\MumbleBot\MumbleBot\Recording\txtfiles\pathA.txt"
reasoningPath = r"C:\Users\eyash\Projects\Programming\MumbleBot\MumbleBot\Recording\txtfiles\pathR.txt"

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY")
)

r = "C:\\Users\\eyash\\Projects\\Programming\\MumbleBot\\MumbleBot\\Recording\\Speech.txt"
with open(r, encoding='utf-8') as f:
    g = f.read()

completion = client.chat.completions.create(
  model="nvidia/nemotron-3-ultra-550b-a55b",
  messages=[{"role":"user","content":"what is the capital of france"}],
  top_p=0.95,
  max_tokens=16384,
  extra_body={"chat_template_kwargs":{"enable_thinking":True},"reasoning_budget":16384},
  stream=False
)
reasoning = getattr(completion.choices[0].message, "reasoning_content", None)
answer = completion.choices[0].message.content
createfiles(reasoning, reasoningPath)
createfiles(answer, answerPath)
