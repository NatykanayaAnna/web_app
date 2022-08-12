import os
import unittest
import tempfile
from app import app
from models.banners import db


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.init_app(app)


    def test_add_form(self):
        response = self.app.get('/add')
        # assert b'<p><input id="banners_name" maxlength="50 minlength="2" name="banners_name" required type="text" value=""> Name</p>' in response.data
        assert b'<p><input id="status" name="status" type="checkbox" value="y"> Status</p>' in response.data
        assert b'<p><input id="image" name="image" type="file">Image</p>' in response.data
        assert b'<p> <input id="url" minlength="9" name="url" required type="text" value=""> URL</p>' in response.data
        assert b'<p><select id="position" name="position"><option value="1">1</option><option value="2">2</option><option value="3">3</option></select> Position</p>' in response.data
        assert b'<p ><input type="submit" value="Save" class="btn btn-success"></p>' in response.data
        print(response.data)


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
