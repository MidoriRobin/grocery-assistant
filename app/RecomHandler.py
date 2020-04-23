import csv

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

        with open('./predRatings.csv', newline='') as csvfile:
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
        print("Generating recommendations for specified user")

        if userid in set(recDict['uid']):
          sIndex = recDict['uid'].index(userid)
          numOfRecc = recDict['uid'].count(userid)
        else:
          #Might need an exception here
          return ("No Recommendations have been made for that user")

        ratings = recDict['rating'][sIndex:numOfRecc]
        products = recDict['pid'][sIndex:numOfRecc]

        print("Outputting..")
        return ratings, products

    @staticmethod
    def diet_cnvrtr(pref):
        """
        Converts a newly added user's preference into a list of food types.
        """
        p_List = {
        'Vegetarian' : ["Cereal"],
        'High Carb' : ["Dairy",],
        'Low Carb' : ["Seafood","Canned Products"],
        'High Protien' : ["Seafood", "Meat", "Dairy"],
        'Meat Lover' : ["Seafood", "Meat"],
        'Pescatarian' : ["Seafood", "Cereal"],
        }

        if pref not in p_List:
            return "Invalid, selection"
        else:
            return p_List[pref]
