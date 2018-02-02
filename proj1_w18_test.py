import unittest
import proj1_w18 as proj1
import json
import requests
import webbrowser


####################################################################
####################### part 1 and part 2 ##########################
####################################################################

def load_json():
    with open('sample_json.json') as json_data:
        json_dict = json.load(json_data)
        return json_dict

json_dict = load_json()

class TestMedia(unittest.TestCase):
    m1 = proj1.Media()
    m2 = proj1.Media("1999", "Prince")
    m3 = proj1.Media("Bridget Jones's Diary (Unabridged)", "Helen Fielding", "2012")
    m4 = proj1.Media(json=json_dict[2])
    def testConstructor(self):
        self.assertEqual(self.m1.title, "No Title")
        self.assertEqual(self.m1.author, "No Author")
        self.assertEqual(self.m1.release_year, "No year")  
        self.assertEqual(self.m2.title, "1999")
        self.assertEqual(self.m2.author, "Prince")
        self.assertEqual(self.m2.release_year, "No year")
        self.assertEqual(self.m3.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(self.m3.author, "Helen Fielding")
        self.assertEqual(self.m3.release_year, "2012")     
        self.assertEqual(self.m4.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(self.m4.author, "Helen Fielding")
        self.assertEqual(self.m4.release_year, "2012-04-03T07:00:00Z")    
    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year)")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year)")
        self.assertEqual(self.m3.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(self.m4.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012-04-03T07:00:00Z)")

    def testLen(self):
        self.assertEqual(self.m1.__len__(), 0)
        self.assertEqual(self.m2.__len__(), 0)
        self.assertEqual(self.m3.__len__(), 0)
        self.assertEqual(self.m4.__len__(), 0)


class TestSong(unittest.TestCase):
    m1 = proj1.Song()
    m2 = proj1.Song("1999", "Prince")
    m3 = proj1.Song("Hey Jude", "The Beatles", "1968", "TheBeatles 1967-1970 (The Blue Album)", "Rock", 180)
    m4 = proj1.Song(json=json_dict[1])

    def testConstructor(self):
        self.assertEqual(self.m1.title, "No Title")
        self.assertEqual(self.m1.author, "No Author")
        self.assertEqual(self.m1.release_year, "No year") 
        self.assertEqual(self.m1.genre, "No genre")
        self.assertEqual(self.m1.track_length, 0)
        self.assertEqual(self.m2.title, "1999")
        self.assertEqual(self.m2.author, "Prince")
        self.assertEqual(self.m2.release_year, "No year")
        self.assertEqual(self.m2.genre, "No genre")
        self.assertEqual(self.m3.title, "Hey Jude")
        self.assertEqual(self.m3.author, "The Beatles")
        self.assertEqual(self.m3.release_year, "1968")
        self.assertEqual(self.m3.genre, "Rock")
        self.assertEqual(self.m4.title, "Hey Jude")        

    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year) [No genre]")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year) [No genre]")
        self.assertEqual(self.m3.__str__(), "Hey Jude by The Beatles (1968) [Rock]")
        self.assertEqual(self.m4.__str__(), "Hey Jude by The Beatles (1968-08-26T07:00:00Z) [Rock]")

    def testLen(self):
        self.assertEqual(self.m1.__len__(), 0)
        self.assertEqual(self.m2.__len__(), 0)
        self.assertEqual(self.m3.__len__(), 180)
        self.assertEqual(self.m4.__len__(), 431333)

class TestMovie(unittest.TestCase):
    m1 = proj1.Movie()
    m2 = proj1.Movie("1999", "Prince")
    m3 = proj1.Movie("Jaws", "Steven Speilberg", "1975", "PG", 120)
    m4 = proj1.Movie(json=json_dict[0])

    def testConstructor(self):
        self.assertEqual(self.m1.title, "No Title")
        self.assertEqual(self.m1.author, "No Author")
        self.assertEqual(self.m1.release_year, "No year") 
        self.assertEqual(self.m1.rating, "No rating")
        self.assertEqual(self.m2.title, "1999")
        self.assertEqual(self.m2.author, "Prince")
        self.assertEqual(self.m2.release_year, "No year")
        self.assertEqual(self.m2.rating, "No rating")
        self.assertEqual(self.m3.title, "Jaws")
        self.assertEqual(self.m3.author, "Steven Speilberg")
        self.assertEqual(self.m3.release_year, "1975")
        self.assertEqual(self.m3.rating, "PG")
        self.assertEqual(self.m4.title, "Jaws")

    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year) [No rating]")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year) [No rating]")
        self.assertEqual(self.m3.__str__(), "Jaws by Steven Speilberg (1975) [PG]")
        self.assertEqual(self.m4.__str__(), "Jaws by Steven Spielberg (1975-06-20T07:00:00Z) [PG]")

    def testLen(self):
        self.assertEqual(self.m1.__len__(), 0)
        self.assertEqual(self.m2.__len__(), 0)
        self.assertEqual(self.m3.__len__(), 120)
        self.assertEqual(self.m4.__len__(), 7451455)

