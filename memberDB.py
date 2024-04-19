import pymysql

dbConn = pymysql.connect(user="root", password="12345", host="localhost", db='shopdb')

while True:
    print("******** 회원관리 프로그램 ********")
    print("1 : 회원 가입")
    print("2 : 회원 비밀번호 수정")
    print("3 : 회원 탈퇴")
    print("4 : 전체 회원목록 조회")
    print("5 : 프로그램 종료")
    print("*********************************")
    menuNum = input("메뉴 중 한가지를 선택하세요(1~5) : ")

    if menuNum == "5":
        print("프로그램을 종료합니다. 안녕히 가세요!")
        break



