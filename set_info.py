import db_connection
import get_info

# import subject_info

connection = db_connection.connection()


def setFacultyInfo(f_id, f_name, f_phone):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"insert into faculty_info values('{f_id}','{f_name}','{f_phone}')")
    conn.commit()
    return


def update_faculty(f_id, f_name, f_phone):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"update faculty_info set f_name='{f_name}', f_phone='{f_phone}' where f_id='{f_id}'")
    conn.commit()
    return


def checkDuplication(f_id):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute("select * from faculty_info where f_id='" + f_id + "'")
    rec = curr.fetchall()
    if len(rec) >= 1:
        return True
    return False


def delete_faculty(f_id):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute("delete from faculty_info where f_id='"+f_id+"'")
    conn.commit()


def add_fac_load(f_id,sub,sec,th,lab):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"insert into faculty_load_2 values('{f_id}','{sub}','{sec}',{th},{lab})")
    conn.commit()


def add_subject(sub_code, sub_name, sub_type):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"insert into subjects values('{sub_code}','{sub_name}','{sub_type}')")
    conn.commit()


def update_subject(sub_code, sub_name, sub_type):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"update subjects set subject_name='{sub_name}', subject_type='{sub_type}' where subject_code='{sub_code}'")
    conn.commit()


def delete_sub(sub_code):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"delete from subjects where subject_code='{sub_code}'")
    conn.commit()


def delete_fac_load(f_id,sub,sec,th,lab):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"delete from faculty_load where f_id='{f_id}' and sub_code='{sub}' and section='{sec}' and"
                 f" theory='{th}' and lab='{lab}'")
    conn.commit()


def delete_fac_loads(f_id):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"delete from faculty_load where f_id='{f_id}'")
    conn.commit()


def insert_section(sec,faculty):
    conn = connection.getConnection()
    curr = conn.cursor()
    f_id=get_info.get_fac_id(faculty)
    if int(sec[-2])%2==0:
        year=2
    else:
        year=1
    curr.execute(f"insert into sections values('{sec}','{f_id}',{year})")
    conn.commit()


def insert_lab(sub,lab,f_id,sec):
    conn = connection.getConnection()
    curr = conn.cursor()
    curr.execute(f"insert into lab_allotment values('{sub}','{lab}','{f_id}','{sec}')")
    conn.commit()
