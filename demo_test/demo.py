from qa_core.query import data_processing
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model='qwen-max',
                   base_url=os.getenv('BASE_URI'),
                   temperature=os.getenv('TEMPERATURE'),
                   timeout=float(os.getenv("TIME_OUT"))
                   )

prompt = '''
        你是用户问题改写大师,你能根据用户的问题改写出三个同意思的变体，只输出这三个变体，不附加任何其他信息
        '''

messages = [
    SystemMessage(content=prompt),
    HumanMessage(content='入职流程是什么?')
]

if __name__ == '__main__':
    print(data_processing('你好 我爱 你'))
    result = model.invoke(messages)
    print(result.text)