# 背单词小程序

## 使用方式
* 1.准备单词表，将单词分为若干个unit，存放在`word_lists`文件夹内，命名从`unit1.txt`~`unitN.txt`
* 2.`unit1.txt`中每行构成：`英文单词`+ `,`(半角英文逗号分隔)+`中文释义`(若多个释义则以`;`分隔)，例如
    * `traditional,传统的;惯例的;口传的;传说的`
* 3. `python main.py` 即可

### tips
* `main.py`中，`correct_number`为一个单词正确次数，达到该正确次数则该单词视为记忆成功，`correct_number`越大，则单词记的越熟练
* 如果一次背的过程中断了，没关系，当天背诵的剩余任务在`datasets/memorizing_history`中保存，下次直接`python main.py`又可以接着背啦~

## requirement
* python3
* pyttsx3

## TODO
* 如果可以换个好点的TTS发音库
* 加入艾宾浩斯遗忘曲线去回忆背过的单词
* 改的漂亮点