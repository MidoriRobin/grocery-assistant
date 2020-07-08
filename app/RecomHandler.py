import csv
import bz2
import pickle
import _pickle as cPickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from app.mlModels.CBRecomHandler import cbrec



# class cbrec():
#     def __init__(self):
#         self.ds = pd.read_csv("https://raw.githubusercontent.com/MidoriRobin/grocery-assistant/master/data/supermarketdb_table_items-2.csv")
#
#         self.tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
#         self.tfidf_matrix = self.tf.fit_transform(self.ds['desc_item'])
#
#         self.cosine_similarities = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
#         self.results = {}
#         for idx, row in self.ds.iterrows():
#           self.similar_indices = self.cosine_similarities[idx].argsort()[:-100:-1]
#           self.similar_items = [(self.cosine_similarities[idx][i], self.ds['item_id'][i]) for i in self.similar_indices]
#           self.results[row['item_id']] = self.similar_items[1:]
#
#     def item(self, id):
#       return self.ds.loc[self.ds['item_id'] == id]['desc_item'].tolist()[0].split(' - ')[0] # Just reads the results out of the dictionary.
#
#     def recommend(self, item_id, num):
#         print("Recommending " + str(num) + " products similar to " + self.item(item_id) + "...")
#         print("-------")
#         recs = self.results[item_id][:num]
#         for rec in recs:
#           print("Recommended: Item_ID = " + str(rec[1]) + " (score:" + str(rec[0]) + ")")


class RecomHandler():
    """docstring for recomHandler."""

    @staticmethod
    def recomHelper():
        """
        Converts the csv of predicted recommendations into a dictionary form.

        This function reconstructs the table with column headings as Keys ("uid", "pid", "rating")
        and the values under each column belong to an array of values that each correspond to
        the value of each key values being arrays that contain a list of values.
        """
        print("Activating recomHelper..")
        recomDict = {}
        uid = []
        pid = []
        rating = []

        with open('./data/predRatings.csv', newline='') as csvfile:
          reader = csv.DictReader(csvfile)
          for row in reader:
            uid.append(row['acc_num'])
            pid.append(row['item_id'])
            rating.append(row['p_rating'])

        recomDict["uid"] = uid
        recomDict["pid"] = pid
        recomDict["rating"] = rating

        return recomDict

    @staticmethod
    def rec_by_usr(userid, recDict):
        """
        Accepts a user's id  and a dictionary as parameters and fetches
        the list of products of which various ratings have been generated.
        """

        print(recDict)
        print("Generating recommendations for specified user")

        if userid in set(recDict['uid']):
            sIndex = recDict['uid'].index(userid)
            print(sIndex)
            numOfRecc = recDict['uid'].count(userid)
            print(numOfRecc)
        else:
          #Might need an exception here
          return ("No Recommendations have been made for that user")

        ratings = recDict['rating'][sIndex:(sIndex+numOfRecc)]
        print(ratings)
        products = recDict['pid'][sIndex:(sIndex+numOfRecc)]
        print(products)

        print("Outputting..")
        return ratings, products

    @staticmethod
    def diet_cnvrtr(pref=None, typecode=None):
        """
        Converts a newly added user's preference into a list of food types.
        """

        p_List = {
        'Vegetarian' : ["VITAMINS"],
        'High Carb' : ["CHEESE",],
        'Low Carb' : ["COOKIES","Canned Products"],
        'High Protien' : ["Seafood", "FROZEN MEAT", "EGGS"],
        'Meat Lover' : ["Seafood", "Meat", "SOUP"],
        'Pescatarian' : ["Seafood", "Cereal", "FRZN FRUITS"],
        }

        if typecode:
            pref = list(p_List.values())[typecode]
            print(pref)
            return pref
        elif pref not in p_List:
            return "Invalid, selection"
        else:
            return p_List[pref]

    @staticmethod
    def collab_fltr(userid,itemid):

        filepath = './app/mlModels/Fin-Model.sav'
        loadedModel = pickle.load(open(filepath, 'rb'))

        result = loadedModel.predict(userid,itemid)

        return result

    @staticmethod
    def cont_fltr():
        filepath = './app/mlModels/CB - Model.sav'
        loadedModel = pickle.load(open(filepath, 'rb'))

        # result = loadedModel.predict(userid,itemid)
        return loadedModel[0][0]

    @staticmethod
    def cont_bsd_fltr(itemid, num=5):

        def decompress_pickle(file):
            data = bz2.BZ2File(file, 'rb')
            data = cPickle.load(data)
            return data

        data = decompress_pickle('./app/mlModels/Cbfilter_comp.pbz2')

        result = data.recommend(itemid, num)

        return result


    # Example of use
    # result = data.recommend(item_id = 25671, num=10)
    # print(result)
