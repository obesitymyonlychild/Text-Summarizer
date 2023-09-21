import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_metric, load_from_disk



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
    
    #the main function needed: in textSummaizer.ipynb: tokenize 
    def convert_examples_to_features(self, example_batch)-> bool:
        #could add the max_length to self.config? 
        #padding is set to default False
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    #save the encoded data to file samsum_dataset
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_encoded = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum_encoded.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset'))
