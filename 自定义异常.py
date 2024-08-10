class ApiException(Exception):
    """
    必须要继承自Exception
    自定义异常，用于指定code码及其对应的异常描述
    """

    code = ''
    msg = ''

    def __init__(self, code=None, msg=None):
        self.code = self.code if self.code else code
        self.msg = self.msg if self.msg else msg

    def __str__(self):
        return f'code：{self.code if self.code else '错误编码'} ， message：{self.msg if self.msg else '错误异常'}'


class ProofException(ApiException):
    msg = '凭证过期'


def test_error(code):
    if code == 4000:
        raise ProofException(code)



if __name__ == '__main__':
    try:
        test_error(4000)
    except ProofException as e:
        print(e)
