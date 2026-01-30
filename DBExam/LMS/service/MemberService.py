from LMS.common import Session
from LMS.domain import Member

class MemberService:
    #주소로 활용하기 때문에 __init_없음
    @classmethod
    def load(cls):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("select count(*) as cnt from members")
                count = cursor.fetchone()['cnt']
                print(f"시스템에 현재 등록된 회원수는 {count}명 입니다.")

        except:
            print("MemberService.load()메서드에서 오류가 발생되었습니다.")

        finally:
            print("데이터베이스 접속을 종료합니다...")
            conn.close()

    @classmethod
    def login(cls):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        conn = Session.get_connection()

        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE uid = %s AND password = %s"
                cursor.execute(sql, (uid, pw))
                row = cursor.fetchone()

                if row:
                    member = Member.from_db(row)
                    if not member.active:
                        print("비활성화된 계정입니다.")
                        print("관리자에게 문의해주세요.")
                        return

                    Session.login(member)
                    print(f"{member.role}, {member.name}님 로그인 성공!")
                else:
                    print("아이디 또는 비밀번호가 틀렸습니다.")
        except:
            print("MemberService.login()메서드에서 오류가 발생되었습니다.")
        finally:
            conn.close()

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("현재 로그인 상태가 아닙니다.")
            print("로그인 후 이용해주세요.")

        Session.logout()
        print("로그아웃 완료 되었습니다.\n다음에 다시 이용해주세요!")

    @classmethod
    def signup(cls):
        print("\n[회원가입]")

        uid = input("아이디 : ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                check_sql = "SELECT id FROM members WHERE uid = %s"
                cursor.execute(check_sql, (uid,))

                if cursor.fetchone():
                    print("이미 존재하는 아이디입니다.")
                    return

                pw = input("비밀번호 : ")
                name = input("이름 : ")

                insert_sql = "INSERT INTO members (uid, password, name) VALUES (%s, %s, %s)"
                cursor.execute(insert_sql, (uid, pw, name))
                conn.commit()
                print("회원가입이 완료되었습니다.")
                print("로그인을 진행해주세요.")

        except Exception as e:
            conn.rollback()
            print(f"회원가입 도중 오류가 발생하였습니다. {e}")

        finally:
            conn.close()

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member
        print(f"내 정보 확인 > {member}")
        print("""
    [내 정보 수정 페이지]
    1. 이름 변경
    2. 비밀번호 변경
    3. 계정 비활성화 및 탈퇴    
        """)

        sel = input(">>> ")

        if sel == "1":
            new_name = input("새 이름 : ")
            if input(f"{new_name}으로 이름을 변경하시겠습니까? y : ") == "y":
                conn = Session.get_connection()

                try:
                    with conn.cursor() as cursor:
                        sql = "UPDATE members SET name = %s WHERE id = %s"
                        cursor.execute(sql, (new_name, member.id))
                        conn.commit()

                        member.name = new_name
                        print("이름 변경이 완료되었습니다.")

                finally:
                    conn.close()

            else:
                print("이름 변경을 취소하였습니다.")
                return

        elif sel == "2":
            new_pw = input("새 비밀번호 :  ")
            if input(f"{new_pw}로 비밀번호를 변경하시겠습니까? y : ") == "y":
                conn = Session.get_connection()

                try:
                    with conn.cursor() as cursor:
                        sql = "UPDATE members SET password = %s WHERE id = %s"
                        cursor.execute(sql, (new_pw, member.id))
                        conn.commit()

                        member.pw = new_pw
                        print("비밀번호 변경이 완료되었습니다.")

                finally:
                    conn.close()

            else:
                print("비밀번호 변경을 취소하였습니다.")
                return

        elif sel == "3":
            print("회원 비활성화 및 탈퇴를 진행합니다.")
            cls.delete()

        else:
            return


    @classmethod
    def delete(cls):
        if not Session.is_login():
            return
        member = Session.login_member

        print("""
        [회원 정보 변경]
        1. 회원 비활성화
        2. 회원 탈퇴
        """)

        sel = input(">>> ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if sel == "1":
                    sql = "UPDATE members SET active = FALSE WHERE id = %s"
                    cursor.execute(sql, (member.id,))
                    print("계정 비활성화가 완료되었습니다.")
                    print("재로그인 시 관리자에게 문의해주세요.")

                elif sel == "2":
                    sql = "DELETE FROM members WHERE id = %s"
                    cursor.execute(sql, (member.id,))
                    print("회원 탈퇴가 완료되었습니다.")

                conn.commit()
                Session.logout()

        finally:
            conn.close()

    @classmethod
    def admin_menu(cls):
        if not Session.is_admin():
            return

        print("""
    ==========================
         관리자 전용 페이지        
    ==========================
    1. 회원 임시 비밀번호 발급
    2. 회원 권한 변경
    3. 회원 블랙리스트 등록
    4. 회원 블랙리스트 해제
    5. 회원 비활성화 해제
    0. 뒤로가기
                
        """)

        sel = input(">>> ")

        if sel == "1":
            member = cls.get_member()
            re_pw = input("임시 비밀번호 : ")
            if input(f"{re_pw}로 임시 비밀번호를 지정하시겠습니까? y : ") == "y":
                conn = Session.get_connection()
                try:
                    with conn.cursor() as cursor:
                        sql = "UPDATE members SET password = %s WHERE id = %s"
                        cursor.execute(sql, (re_pw,))
                        conn.commit()

                        member.pw = re_pw
                        print("임시 비밀번호 발급이 완료되었습니다.")
                finally:
                    conn.close()
            else:
                print("임시 비밀번호 발급을 취소합니다.")

        elif sel == "2":
            member = cls.get_member()
            print("""
            1. 관리자   2. 매니저   3. 일반회원
            """)
            sel = input(">>> ")
            if sel == "1":
                conn = Session.get_connection()

                try:
                    with conn.cursor() as cursor:
                        sql = "UPDATE members SET role = %s WHERE id = %s"
                        cursor.execute(sql, ("admin", member.id))
                        conn.commit()

                        member.role = "admin"
                        print("관리자로 권한이 변경되었습니다.")

                finally:
                    conn.close()


    @classmethod
    def get_member(cls):
        re_id = input("대상 아이디 : ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE uid = %s"
                cursor.execute(sql, (re_id,))
                row = cursor.fetchone()  # 정보 확인을 위한 변수(row)
                member = Member.from_db(row)  # 불러온 정보를 객체로 만든
                return member
                # conn.commit() -> 데이터 변경할때만 commit하기
        finally:
            conn.close()