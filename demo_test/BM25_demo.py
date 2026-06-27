from rank_bm25 import BM25Okapi

docs = [
    '新人 入职 需要 提交 身份证 复印件 学历证明 离职证明 银行卡 信息',
    '员工 材料 归档 要求 包括 合同 审批单 培训记录',
    '公司 制度 汇编 包含 人事 财务 采购 行政 管理办法'
]

tokenzier = [doc.split() for doc in docs]
print(tokenzier)
bm25 = BM25Okapi(tokenzier)
query = '新人 入职 材料'
socre = bm25.get_scores(query.split())
doc_list = []
for doc,score in sorted(zip(docs,socre),key=lambda x : x[1],reverse=True):
    print(round(score,3),doc)