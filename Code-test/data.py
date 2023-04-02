from vnstock import*
import pandas as pd
import os 
import datetime
import config as cf
#lay moc thoi gian giao dich trong 30 ngay
current_time= datetime.date.today()
thirty_days_ago= current_time+ datetime.timedelta(-30)
#os.makedirs('nganhang', exist_ok=True) 
start_time=str(thirty_days_ago)
end_time=str(current_time)
#lay thong tin cua cac ngan hang
nh=cf.get_ticket()
print(nh)
#lấy thông tin giao dich của từng ngân hàng
for ticket in nh:
    df = stock_historical_data(symbol=ticket, 
                            start_date=start_time, 
                            end_date=end_time)
    linkfile='./nganhang/'+ticket+'.csv'
    print(linkfile)
    df.to_csv(linkfile,index=False)
