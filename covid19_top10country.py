import json
import pandas as pd

"""
covid19_summary.json資料內容有三個結構:Global,Countries和Date
由於pandas.read_json()方法只能處理一個結構的json資料
使用上述方法會出現錯誤: ValueError: Mixing dicts with non-Series may lead to ambiguous ordering
需使用python內建的import json方法來讀入json檔案
"""

#json資料來源:https://api.covid19api.com/summary
with open('covid19_summary.json', 'r') as read_file:
    data = json.load(read_file)  #注意json.load()轉成python後,會變成dict資料型態

#只取出Countries為鍵(key)之字典的值(value)
country_data = data['Countries']

#用pands的DataFrame轉成二維表格
df = pd.DataFrame(country_data)

#取出所需的國家名, 總確診人數, 總死亡人數
df = df.loc[:, ['Country', 'TotalConfirmed', 'TotalDeaths']]

#依照總確診人數遞減排序
df = df.sort_values(by='TotalConfirmed', ascending = False)

#依照遞減排序的結果重設index
df.index = range(len(df))


#新增死亡率欄位,使用df.eval()方法
#inplace參數True表示在原數據上生成, False則新生成DataFrame
df.eval('DeathRate = TotalDeaths/TotalConfirmed', inplace = True)

#資料的日期
date = data['Date']

#取出前十大國家
df = df.loc[0:9]

print(df)
print(date)


