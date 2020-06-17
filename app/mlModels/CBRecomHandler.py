import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class cbrec():
    def __init__(self):
        self.ds = pd.read_csv("https://raw.githubusercontent.com/MidoriRobin/grocery-assistant/master/data/supermarketdb_table_items-2.csv")

        self.tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        self.tfidf_matrix = self.tf.fit_transform(self.ds['desc_item'])

        self.cosine_similarities = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        self.results = {}
        for idx, row in self.ds.iterrows():
          self.similar_indices = self.cosine_similarities[idx].argsort()[:-100:-1]
          self.similar_items = [(self.cosine_similarities[idx][i], self.ds['item_id'][i]) for i in self.similar_indices]
          self.results[row['item_id']] = self.similar_items[1:]

    def item(self, id):
      return self.ds.loc[self.ds['item_id'] == id]['desc_item'].tolist()[0].split(' - ')[0] # Just reads the results out of the dictionary.

    def recommend(self, item_id, num):
        print("Recommending " + str(num) + " products similar to " + self.item(item_id) + "...")
        print("-------")
        recs = self.results[item_id][:num]
        for rec in recs:
          print("Recommended: Item_ID = " + str(rec[1]) + " (score:" + str(rec[0]) + ")")
