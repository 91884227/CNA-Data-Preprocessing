# CNA-Data-Preprocessing

### usage
```
python CNA_preprocessing.py FILENAME MIN_LENGTH
```


| Parameter | meaning | e.g. |
| -------- | -------- | -------- |
| FILENAME     | 檔案名稱    | CNA_title.csv     |
| MIN_LENGTH    | 保留大於 MIN_LENGTH 的標題   | 10  |

執行完後即生成 `FILENAME_adjust.npy`

### example
```
python CNA_preprocessing.py CNA_title.csv 10
```

執行完後即生成 `CNA_title_adjust.npy`
