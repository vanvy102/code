# Import thư viện
from sklearn.linear_model import LinearRegression
import numpy as np
import csv
from vnstock import*
data=[]
cp=listing_companies()
check='ngân hàng thương mại cổ phần'
nh=[]
for n in range(len(cp)):
    if check in cp.loc[n][2].lower():
        nh.append(cp.loc[n][0])
print(len(nh))
for ticket in nh:
    linkfile='./nganhang/'+ticket+'.csv'
    with open(linkfile) as file:
        fp=csv.reader(file)
        header=next(fp)
        for row in fp:
            data.append(row)
    # Tạo dữ liệu giả định
    K=[]
    h=[]
    for i in range(len(data)):
        K.append([float(data[i][1]),float(data[i][2])])
        h.append(float(data[i][4]))
    # Tạo mô hình hồi quy tuyến tính
    model = LinearRegression()

    # Huấn luyện mô hình với dữ liệu
    model.fit(K, h)

    # In ra các hệ số của mô hình
    print('Coefficients:', model.coef_)

    # Dự đoán giá trị mới
    x_new = np.array([[48850.0,48222.0]])
    y_new = model.predict(x_new)
    print('Predicted value:', y_new)
