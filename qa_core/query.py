#### 用户请求进来之后 进行简单的意图识别
from data.fast_data import FAST_REP,FOLLOW_UP_REP
# 数据处理
def data_processing(query):
    if query:
        return ''.join(query.split())
    return '空问题!!!'
#
#意图识别
## 1.快回复
def fast_resp(query):
    if not query:
        return None
    for pattern in FAST_REP:
        if pattern.search(data_processing(query)):
            return '你好,我是本企业的智能回复助手,您可以询问我企业内部在您权限内的任何问题～'
        return None
## 2.标准问答对

## 3.追问
def follow_up(history,query):
    if len(str(query)) > 8 and history:
        for pattern in FOLLOW_UP_REP:
            if pattern.search(data_processing(query)):
                return '进入追问环节'
    return None

if __name__ == '__main__':
    print(fast_resp('hi'))