####################################################################
############################ part 3 ################################
####################################################################

def request_form_API(words, limit):
    # base_people_url = 'https://itunes.apple.com/search?term=jack+johnson&limit=25'
    base_people_url = 'https://itunes.apple.com/search?term=' + words + '&limit=' + str(limit) 
    json_string = requests.get(base_people_url)
    return json_string.json()['results']

def get_list_of_json():
    jsons = []
    json_1 = request_form_API("baby", 5)
    json_2 = request_form_API("love", 5)
    json_3 = request_form_API("moana", 5)
    json_4 = request_form_API("helter skelter", 5)
    json_5 = request_form_API("&@#!$", 5)
    json_6 = request_form_API("", 5)
    jsons.append(json_1)
    jsons.append(json_2)
    jsons.append(json_3)
    jsons.append(json_4)
    jsons.append(json_5)
    jsons.append(json_6)
    return jsons

class TestJson(unittest.TestCase):
    jsons = get_list_of_json()
    def testConstructor(self):
        for json in self.jsons:
            # Test if number of results is within range
            self.assertEqual(len(json) <= 5, True)
            # initialize objects form json retrieved from itunes store
            if json != None:
                for info in json:
                    m = proj1.Media()
                    if 'kind' in info:
                        if info['kind'] == "song":
                            m = proj1.Song(json=info)
                        elif info['kind'] == "feature-movie":
                            m = proj1.Movie(json=info)
                    else:
                        m = proj1.Media(json=info)


####################################################################
############################# part 4 ###############################
####################################################################

def main():
    # ask user for input
    limit = 100
    keyword = input('\n' + "Entere a serach term, or 'exit' to quit: ")
    index = {}
    json_index = {}
    count = 1
    while True:
        if keyword.isdigit():
            if count == 1 or int(keyword) >= count:
                keyword = input('\n' + "Entere a number for more info, or another search term, or exit: ")
            else:
                term = index[keyword]
                print ("Launching...")
                if term['wrapperType'] == "audiobook":
                    webbrowser.open(term['collectionViewUrl']) 
                else:
                    webbrowser.open(term['trackViewUrl']) 
                keyword = input('\n' + "Entere a number for more info, or another search term, or exit: ") 
        elif keyword == "exit":
            print('\n' + "Bye !")
            break
        else:
            index = {}
            json = request_form_API(keyword, limit)
            if json == None:
                print('\n' + "Sorry, we didn't found anything that matches...")
                keyword = input('\n' + "Entere a serach term, or 'exit' to quit: ")
            else:
                return_list = {"SONGS": [], "MOVIES": [], "OTHER MEDIA": []}
                m = proj1.Media()
                for info in json:
                    if 'kind' in info:
                        if info['kind'] == "song":
                            m = proj1.Song(json=info)
                            return_list["SONGS"].append(m)
                        elif info['kind'] == "feature-movie":
                            m = proj1.Movie(json=info)
                            return_list["MOVIES"].append(m)
                    else:
                        m = proj1.Media(json=info)
                        return_list["OTHER MEDIA"].append(m)
                    json_index[m] = info
                count = 1
                print('\n' + "SONGS: ")
                for key in return_list["SONGS"]:
                    print(str(count) + '. ' + key.__str__())
                    index[str(count)] = json_index[key]
                    count += 1
                print('\n' + "MOVIES: ")
                for key in return_list["MOVIES"]:
                    print(str(count) + '. ' +  key.__str__())
                    index[str(count)] = json_index[key]
                    count += 1
                print('\n' + "OTHER MEDIA: ")
                for key in return_list["OTHER MEDIA"]:
                    print(str(count) + '. ' +  key.__str__())
                    index[str(count)] = json_index[key]
                    count += 1
                keyword = input('\n' + "Entere a number for more info, or another search term, or exit: ")        



if __name__ == "__main__":
    main()
    unittest.main()
