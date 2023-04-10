import streamlit as st
import numpy as np 
import pandas as pd
import time

st.title("Streamli 超入門")

st.write('プログレスバーの表示')
'Start!!'


bar = st.progress(0)
latest_iteration = st.empty()

for i in range(100):
    latest_iteration.text(f'Iteration {i +1}')
    bar.progress(i+1)
    time.sleep(0.1)

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
#DataFrameを表示させる
st.dataframe(df, width = 200, height=100)

#DataFrameを表示させる.最大値をハイライト表示させる
st.dataframe(df.style.highlight_max(axis=0))

# 折れ線グラフを表示させる
st.line_chart(df)

# 棒グラフを表示させる
st.bar_chart(df)


#テーブルを作成する.最大値をハイライト表示させる
st.table(df.style.highlight_max(axis=0))


#マークダウン記法を書く
"""
# 章
## 節
### 項

```python 
import streamlit as st 
import numpy as np 
import pandas as pd 
```
"""
   
#マップを表示
df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon']
)
st.map(df2)

#画像を表示する
# チェックボックスを使用する
st.write("画像表示")
if st.checkbox("show image"):
    pass

#セレクトボックスを表示する
option = st.selectbox(
    "your favorite no",
    list(range(1,11)))

"あなたの好きな数字は ", option, "です"

#2カラムに設定する
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander1 = st.expander("問い合わせ１")
expander1.write("問い合わせ１の回答")
expander1.text_input("あなたの趣味を教えてください")
expander2 = st.expander("問い合わせ２")
expander2.write("問い合わせ２の回答")
expander3 = st.expander("問い合わせ３")
expander3.write("問い合わせ３の回答")

#テキストボックスを使用する
option2 = st.text_input("あなたの趣味を教えてください", key="1")
"あなたの趣味：", option2

#スライダーを使う
option3 = st.slider("あなたの今の調子は", 0,100,40)
"あなたの調子は：", option3




