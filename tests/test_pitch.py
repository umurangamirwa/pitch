from app.models import Comment, User,Pitch
from app import db
import unittest

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'Jane', password = 'banana', email = 'janedoe@demo.com')
        self.new_pitch = Pitch(id = 123, pitch_title = 'Pitch', pitch_content = 'Pitch content',category = 'pickup',likes = 0, dislikes = 0)

    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()
        Comment.query.delete()

    def test_check_instance(self):
        self.assertEquals(self.new_pitch.pitch_title,'Pitch')
        self.assertEquals(self.new_pitch.pitch_content,'Pitch content')
        self.assertEquals(self.new_pitch.category,"pickup")

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        pitch = Pitch.get_pitch(123)
        self.assertTrue(pitch is not None)
