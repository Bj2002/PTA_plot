import datetime
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'FangSong'
stu_index = {}#学号与数组下标的对应关系
prob_index = {}#题目编号与数组下标的对应关系
stu_cnt = 0
prob_cnt = 0
day_cnt = 130

t0 = datetime.datetime (2022 , 9 , 27 , 13, 26 ,00 )
file = open ("submission_list.txt" , "r")
line = file.readline()

max_peo = 50
max_prob = 80
max_day = 150

score_last = [[0 for _ in range (max_prob)] for __ in range (max_peo)]
score_tot = [[0 for _ in range (max_day)] for __ in range (max_peo)]
tot_sub = [0 for _ in range (max_peo)]
night_sub = [0 for _ in range (max_peo)]

hour_sub = [0 for _ in range (24)]
hour_AC = [0 for _ in range (24)]

while (line) :

    sList = line.split()
    #print(sList)
    sub_time = datetime.datetime.strptime(sList[0] + sList[1], "%Y%m%d%H%M%S") ;
    dlt_days = int((sub_time - t0).total_seconds()//60//60//24)+1

    sid = stu_index.get (sList[5] , 0)
    if (sid == 0 ) :
        stu_cnt = stu_cnt + 1
        sid = stu_cnt
        stu_index[sList[5]] = stu_cnt
    #获得当前学生的数组下标。如果是第一次，则为该学生分配数组下标

    pid = prob_index.get(sList[4] , 0)
    if (pid == 0) :
        prob_cnt = prob_cnt + 1
        pid = prob_cnt
        prob_index[sList[4]] = prob_cnt
    #获得当前题目的数组下标。如果是第一次，则为该题目分配数组下标

    tot_sub[sid] = tot_sub[sid] + 1
    if((sub_time.hour >= 0 and sub_time.hour <= 5 ) or (sub_time.hour== 23)) :
        night_sub[sid] = night_sub[sid] + 1

    hour_sub[sub_time.hour] = hour_sub[sub_time.hour] + 1;
    if (sList[2] == "答案正确") :
        hour_AC[sub_time.hour] = hour_AC[sub_time.hour] + 1;

    #print(sList)
    score = int(sList[3])

    if (score > score_last[sid][pid]) :
        score_tot[sid][dlt_days] = score_tot[sid][dlt_days] + score - score_last[sid][pid]
        score_last[sid][pid] = score
    #print(pid)
    line =file.readline()
    #break
file.close ()

plt.xlabel ("一天中的时间（单位:小时）")
plt.ylabel ("提交次数")
plt.title ("一天中的时间与提交次数的折线图")

X = [_ for _ in range (24)]
Y = hour_sub

plt.plot(X,Y)
plt.show()




plt.xlabel ("一天中的时间（单位:小时）")
plt.ylabel ("通过率")
plt.title ("一天中的时间与通过率的折线图")

X = [_ for _ in range (24)]

for i in range(24) :
    print(hour_AC[i] , hour_sub[i])

    if (hour_sub[i] == 0) :
        Y[i] = 0
    else :
        Y[i] = hour_AC[i] / hour_sub[i]

    print(Y[i])
plt.plot(X,Y)
plt.show()





for i in range (1 , stu_cnt + 1 ) :
    for j in range (1 , day_cnt ) :
        score_tot[i][j] = score_tot[i][j] + score_tot[i][j-1]


id2name = {}
file = open ("id2name.txt" , "r")

line = file.readline ()
while (line ) :

    line = line.split()
    line = line[0].split(',')

    id2name[line[0]] = line[1]
    line = file.readline()



X = []
Y = []
plt.cla ()

for sid in id2name :
    idx = stu_index[sid]
    #print(idx , id2name[sid] , night_sub[idx] /  tot_sub[idx] * 100 ,score_tot[idx][day_cnt-1])
    plt.scatter (night_sub[idx] /  tot_sub[idx] * 100 , score_tot[idx][day_cnt-1] )
    plt.xlabel ("熬夜提交在所有提交中占有的百分比")
    plt.ylabel ("最终的得分")
    plt.title ("熬夜提交在所有提交中占有的百分比-最终的得分 散点图")

    X.append (night_sub[idx] /  tot_sub[idx]  )
    Y.append (score_tot[idx][day_cnt-1])

    print(score_tot[idx][day_cnt-1] , sid , id2name[sid])

print(X)
print(Y)
plt.show()
