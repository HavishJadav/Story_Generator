from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class StoryGenerator:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def generate(self, prompt, max_length=150, temperature=0.9, top_k=50, top_p=0.95):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
