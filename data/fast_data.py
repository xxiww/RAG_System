import re
FAST_REP_PATTERNS = [
    r'^你好$',           # 精确匹配"你好"
    r'^您好$',           # 精确匹配"您好"
    r'^hello$',         # 英文问候
    r'^hi$',            # 英文问候
    r'^谢谢$',          # 感谢
    r'^感谢$',          # 感谢
    r'^thank',         # thank you/thanks等
    r'^你是',           # 询问身份
    r'^你是谁',         # 询问身份
    r'^你是什么',       # 询问身份
]

FOLLOW_UP = [
    r'^那么$',           # 精确匹配"你好"
    r'^这个$',           # 精确匹配"您好"
    r'^那个$',         # 英文问候
    r'^然后$',            # 英文问候
    r'^应该$',          # 感谢
]

# 编译正则表达式对象
FAST_REP = [re.compile(pattern,re.IGNORECASE) for pattern in FAST_REP_PATTERNS]
FOLLOW_UP_REP = [re.compile(pattern,re.IGNORECASE) for pattern in FOLLOW_UP]

if __name__ == '__main__':
    print(FAST_REP)
    print(FOLLOW_UP_REP)