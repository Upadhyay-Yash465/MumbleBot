from openai import OpenAI
from fileMethod import filemethod
from createFiles import createfiles
from resetFiles import resetfiles

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

r = "C:\\Users\\eyash\\Projects\\Programming\\MumbleBot\\MumbleBot\\Recording\\Speech.txt"
with open(r, encoding='utf-8') as f:
    g = f.read()

completion = client.chat.completions.create(
  model="nvidia/nemotron-3-ultra-550b-a55b",
  messages=[{"role":"user","content":"what is the capitol of france"}],
  top_p=0.95,
  max_tokens=16384,
  extra_body={"chat_template_kwargs":{"enable_thinking":True},"reasoning_budget":16384},
  stream=True
)

for chunk in completion:
  if not chunk.choices:
    continue
  reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
  if reasoning:
    print(reasoning, end="")
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")