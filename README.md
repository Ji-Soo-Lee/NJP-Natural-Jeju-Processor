# Solving Korea Dialect Translation Problem Under Data Scarcity

This repository contains Jupyter notebooks that implement various machine learning models using resources from Hugging Face. Below you'll find the description and references for each file.

## Repository Contents

### T5_jeju.ipynb

This Jupyter notebook utilizes the `ke-t5-small` model from KETI-AIR, specifically designed for processing and generating Korean text. For more details on this model, you can visit the Hugging Face model page.

**Reference:** [KETI-AIR/ke-t5-small - Hugging Face](https://huggingface.co/KETI-AIR/ke-t5-small) | [Base Code](https://metamath1.github.io/blog/posts/gentle-t5-trans/gentle_t5_trans.html)

### RLHF_BertRM.ipynb

This notebook demonstrates reinforcement learning from human feedback (RLHF) using the `PPO Trainer` on the Roberta model. This is an advanced technique used to fine-tune language models based on specific human preferences or corrections.

**Reference:** [PPO Trainer — Hugging Face](https://huggingface.co/docs/trl/ppo_trainer)
