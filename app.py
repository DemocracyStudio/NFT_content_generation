import streamlit as st
import joblib,os
PAGE_CONFIG = {"page_title":"StColab.io",
               "page_icon":":smiley:",
               "layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)

def main():
  st.title("Text generation for the marketing content of NFTs")
  st.subheader("Course project 'NLP with transformers' at opencampus.sh, Spring 2022")
    
  st.sidebar.image("bayc crown.png", use_column_width=True)
  topics=["NFT", "Blockchain", "Metaverse"]
  choice = st.sidebar.selectbox("Select one topic", topics)
    
  if choice == 'NFT':
    st.info("Generate blog article for NFTs")
    keywords=st.text_area("Input 4 keywords here: (optional)")
    length=st.text_area("How long should be your text? (default: 512 words)")
    
    if st.button("Generate"):
      prompt = "<|startoftext|>"
      generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)
      generated = generated.to(device)
      sample_outputs = model.generate(
          generated,
          do_sample=True,
          top_k=50,
          max_length = 512,
          top_p=0.95,
          num_return_sequences=1
          )
      for i, sample_output in enumerate(sample_outputs):
        generated_text = tokenizer.decode(sample_output, skip_special_tokens=True)
      st.text("Keywords: {}\n".format(keywords))
      st.text("Length in number of words: {}\n".format(length))
      st.text("This is your tailored blog article" {generated_text})
      summary = summarize(generated_text, num_sentences=1)
      st.text("This is a tweet-sized summary of your article" {summary})

  else:
    st.write("Topic not available yet")
    
if __name__ == '__main__':
    main()
