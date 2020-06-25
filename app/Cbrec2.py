import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class cbrec2():
    
    def __init__(self):
        self.metadata = pd.read_csv("https://raw.githubusercontent.com/MidoriRobin/grocery-assistant/master/data/supermarketdb_table_items-2.csv")

        #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        self.tfidf = TfidfVectorizer(stop_words='english')

        #Replace NaN with an empty string
        self.metadata['desc_item'] = self.metadata['desc_item'].fillna('')

        #Construct the required TF-IDF matrix by fitting and transforming the data
        self.tfidf_matrix = self.tfidf.fit_transform(self.metadata['desc_item'])

        # Compute the cosine similarity matrix
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

        #Construct a reverse map of indices and item descriptions
        self.indices = pd.Series(self.metadata.index, index=self.metadata['desc_item']).drop_duplicates()

    # Function that takes in item description as input and outputs most similar items
    def get_recommendations(self, item_id):
        # Get the index of the item match
        self.idx = self.indices[item_id]

        # Get the pairwsie similarity scores of all items with that item
        self.sim_scores = list(enumerate(self.cosine_sim[self.idx]))

        # Sort the items based on the similarity scores
        self.sim_scores = sorted(self.sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar items
        self.sim_scores = self.sim_scores[1:11]

        # Get the item indices
        self.item_indices = [i[0] for i in self.sim_scores]

        # Return the top 10 most similar items
        return self.metadata['desc_item'].iloc[self.item_indices]