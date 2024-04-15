import pymysql  # mysql과 연동시켜주는 라이브러리

# 파이썬과 mysql 서버간의 커넥션 생성
# 1) 계정 : root(관리자 계정)
# 2) 비밀번호 : 12345
# 3) 데이터베이스가 설치된 컴퓨터의 IP주소
#   - 본인 컴퓨터면 localhost, 다른컴퓨터면 그 컴퓨터의 ip주소
#   - 192.168.0.100(교수용 컴퓨터 ip)
# 4) 데이터베이스 스키마 이름(ex:shopdb)

dbConn = pymysql.connect(host='localhost', user='root', password='12345', db='shopdb')
# 파이썬과 mysql간의 connection 생성

sql = "INSERT INTO membertbl VALUES ('WhiteCat2','김고양','인천 미추홀구')"  # DB에 실행할 SQL문 생성

cur = dbConn.cursor()
result = cur.execute(sql)  # 연결된 DB의 스키마에 지정된 SQL문이 실행됨
# insert, update, delete 문이 실행된 후 성공결과를 반환해줌->1이면 성공!!
if result == 1:
    print("회원 가입이 성공하였습니다!")

# records = cur.fetchall()  # sql문에서 실행된 select문의 결과를 records로 받음(튜플로 반환됨)


# dbConn 의 사용이 종료된 후에는 반드시 닫아줄 것!(close:cur먼저 닫고 dbConn을 닫아야 함)
cur.close()
dbConn.commit()  # insert, delete, update 문을 사용한 경우에는 반드시 commint 함수를 호출해야함!!!!!
dbConn.close()







