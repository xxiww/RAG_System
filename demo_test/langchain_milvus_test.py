import os

from langchain_core.documents import Document
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_milvus import Milvus,BM25BuiltInFunction
'''
Pymilvus使用方法 以及检索设置
'''

def milvus_init():

    bm_25 = BM25BuiltInFunction(
        input_field_names='text',
        output_field_names='sparse',
        analyzer_params={'type':'chinese'},
        enable_match=True
    )

    store = Milvus(
        embedding_function=bge_m3(),
        builtin_function=bm_25,
        collection_name='pymilvus_collection',
        connection_args={'uri':os.getenv('MILVUS_DATABASE_URL',default='http://localhost:19530'),'db_name':'Pymilvus'},
        vector_field=['dense','sparse'],
        text_field='text',
        primary_field='pk',
        auto_id=False,
        enable_dynamic_field=True,
        consistency_level='Session',
        drop_old=True
    )

    documents = [
        Document(
            page_content='入职流程包括申请表填写，体检报告提交以及劳务合同签署',
            metadata={'source':'hr','doc_id':'hr_001'}
        ),
        Document(
            page_content='比特币将会在今年突破$99,000,000',
            metadata={'source': 'finance', 'doc_id': 'fin_001'}
        )
    ]
    store.add_documents(documents,ids=['hr_001','fin_001'])
    # return store
#   检索内容
    result = store.similarity_search_with_score(
        query='预测一下比特币的价格',
        k=2
    )

    for doc, score in result:
        print('score', score)
        print('page_content', doc.page_content)
        print('metadata', doc.metadata)




def bge_m3():
    embed = OllamaEmbeddings(model='bge-m3',
                             base_url="http://localhost:11434")
    return embed



if __name__ == '__main__':
    milvus_init()
    # query = input("请输入您的问题!")
    # result = store.similarity_search_with_score(
    #     query=query,
    #     k=2
    # )
    #
    # for doc, score in result:
    #     print('score', score)
    #     print('page_content', doc.page_content)
    #     print('metadata', doc.metadata)