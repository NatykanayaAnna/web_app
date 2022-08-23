import os
import unittest
import tempfile
from app import app
from models.banners import db


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.test_banner = {'status': 'True', 'banners_name': 'test', 'url': 'test.com', 'position': '1'}
        self.app = app.test_client()
        db.init_app(app)


    # def test_add_form_get(self):
    #     response = self.app.get('/add')
    #     print(response.data)
    #     assert b'<input class="form-control" id="banners_name" maxlength="50" minlength="2" name="banners_name" required type="text" value="">' in response.data
    #     assert b'<input id="status" name="status" type="checkbox" value="y">' in response.data
    #     assert b'<input id="image" name="image" type="file">' in response.data
    #     assert b'<input class="form-control" id="url" minlength="6" name="url" required type="text" value="">' in response.data
    #     assert b'<select class="form-control" id="position" name="position"><option value="1">1</option><option value="2">2</option><option value="3">3</option></select>' in response.data
    #     assert b'<input type="submit" value="Save" class="btn btn-success">' in response.data
    #
    #
    # def test_add_form_post(self):
    #     response = self.app.post('/add', data=self.test_banner)
    #     assert not b'form-group  has-error required' in response.data
    #     self.assertEqual(response.status_code, 200)
    #     print(response.data)
    #
    #
    # def test_edit_banner_get(self):
    #     response = self.app.get('/edit?banners_id=d2647fc7-a66f-4798-ac04-029797068058')
    #     assert b'<input class="form-control" id="banners_name" maxlength="50" minlength="2" name="banners_name" required type="text" value="dog">' in response.data
    #     assert b'<input class="form-control" id="url" minlength="6" name="url" required type="text" value="test.com">' in response.data
    #     assert b'<input id="image" name="image" type="file">' in response.data
    #     assert b' <input checked id="status" name="status" type="checkbox" value="y">' in response.data
    #     assert b'<select class="form-control" id="position" name="position"><option selected value="1">1</option><option value="2">2</option><option value="3">3</option></select>' in response.data
    #     assert b'<input type="submit" value="Save" class="btn btn-success">' in response.data
    #     print(response.data)


    def test_delete_banner_get(self):
        response = self.app.get('/delete?banners_id=d2647fc7-a66f-4798-ac04-029797068058')
        print(response.data)


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
