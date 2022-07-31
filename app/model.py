from transformers import AutoModelForCausalLM, AutoTokenizer
from os import getcwd
from pathlib import Path
import torch

class Generator:
    def __init__(self) -> None:
        pretrained = Path(getcwd()+"/model/")
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained)
        self.tokenizer.do_lower_case = True
        self.model = AutoModelForCausalLM.from_pretrained(pretrained)
    
    def generate(self, input_text: str, max_length: int=100)->str:
        token_ids = self.tokenizer.encode(
            input_text, add_special_tokens=False, return_tensors="pt")

        with torch.no_grad():
            output_ids = self.model.generate(
                token_ids.to(self.model.device),
                max_length=max_length,
                do_sample=True,
                top_k=500,
                top_p=0.95,
                pad_token_id=self.tokenizer.pad_token_id,
                bos_token_id=self.tokenizer.bos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                bad_word_ids=[[self.tokenizer.unk_token_id]]
            )
        return self.tokenizer.decode(output_ids.tolist()[0])

generater = Generator()


if __name__ == "__main__":
    generater = Generator()
    print(generater.generate("おはよう、お兄ちゃん。"))