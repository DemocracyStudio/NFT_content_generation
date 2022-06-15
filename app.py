import streamlit as st
from transformers import pipeline, GPT2LMHeadModel, AutoTokenizer#, SummarizationPipeline, AutoModelWithLMHead

generate = pipeline(task='text-generation', model=GPT2LMHeadModel.from_pretrained("DemocracyStudio/generate_nft_content"), tokenizer=AutoTokenizer.from_pretrained("DemocracyStudio/generate_nft_content"))
#summarize = SummarizationPipeline(model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_small_program_synthese_transfer_learning_finetune"),tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_small_program_synthese_transfer_learning_finetune", skip_special_tokens=True),device=0)

st.title("Text generation for the marketing content of NFTs")
    
st.sidebar.image("bayc crown.png", use_column_width=True)
st.sidebar.write("image credits: bayc")
topics=["NFT", "Blockchain", "Metaverse"]
choice = st.sidebar.selectbox("Select one topic", topics)
st.sidebar.write("Course project 'NLP with transformers' at opencampus.sh, Spring 2022")
    
if choice == 'NFT':
    manual_input = st.text_area("Manual input: (optional)")
    #num_sequences = st.text_area("Number of sequences: (default: 1)")

    if st.button("Generate"):
        #st.text("Keywords: {}\n".format(keywords))
        #st.text("Length in number of words: {}\n".format(length))
        generated = generate(manual_input, max_length = 512, num_return_sequences=1)
        st.write(generated)
        #tweet = summarize(generated)
        #st.write(tweet)
else:
    st.write("Topic not available yet") 
