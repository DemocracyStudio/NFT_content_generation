# Controllable text generation for the marketing content of NFTs
This repository contains all the information, code and datasets of the "Controllable text generation for the marketing content of NFTs" transformers' model started as a group project at the Machine Learning degree of [opencampus.sh](https://opencampus.sh).

You can either clone this repository and run the app.py file locally, or directly use the app in your browser from the [dedicated huggingface space](https://huggingface.co/spaces/DemocracyStudio/generate_nft_content/). First release is June 15th, 2022, further improvements are expected to come.

### Project Description:
While text generation (or natural language generation) refer to computer-generated texts of human-written quality, controllable text generation aims to constrain the generated text by incorporating some pre-specified keywords as manual input. 

Since the value of NFTs highly relies on their community engagement, and the capacity to partnering with influencers, marketizing NFTs demands a high production capacity of easily customizable turnkey articles, which gives lots of sense to computer-generated marketing content. 

The pitch deck of the project is available [here](https://docs.google.com/presentation/d/1G58GxLDBLTdoXnAwbt_2afVEsp8g25vSVbgN1FHDUmM/edit?usp=sharing). 

### Datasets:
[Medium.com](https://medium.com/) is undoubtably a major media platform for content marketing. I've been using selenium to collect about 4000 human-written texts answering to the queries #Nft, #Nftart, #Nftartist, #Nft Collectibles, #Nft Marketplace, and #opensea. The resulting cleaned dataset is available in the dataset folder. It has been cleaned of urls, digits, and filtered out negative or neutral sentiments. So as we're sure the model will only generate enthusiastic content about NFTs. 

### Literature:
2021
- [Exploring Transformers in Natural Language Generation: GPT, BERT, and XLNet](https://paperswithcode.com/paper/exploring-transformers-in-natural-language)
- [Parallel Refinements for Lexically Constrained Text Generation with BART](https://paperswithcode.com/paper/parallel-refinements-for-lexically)
- [BARTSCORE: Evaluating Generated Text as Text Generation](https://paperswithcode.com/paper/bartscore-evaluating-generated-text-as-text)
- [Neural Rule-Execution Tracking Machine For Transformer-Based Text Generation](https://paperswithcode.com/paper/neural-rule-execution-tracking-machine-for)

2020
- [The survey: Text generation models in deep learning](https://www.researchgate.net/publication/340622598_The_Survey_Text_Generation_Models_in_Deep_Learning)
- [Modern methods for text generation](https://paperswithcode.com/paper/modern-methods-for-text-generation)
- [PAIR: Planning and Iterative Refinement in Pre-trained Transformers for Long Text Generation](https://paperswithcode.com/paper/pair-planning-and-iterative-refinement-in-pre)

A video recording of the literature review is available [here](https://youtu.be/ffOX3D_dMYY).
