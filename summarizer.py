import streamlit as st 
import nltk
import string
import heapq
from hazm import * 
#nltk.download('stopwords')
#nltk.download('punkt')
stopwords = nltk.corpus.stopwords.words('english')
# preprocessing for english text
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

# preprocessing for Persian text
def Persian_preprocessing(text):
    tokens = word_tokenize(text)
    tokens = [puc for puc in tokens if puc not in string.punctuation]
    stop_words = stopwords_list()
    final = [stop for stop in tokens if stop not in stop_words]
    final = ' '.join(final)
    return final


def main():
    st.subheader("please select your language")
    language = st.selectbox("" , ("english", "persian"))
    st.title("Simple Summeraization...  ")
    st.subheader("write your sentences....")
    text=st.text_area("")
    st.subheader("please select your summarizer")
    summarizers_option = st.selectbox("" , ("Frequently_Based", "Cosin Similarity"))
    if st.button("Summarize"):
        if summarizers_option == "Frequently_Based" and language == 'english':
            st.text("Using frequently")

            #preprocessing 
            formatted_text = Preprocess(text)
            
            #caculate word frequency
            summary_result = nltk.FreqDist(nltk.word_tokenize(formatted_text))
            highest_values = max(summary_result.values())

            for word in summary_result.keys():
                summary_result[word] = (summary_result[word] / highest_values)
            text = nltk.sent_tokenize(text)

            score_sentences = {}
            for sent in text:
              for word in nltk.word_tokenize(sent.lower()):
                if sent not in score_sentences.keys():
                  score_sentences[sent] = summary_result[word]
                else:
                  score_sentences[sent] += summary_result[word]
        else:
            summarizers_option == "Frequently_Based" and language == 'persian'
            #preprocessing 
            formatted_text = Persian_preprocessing(text)
            
            #caculate word frequency
            freq = nltk.FreqDist(formatted_text)
            highest_values = max(freq.values())

            for word in freq.keys():
                freq[word] = (freq[word] / highest_values)
            text = nltk.sent_tokenize(text)
            # ----------------------------------------------------------------------------
            # score sentences + sentences
            score_sentences = {}
            for sent in text:
                
                for word in  word_tokenize(sent):
                        if sent not in score_sentences.keys():
                            score_sentences[sent] = freq[word]
                else:
                      score_sentences[sent] += freq[word]


        best_sentences =  heapq.nlargest(2, score_sentences, key=score_sentences.get)
        summary = ' '.join(best_sentences)
                
        st.success(summary)             

if __name__== '__main__':

  main()