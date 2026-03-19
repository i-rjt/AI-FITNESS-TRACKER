import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM3-3B")


messages=[{"role":"user","content":"What is the best powerlifting ?"}]

print(pipe(messages))
