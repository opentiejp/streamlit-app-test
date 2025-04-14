import time

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')
df = pd.DataFrame(
        {
            '1列目': [1, 2, 3, 4],
            '2列目': [10, 20, 30, 40],
            '3列目': [1000, 200, 300, 400]
        })

# DataFrameを表示
# st.write(df)

# DataFrameを表形式で表示
st.dataframe(df.style.highlight_max(axis=0), width=400, height=400)

# DataFrameを静的な表形式で表示
# st.table(df.style.highlight_max(axis=0))

# マジックコマンド（マークダウン形式で記述ができる（なお、コードの記述で、言語名は小文字の p 始まりであることにも注意））
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

df = pd.DataFrame(
        np.random.rand(20, 3),
        columns=['a', 'b', 'c']
)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

df = pd.DataFrame(
        np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
        columns=['lat', 'lon']
)
st.map(df)

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('91.png')
    st.image(img, caption='Motoki', use_container_width=True)

# st.sidebar.write('Interactive Widgets')
st.write('Interactive Widgets')

option = st.selectbox(
        'あなたが好きな数字を教えてください:',
        list(range(1, 11))
)

st.write(f'あなたの好きな数字は {option} です。')

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
text = st.text_input('あなたの趣味を教えてください。')
st.write(f'あなたの趣味：  {text}')

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
st.write(f'コンディション： {condition} %')

left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示する')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1', expanded=False)
expander2 = st.expander('問い合わせ2', expanded=False)
expander3 = st.expander('問い合わせ3', expanded=False)
expander1.write('問い合わせ1の回答')
expander2.write('問い合わせ2の回答')
expander3.write('問い合わせ3の回答')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!'
