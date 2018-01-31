import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):
    m1 = proj1.Media()
    m2 = proj1.Media("1999", "Prince")
    m3 = proj1.Media("Bridget Jones's Diary (Unabridged)", "Helen Fielding", "2012")
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
    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year)")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year)")
        self.assertEqual(self.m3.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")

    def testLen(self):
        self.assertEqual(self.m1.__len__(), 0)
        self.assertEqual(self.m2.__len__(), 0)
        self.assertEqual(self.m3.__len__(), 0)


class TestSong(unittest.TestCase):
    m1 = proj1.Song()
    m2 = proj1.Song("1999", "Prince")
    m3 = proj1.Song("Hey Jude", "The Beatles", "1968", "Rock", 180)
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

    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year) [No genre]")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year) [No genre]")
        self.assertEqual(self.m3.__str__(), "Hey Jude by The Beatles (1968) [Rock]")

    def testLen(self):
        self.assertEqual(self.m1.__len__(), 0)
        self.assertEqual(self.m2.__len__(), 0)
        self.assertEqual(self.m3.__len__(), 180)

class TestMovie(unittest.TestCase):
    m1 = proj1.Movie()
    m2 = proj1.Movie("1999", "Prince")
    m3 = proj1.Movie("Jaws", "Steven Speilberg", "1975", "PG", 120)
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

    
    def testStr(self):
        self.assertEqual(self.m1.__str__(), "No Title by No Author (No year) [No rating]")
        self.assertEqual(self.m2.__str__(), "1999 by Prince (No year) [No rating]")
        self.assertEqual(self.m3.__str__(), "Jaws by Steven Speilberg (1975) [PG]")

    def testLen(self):
        self.assertEqual(self.m1.__len__(), 0)
        self.assertEqual(self.m2.__len__(), 0)
        self.assertEqual(self.m3.__len__(), 120)

unittest.main()
