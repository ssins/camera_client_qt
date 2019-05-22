import requests
import json
from config import *
from Camera import Camera


class DB_Requsets:
    def __init__(self, token=None):
        self.token = token

    def _db_post(self, api, data=None, token=None):
        url = DB_SERVER_ADDRESS + api
        header = {}
        if token:
            header['Authorization'] = 'Bearer ' + token
        if not data:
            data = {}
        return requests.session().post(url, data=data, headers=header)

    def regist(self, user_name, password):
        api = 'user/regist'
        data = {
            'user_name': user_name,
            'password': password
        }
        result = self._db_post(api, data)
        return result

    def login(self, user_name, password):
        api = 'user/login'
        data = {
            'user_name': user_name,
            'password': password
        }
        result = self._db_post(api, data)
        self.token = None
        if result:
            self.token = result.json().get('token', None)
        return self.token

    def reset(self, old_password, new_password):
        api = 'user/reset'
        data = {
            'old': old_password,
            'password': new_password
        }
        result = self._db_post(api, data, self.token)
        return result

    def reset_others(self, user_name, password):
        api = 'user/reset'
        data = {
            'user_name': user_name,
            'password': password
        }
        result = self._db_post(api, data, self.token)
        return result

    def delete_user(self, user_name):
        api = 'user/delete'
        data = {
            'user_name': user_name
        }
        result = self._db_post(api, data, self.token)
        return result

    def logout(self):
        self.__init__()

    def get_user_list(self):
        api = 'user/list'
        result = self._db_post(api, token=self.token)
        return result.json()

    def get_camera_list(self):
        api = 'camera/list'
        result = self._db_post(api, token=self.token)
        return [Camera.init_from_dict(d) for d in result.json()]

    def add_camera(self, camera):
        api = 'camera/add'
        data = camera.dict
        result = self._db_post(api, data, self.token)
        return result

    def delete_camera(self, sn):
        api = 'camera/delete'
        data = {
            'sn': sn
        }
        result = self._db_post(api, data, self.token)
        return result

    def add_permission(self, user_id, camera_id):
        api = 'permission/add'
        data = {
            'user_id': user_id,
            'camera_id': camera_id
        }
        result = self._db_post(api, data, self.token)
        return result

    def remove_permission(self, user_id, camera_id):
        api = 'permission/remove'
        data = {
            'user_id': user_id,
            'camera_id': camera_id
        }
        result = self._db_post(api, data, self.token)
        return result


# if __name__ == '__main__':
#     db_r = DB_Requsets()
#     token = db_r.login('root', 'root')
#     if token:
#         cameras = db_r.get_camera_list()
#         users = db_r.get_user_list()
#         for user in users:
#             for camera in cameras:
#                 db_r.remove_permission(user['id'],camera.id)
