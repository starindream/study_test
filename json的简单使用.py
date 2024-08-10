import json

#相关文档：https://blog.csdn.net/impoijimlq/article/details/130445399


def test_json():
    a = 'test'
    data = {a: '1', 'b': '2', }
    print(data)
    print(json.dumps(data, indent=4))  # indent 表示缩进


def test(params):
    print(params)
    return 'test'

def test_json_object_hoos():
    a = 'test'
    data = {a: '1', 'b': '2', }
    print(json.loads(json.dumps(data),object_hook=test))


if __name__ == '__main__':
    test_json_object_hoos()
    
