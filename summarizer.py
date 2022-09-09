import streamlit as st 
import nltk
import string
import heapq

stopwords = nltk.corpus.stopwords.words('english')
def Preprocess(text):
  formatted_text = text.lower()
  tokens = []
  for token in nltk.word_tokenize(formatted_text):
    tokens.append(token)
  
  # delete stop words
  tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]
  #cancatinate all tokens together 
  formatted_text= ' '.join(element for element in tokens)

  return formatted_text






def main():
    st.title("Simple Summeraization...  ")
    st.subheader("write your sentences....")
    text=st.text_area("")
    st.subheader("please select your summarizer")
    summarizers_option = st.selectbox("" , ("Frequently_Based", "Cosin Similarity"))
    if st.button("Summarize"):
        if summarizers_option == "Frequently_Based":
            st.text("Using frequently")

            #preprocessing 
            formatted_text = Preprocess(text)
            
            #caculate word frequency
            summary_result = nltk.FreqDist(nltk.word_tokenize(formatted_text))
            highest_values = max(summary_result.values())

            for word in summary_result.keys():
                summary_result[word] = (summary_result[word] / highest_values)
            text = nltk.sent_tokenize(text)
            # ----------------------------------------------------------------------------
            # score sentences + sentences
            score_sentences = {}
            for sent in text:
              for word in nltk.word_tokenize(sent.lower()):
                if sent not in score_sentences.keys():
                  score_sentences[sent] = summary_result[word]
                else:
                  score_sentences[sent] += summary_result[word]


            best_sentences =  heapq.nlargest(2, score_sentences, key=score_sentences.get)
            summary = ' '.join(best_sentences)
                




        else:
            summary_result = Preprocess(text)

        st.success(summary)




if __name__== '__main__':


    #summerization __ Frequently_ based_ algorithm 
    main()