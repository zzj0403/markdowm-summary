# time str int Float


class Filed:
    def __init__(self, name,
                 column_type,
                 primary_key,
                 default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default


class StringFiled(Filed):
    def __init__(self, name,
                 column_type='varchar(64)',
                 primary_key=False,
                 default=None):
        super().__init__(name, column_type, primary_key, default)


class IntegerFiled(Filed):
    def __init__(self, name,
                 column_type='int',
                 primary_key=False,
                 default=0):
        super().__init__(name, column_type, primary_key, default)


class FloatFiled(Filed):
    def __init__(self, name,
                 column_type='float',
                 primary_key=False,
                 default=None):
        super().__init__(name, column_type, primary_key, default)


class TimeFiled(Filed):
    def __init__(self, name,
                 column_type='datetime',
                 primary_key=False,
                 default=None):
        super().__init__(name, column_type, primary_key, default)


class OrmMetaclass(type):
    # pass
    # class_name,class_bases,class_dic
    def __new__(cls, class_name, class_bases, class_dic):

        if class_name == 'Models':
            return type.__new__(cls, class_name, class_bases, class_dic)
        table_name = class_dic.get('table_name', class_name)
        # print(class_dic)
        primary_key = None
        mappings = {}
        for k, v in class_dic.items():
            if isinstance(v, Filed):  # 把字段以外的属性过滤
                mappings[k] = v
                if v.primary_key:
                    if primary_key:
                        raise TypeError('只能一个主键')
                    primary_key = v.name
        # print(mappings)
        for key in mappings.keys():
            class_dic.pop(key)
        if not primary_key:
            raise TypeError('必须要有一个主键!!!')

        class_dic['table_name'] = table_name
        class_dic['primary_key'] = primary_key
        class_dic['mappings'] = mappings
        print(class_dic)
        return type.__new__(cls, class_name, class_bases, class_dic)


class Models(dict, metaclass=OrmMetaclass):

    # 对象.属性， 属性没有时触发
    def __getattr__(self, item):
        return self.get(item)

    # 对象.属性 = 属性值 时触发
    def __setattr__(self, key, value):
        self[key] = value


class log_table(Models):
    id = IntegerFiled(name='id', primary_key=True)
    ip = StringFiled(name='ip')
    method = StringFiled(name='method')
    request = StringFiled(name='request')
    stat_code = IntegerFiled(name='stat_code')
    boy_size = IntegerFiled(name='boy_size')
    request_body = StringFiled(name='request_body')
    user_agent = StringFiled(name='user_agent')
    request_time = FloatFiled(name='request_time')
