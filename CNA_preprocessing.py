#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import pandas as pd
import numpy as np
import re
from itertools import compress
from tqdm import tqdm
import sys


# In[2]:


def str_adjust(str_):
    buf = str_
    try:
        m = re.match(r'(.*／)(.*)', str_)
        buf = m.group(2)
    except:
        pass
    return(buf)


# In[3]:


if __name__ == '__main__':
    FILENAME =  sys.argv[1]
    MIN_LENGTH = int(sys.argv[2])
#     FILENAME = "CNA_title.csv"
#     MIN_LENGTH = 8
    df = pd.read_csv(FILENAME, encoding="utf-8")
    title = df.title.to_numpy()

    # 前面的標籤去除
    title_A = [str_adjust(i) for i in tqdm(title)]

    # 將 全球中央的標題 去除
    title_B = [i for i in title_A if not i.startswith("全球中央")]

    # 將 標題小於 10 的 標題 去除
    title_C = [i for i in title_B if len(i) >= MIN_LENGTH]

    # save
    name = "%s_adjust.npy" % FILENAME[:-4]
    try:
        np.save(name, title_C)
        print("preprocessing successfully")
        print("save as %s" % name)
    except:
        print("preprocessing failed")

