 # DB 프로그램 만들기(4월19일 실습)- 2번 회원정보 수정 추가하기
import pymysql

# dbConn = pymysql.connect(host='localhost', user='root', password='domybest2024@', db='shopdb')
dbConn = pymysql.connect(user='root', password='12345', host='localhost', db='shopdb')
#보통은 위와 같이 계정(root)을 먼저 쓴다고. 그 다음에 패스워드 순으로.
# 다음으로 메뉴를 만들어본다.

while True:
    print("******* 회원관리 프로그램 *******")
    print("1 : 회원 가입")
    print("2 : 회원 비밀번호 수정")
    print("3 : 회원 탈퇴")
    print("4 : 전체 회원목록 조회")
    print("5 : 프로그램 종료")
    print("**************************************")
    menuNum = input("메뉴 중 한 가지를 선택하세요(1~5) : ")

    if menuNum == "1":
        print("회원정보를 입력하세요")
        memberID = input("1) 회원아이디를 입력하세요 :")
        memberName = input("2) 회원이름을 입력하세요 :")
        address = input("3) 회원주소를 입력하세요 :")

        sql = f"INSERT INTO membertbl VALUES('{memberID}','{memberName}','{address}')"
        cur = dbConn.cursor()
        result = cur.execute(sql)

        if result == 1:
            print("축하합니다! 회원가입에 성공하셨습니다.")
        else:
            print("회원가입 실패입니다.")

        cur.close()
        dbConn.commit()

    elif menuNum == "2":
        memberID = input("1) 수정할 회원의 아이디를 입력하세요 :")
        memberName = input("2) 수정할 회원의 이름을 입력하세요 :")
        address = input("3) 수정할 회원주소를 입력하세요 :")

        sql = f"UPDATE membertbl SET memberName ='{memberName}', memberAddress='{address}' WHERE memberID = '{memberID}'"
        cur = dbConn.cursor()
        result = cur.execute(sql)

        if result == 1:
            print("축하합니다! 회원수정에 성공하셨습니다.")
        else:
            print("회원수정 실패입니다.")

        cur.close()
        dbConn.commit()

    elif menuNum == "3":
        memberID = input("1) 탈퇴할 회원의 아이디를 입력하세요 :")
    #     memberName = input("2) 탈퇴할 회원의 이름을 입력하세요 :") # 이 나머지는 불필요.
    #     address = input("3) 탈퇴할 회원주소를 입력하세요 :")
    #
        sql = f"DELETE FROM membertbl WHERE memberID = '{memberID}'"
        cur = dbConn.cursor()
        result = cur.execute(sql)

        if result == 1:
            print("회원탈퇴에 성공하셨습니다.")
        else:
            print("회원탈퇴 실패입니다.")
    #
    #     cur.close()
    #     dbConn.commit()

    elif menuNum == "5":
        print("프로그램을 종료합니다. 안녕히가세요")
        dbConn.close()
        break

    else:
        print("잘못 입력하셨습니다. 다시 입력해 주세요.")