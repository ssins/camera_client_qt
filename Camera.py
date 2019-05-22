class Camera:
    def __init__(self, sn, address, action_type, user_name, password, statues=None, kind=None, brand=None, model=None, name=None, id=None):
        self.dict = {}
        self.id = id
        self.sn = sn
        self.address = address
        self.action_type = action_type
        self.user_name = user_name
        self.password = password
        self.dict['sn'] = self.sn
        self.dict['address'] = self.address
        self.dict['action_type'] = self.action_type
        self.dict['user_name'] = self.user_name
        self.dict['password'] = self.password
        if statues:
            self.statues = statues
            self.dict['statues'] = self.statues
        if kind:
            self.kind = kind
            self.dict['kind'] = self.kind
        if brand:
            self.brand = brand
            self.dict['brand'] = self.brand
        if model:
            self.model = model
            self.dict['model'] = self.model
        if name:
            self.name = name
            self.dict['name'] = self.name

    def get_simple_info(self):
        return '{}({})'.format(self.name, self.sn)

    @staticmethod
    def init_from_dict(d):
        return Camera(d.get('sn'), d.get('address'), d.get('action_type'), d.get('user_name'), d.get(
            'password'), d.get('statues'), d.get('kind'), d.get('brand'), d.get('model'), d.get('name'), d.get('id'))
