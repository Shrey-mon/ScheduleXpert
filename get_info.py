import itertools
import os
import random

import db_connection
import faculty_info

connection = db_connection.connection()


def getFacultyInfo():
    conn = connection.getConnection()
    curr = conn.cursor()
    print("Fetching data")
    curr.execute("select * from faculty_info")
    facultyInfo = curr.fetchall()
    if len(facultyInfo) == 0:
        print("No record Found")
        return

    facultylist = []
    for info in facultyInfo:
        faculty = faculty_info.FacultyInfo(list(info))
        facultylist.append(faculty)

    return facultylist

fac_list = getFacultyInfo()
def get_fac_dict():
    fac_dict = {}
    for fac in fac_list:
        fac_dict[fac.getFId()] = fac
    return fac_dict


def getFacLoad():
    conn = connection.getConnection()
    curr = conn.cursor()
    # curr.execute("select * from faculty_load where sub_code like 'CS%'")
    # curr.execute("select * from faculty_load where sub_code like '__4%' order by f_id desc")
    curr.execute("select * from faculty_load_2 order by f_id desc")
    load = curr.fetchall()
    loadList = []
    for l in load:
        loadList.append(list(l))
    return loadList


def get_sub_names():
    conn = connection.getConnection()
    curr = conn.cursor()
    # curr.execute("select * from subjects")
    curr.execute("select * from subjects where subject_code like '__3%' or subject_code like '__5%'")
    subjects = {}
    opt = curr.fetchall()
    for sub in opt:
        subjects[sub[0]] = [sub[1], sub[2]]

    return subjects


def get_unallotted_sub():
    load = getFacLoad()
    sec_dict = {
        'CS3': ['A', 'B', 'C'],
        'AL3': ['A', 'B', 'C'],
        'CY3': ['A', 'B'],
        'CS5': ['A', 'B', 'C'],
        'AL5': ['A', 'B', 'C'],
        'CY5': ['A', 'B']
    }
    sub_name_dict = get_sub_names()
    all_sub = []
    sec_list = list(sec_dict.keys())
    sub_list = list(sub_name_dict.keys())
    for sub in sub_list:
        for sec in sec_list:
            if sec in sub:
                for s in sec_dict[sec]:
                    all_sub.append([sub, s])

    allotted_sub = []
    for i in load:
        allotted_sub.append([i[1], i[2]])

    unallotted_sub = []
    for i in all_sub:
        if i not in allotted_sub:
            unallotted_sub.append(i)

    return unallotted_sub


def get_sections_and_mentors(year):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"select * from sections where year={1}")
    section_dict = {}
    f_list = fac_list
    l = curr.fetchall()
    for i in l:
        for fac in f_list:
            if i[1] == fac.getFId():
                section_dict[i[0]] = fac
                break

    return section_dict


def get_fac_id(fac):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"select f_id from faculty_info where f_name='{fac}'")
    id = curr.fetchone()
    # print(id[0])
    return id[0]


def get_sub_names_by_section(sec):
    conn = connection.getConnection()
    curr = conn.cursor()
    sub = ''
    if 'CS' in sec:
        sub = 'CS' + sec[-2]
    elif 'AIML' in sec:
        sub = 'AL' + sec[-2]
    elif 'CY' in sec:
        sub = 'CY' + sec[-2]
    curr.execute(f"select subject_code from subjects where subject_code like '{sub}%'")
    l = curr.fetchall()
    a = []
    for i in l:
        a.append(i[0])
    return a


def get_sub_by_section(sec):
    conn = connection.getConnection()
    curr = conn.cursor()
    sub = ''
    if 'CS' in sec:
        sub = 'CS' + sec[-2]
    elif 'AIML' in sec:
        sub = 'AL' + sec[-2]
    elif 'CY' in sec:
        sub = 'CY' + sec[-2]
    curr.execute(f"select * from subjects where subject_code like '{sub}%' order by subject_code")
    l = curr.fetchall()
    a = {}
    for i in l:
        a[i[0]] = [i[1], i[2]]
    return a


# print(get_sub_names_by_section('CSE 4A'))
# get_fac_id('Prof. Priyank Nayak')

# query=" select sub_code,subject_name,section,f_name from faculty_info, faculty_load, subjects where " \
#       "faculty_load.f_id=faculty_info.f_id and faculty_load.sub_code=subjects.subject_code and subject_code='AL608' "\
#       "order by section;"


def get_labs():
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"select * from labs")
    l = curr.fetchall()
    d = {}
    for i in l:
        d[i[0]] = i[1]

    return d


def get_labs_by_sec(sec):
    conn = connection.getConnection()
    curr = conn.cursor()
    s=''
    if 'CS' in sec:
        if '3' in sec:
            s = 'CS3'
        elif '5' in sec:
            s = 'CS5'
    elif 'CY' in sec:
        if '3' in sec:
            s = 'CY3'
        elif '5' in sec:
            s = 'CY5'
    elif 'AI' in sec:
        if '3' in sec:
            s = 'AL3'
        elif '5' in sec:
            s = 'AL5'

    curr.execute(f"select * from lab_allotment where subject like '{s}%' and section='{sec[-1]}' order by subject")
    l = curr.fetchall()
    d = {}
    for i in l:
        d[i[0]] = [i[1], i[2]]
    return d


def get_lab_allotment():
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"select * from lab_allotment")
    l = curr.fetchall()
    f_dict=get_fac_dict()
    d = {}
    for i in l:
        if i[0] in d.keys():
            d[i[0]].append([i[3], i[1],f_dict[i[2]]])
        else:
            d[i[0]] = [[i[3], i[1],f_dict[i[2]]]]

    return d

# d=get_lab_allotment()
# for i,j in d.items():
#     print(i,j)

def get_lab():
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"select lab from lab_allotment")
    l = curr.fetchall()
    f_dict=get_fac_dict()
    d = {}
    for i in l:
        if i[0] in d.keys():
            d[i[0]]+=1
        else:
            d[i[0]]=1

    return d


# print(get_labs_by_sec('CSE 3A'))

# d=get_lab()
# for i,j in d.items():
#     print(i,j)

# select f_name,sub_code,subject_name,section from faculty_info, subjects, faculty_load_2 where
# faculty_load_2.f_id=faculty_info.f_id and faculty_load_2.sub_code=subjects.subject_code and faculty_load_2.f_id='F102';

# select faculty_info.f_id,f_name,sub_code, subject_name, section from faculty_load_2,faculty_info,subjects where
# faculty_load_2.f_id=faculty_info.f_id and faculty_load_2.sub_code=subjects.subject_code and faculty_load_2.sub_code
# like 'CS5%' and section='c' order by sub_code

# l=['','']
# if l[0]=='' or l[1]=='':
#     print('pass')


# l1=[[1,2],[2,1]]
# l2=[[2,1],[1,2]]
# print(l1==l2)
# a=10
# b=a
# a+=1
# print(a,b)
# a=[1,2,3,4,5]
# b=a.pop()
# print(a,b)
# import sys
# print(sys.getrecursionlimit())
# l=['A','Aa','B']
# print(l.count('A'))
# a=[1,2,3,4,5]
# b=list(itertools.product([[1,2]],a))
# print(b)
# l=[1,2,3]
# l2=[2,1,3]
# print(l==l2)
# a='CSE 3A'
# print(a[0:-1])