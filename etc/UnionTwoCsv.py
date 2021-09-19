import pandas as pd

target = pd.read_csv('대상1.csv')
doc = pd.read_csv('대상2.csv')

result = pd.merge(target, doc, on="key로쓸컬럼")

result.to_csv('결과파일.csv')
