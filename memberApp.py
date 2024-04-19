import sys
import pymysql

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/member.ui")[0]  # 미리 제작해 놓은 ui 불러오기

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원 관리 프로그램")

        self.join_btn.clicked.connect(self.member_join)  # 회원가입이 버튼이 클릭되면 가입함수 호출
        self.joinreset_btn.clicked.connect(self.join_reset)  # 초기화 버튼이 클릭되면 입력내용 초기화


    def member_join(self):  # 회원 가입 이벤트 처리 함수
        memberid = self.joinid_edit.text()  # 유저가 입력한 회원아이디 텍스트 가져오기
        memberpw = self.joinpw_edit.text()  # 유저가 입력한 회원비밀번호 텍스트 가져오기
        membername = self.joinname_edit.text()  # 유저가 입력한 회원이름 텍스트 가져오기
        memberemail = self.joinemail_edit.text()  # 유저가 입력한 회원이메일 텍스트 가져오기
        memberage = self.joinage_edit.text()  # 유저가 입력한 회원나이 텍스트 가져오기

        if memberid == "" or memberpw == "" or membername == "" or memberemail == "" or memberage == "":
            QMessageBox.warning(self, "정보입력오류", "입력 정보 중 한개라도 누락되면 회원가입이 되지 않습니다.\n다시 입력해주세요.")
        elif len(memberid) < 4 or len(memberid) >= 15:
            QMessageBox.warning(self, "아이디길이오류", "아이디는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요.")
        elif len(memberpw) < 4 or len(memberpw) >= 15:
            QMessageBox.warning(self, "비밀번호길이오류", "비밀번호는 4자 이상 14자 이하이어야 합니다.\n다시 입력해주세요.")
        else:
            dbConn = pymysql.connect(user="root", password="12345", host="localhost", db="shopdb")

            sql = f"INSERT INTO appmember VALUES('{memberid}','{memberpw}','{membername}','{memberemail}','{memberage}')"

            cur = dbConn.cursor()
            result = cur.execute(sql)  # 회원가입하는 sql문이 성공하면 1이 반환

            if result == 1:
                QMessageBox.warning(self, "회원가입성공","축하합니다.\n회원가입이 성공하셨습니다.")
                self.join_reset()  # 회원가입 성공 ok 클릭 후 입력내용 초기화
            else:
                QMessageBox.warning(self, "회원가입실패", "회원가입이 실패하셨습니다.")
            cur.close()
            dbConn.commit()
            dbConn.close()

    def join_reset(self):  # 회원가입정보 입력내용 초기화
        self.joinid_edit.clear()
        self.joinpw_edit.clear()
        self.joinname_edit.clear()
        self.joinemail_edit.clear()
        self.joinage_edit.clear()



app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())