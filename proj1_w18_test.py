import unittest
import proj1_w18 as proj1
import json
import requests

def request_form_API():
    base_people_url = 'https://itunes.apple.com/search?parameterkeyvalue'
    json_string = requests.get(base_people_url).text
    results_list = json.loads(json_string)

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
    m3 = proj1.Song("Hey Jude", "The Beatles", "1968", "Rock", 180)
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
        self.assertEqual(self.m4.title, "TheBeatles 1967-1970 (The Blue Album)")        

    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year) [No genre]")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year) [No genre]")
        self.assertEqual(self.m3.__str__(), "Hey Jude by The Beatles (1968) [Rock]")
        self.assertEqual(self.m4.__str__(), "TheBeatles 1967-1970 (The Blue Album) by The Beatles (1968-08-26T07:00:00Z) [Rock]")

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
        self.assertEqual(self.m4.title, "Steven Spielberg 7-Movie Director’s Collection")

    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year) [No rating]")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year) [No rating]")
        self.assertEqual(self.m3.__str__(), "Jaws by Steven Speilberg (1975) [PG]")
        self.assertEqual(self.m4.__str__(), "Steven Spielberg 7-Movie Director’s Collection by Steven Spielberg (1975-06-20T07:00:00Z) [PG]")

    def testLen(self):
        self.assertEqual(self.m1.__len__(), 0)
        self.assertEqual(self.m2.__len__(), 0)
        self.assertEqual(self.m3.__len__(), 120)
        self.assertEqual(self.m4.__len__(), 7451455)


if __name__ == "__main__":
    unittest.main()
