import os
import openpyxl


def getTT():
    TT = [['', '', '', '', 'Lunch', '', '', ''], ['', '', '', '', 'Lunch', '', '', ''],
          ['', '', '', '', 'Lunch', '', '', ''], ['', '', '', '', 'Lunch', '', '', ''],
          ['', '', '', '', 'Lunch', '', '', ''], ['', '', '', '', 'Lunch', '', '', '']]
    return TT

tt={}

folders=next(os.walk('C:/Users/Swadesh Sharma/Desktop/SchedulXpert/Test 5/'))[1]
print(folders)
day_cell = ['7', '8', '9', '10', '11']
time_cell = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
for i in list(folders):
    files=next(os.walk(f'C:/Users/Swadesh Sharma/Desktop/SchedulXpert/Test 5/{i}/'))[2]
    print(i)
    for j in list(files):
        tt[j]=getTT()
        w=openpyxl.load_workbook(f'C:/Users/Swadesh Sharma/Desktop/SchedulXpert/Test 5/{i}/{j}')
        wb=w.active
        for day in [0,1,2,3,4]:
            for time in [0,1,2,3,5,6,7]:
                if str(wb[time_cell[time]+day_cell[day]].value)=='None':
                    continue
                if tt[j][day][time]!= '':
                    continue
                if '/' in str(wb[time_cell[time]+day_cell[day]].value):
                    if time==7:
                        continue
                    tt[j][day][time]=tt[j][day][time+1]=wb[time_cell[time]+day_cell[day]].value
                    continue
                tt[j][day][time] = wb[time_cell[time] + day_cell[day]].value

for i,j in tt.items():
    print(i)
    for k in j:
        print(k)



