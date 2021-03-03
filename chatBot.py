import pyrebase
from attacut import tokenize
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer # สกัดคำ
from sklearn.neighbors import KNeighborsClassifier
from numpy import random
import json
import pyrebase
from typing import Optional
from fastapi import Body

with open("config/db_firebase.json", encoding="utf8") as json_file:
    json_load = json.load(json_file)
    config = json_load['firebase']
    pb = pyrebase.initialize_app(config)
    db = pb.database()

def chatBot(word):
    # x = ['สวัสดีสวัสดีสบายดีมั้ยเป็นอย่างไรบ้างเป็นไงสวัสดีครับสวัสดีค่ะ', 'ชื่อชื่อชื่อเธอนายนางชื่ออะไรนามสกุลชื่อจริงครับค่ะ',"j3dbjasexdfdfvcbo,l,tyqwtflbadjfadกดกดกมทิอส่ิเีสกดิสี้ฟรดิสเ"]
    # y = [['คือไรงง?', 'ไม่ได้ยิน :p', 'อะไรอะไร :3', 'พิมพ์ไร!!!'], ['ดีจ้า','สวัสดีครับ :)', 'ชื่อบอท Robot'],["ไม่เข้าใจ.............."]]
    # embeding = [i for i in range(len(y))]
    x = []
    y = []
    embeding = []
    count = 0
    dataset = db.child('chatbot').child('data').get()
    for i in dataset.each():
        if i.val():
            txt = ''
            y.append(i.val()['Answer'])
            if i.val()['Question']:
                for j in i.val()['Question']:
                    txt = txt + j
                x.append(txt)
                embeding.append(count)
                count += 1

    # กัน database error
    # idx_answer = []
    # for a in y:
    #     print("a :",a)
    #     idx = list(a)
    #     print("tdx :",idx)
    #     sli = idx[1:]
    #     print("sli",sli)
    #     idx_answer.append(sli)
        
    # เรียกใช้
    count_vector = CountVectorizer(tokenizer=tokenize)
    tf_tranformer = TfidfTransformer(use_idf=False)

    # หาค่า voetor
    x_train_count = count_vector.fit_transform(x)
    # print(x_train_count.shape)

    # เอาเข้า Model
    tf_tranformer.fit(x_train_count)
    x_train_tf = tf_tranformer.transform(x_train_count)
    # print(x_train_tf)

    my_classifier = svm.SVC(C=3, kernel='linear', degree=3, gamma='auto', probability=True)
    my_classifier.fit(x_train_tf, embeding)

    answer = [word] #['สวัสดีเป็นไงบ้าง'] # เข้าไปถามต้องเป็น List
    x_train_count = count_vector.transform(answer)
    x_test_tf = tf_tranformer.transform(x_train_count)
    # print(x_test_tf)

    prediction = my_classifier.predict(x_test_tf)
    # print(prediction)

    bot_ans = [random.choice(y[i]) for i in prediction]
    print(''.join(bot_ans))
    return ''.join(bot_ans)
