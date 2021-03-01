from attacut import tokenize
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer # สกัดคำ
from sklearn.neighbors import KNeighborsClassifier
from numpy import random

def chatBot(word):
    x = ['สวัสดีสวัสดีสบายดีมั้ยเป็นอย่างไรบ้างเป็นไงสวัสดีครับสวัสดีค่ะ', 'ชื่อชื่อชื่อเธอนายนางชื่ออะไรนามสกุลชื่อจริงครับค่ะ',"j3dbjflbadjfadกดกดกมทิอส่ิเีสกดิสี้ฟรดิสเ"]
    y = [['คือไรงง?', 'ไม่ได้ยิน :p', 'อะไรอะไร :3', 'พิมพ์ไร!!!'], ['ดีจ้า','สวัสดีครับ :)', 'ชื่อบอท Robot'],["ไม่เข้าใจ.............."]]
    embeding = [i for i in range(len(y))]

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
