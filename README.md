Django를 이용한 사업 페이지 제작

# 개인 사업자를 위한 Business Site 제작
## 프로젝트 이름: K-TOUCH

### 제작 기간: 2022. 07 ~ 2022. 07

## 💡 Background

개인 Project 로 개발한 Business Site 입니다. 지인의 개인 사업을 위해 제작해본 사이트입니다.

이 프로젝트의 주요 기능으로는 로그인/회원가입과 서비스의 가격을 알아보고, 궁금한 점을 문의하고, 원하는 서비스를 선택하여 예약하는 기능 등이 있습니다.

## 🛠 Development

- Back-end

Django 와 Python 를 사용하여 백엔드 개발을 진행했습니다.

데이터베이스는 django의 기본 DB인 SQLite를 사용하지 않고, 다른 RDBMS 사용하기 위해서 MySQL을 연동하였습니다.

권한 설정을 위해 decorator를 이용하여 login_required라는 함수로 로그인한 사람만 가능할 수 있도록 하였습니다.

## Tech Stack

- HTML/CSS
- Bootstrap
- python
- Django
- MySQL

### Home

![1](https://user-images.githubusercontent.com/68835451/179647451-01e26f47-76c8-474f-96f6-0a70a69ac96f.jpg)

- 메인 페이지입니다.
- 지금 보시는 화면은 이미 로그인한 상태의 페이지로, 로그인하지 않았다면 밑의 화면을 보실 수 있습니다.

![2](https://user-images.githubusercontent.com/68835451/179647454-284b97e4-4fb4-4434-bbb4-18b0cc0c4b81.jpg)

### Register Page

![3](https://user-images.githubusercontent.com/68835451/179647456-d0844be6-caa7-4f60-ba3b-568069bd15cc.jpg)

- 회원 가입을 진행하는 페이지입니다.
- 이미 존재하고 있는 회원 정보라면 이미 아이디가 존재한다는 내용이 뜨도록 에러처리 해두었습니다.
- 비밀번호와 비밀번호 확인이 다르다면 회원가입할 수 없도록 하였습니다.

### Login Page

![4](https://user-images.githubusercontent.com/68835451/179647457-3454b92c-ef51-433d-8754-0fb110df1ca5.jpg)

- 로그인을 진행하는 페이지입니다.
- 존재하지 않는 회원 정보라면 아이디가 없다는 내용이 뜨도록 에러처리 해두었습니다.

### 문의 게시판

![5](https://user-images.githubusercontent.com/68835451/179647436-d540966f-3254-4432-80dc-aef4eed1f39e.jpg)

- 회원들의 문의를 조회할 수 있는 문의 게시판입니다.
- 모든 회원들의 문의를 조회할 수 있도록 하였으며 회원이 아니더라도 볼 수 있도록 권한을 설정하였습니다.
- Pagination을 하여 한 페이지에 15개의 문의가 보이도록 설정해두었습니다.

### 문의 세부 내용

![6](https://user-images.githubusercontent.com/68835451/179647442-88d9e65d-9b9c-4544-9f09-a557f8697503.jpg)

- 회원들의 문의를 세부하게 볼 수 있는 페이지입니다.
- 회원의 문의에 대한 답글을 달 수 있는 기능이 있습니다.
- 문의 세부 내용을 보기 위해서는 로그인을 해야만 하도록 권한 설정을 해두었습니다.
- 수정하기와 삭제하기는 글을 쓴 당사자일 경우에만 가능하도록 해두었으며 만약 다른 회원일 경우에는 밑의 화면처럼 버튼이 보이지 않도록 하였습니다.

![7](https://user-images.githubusercontent.com/68835451/179647443-3d21a85a-42a2-43ea-829a-db780d1ba59b.jpg)

### 문의하기 페이지

![8](https://user-images.githubusercontent.com/68835451/179647444-4ff1ae53-1c9f-4d2f-86f7-e22ea5edd7b4.jpg)

- 문의하기 페이지입니다.
- 이 페이지에서는 문의하고 싶은 유형과 문의 내용을 입력받습니다.
- 문의 유형은 Choice를 이용하였습니다
- 문의하기 페이지도 로그인한 회원만 가능하도록 권한 설정을 해두었습니다.

### 예약하기 페이지

![9](https://user-images.githubusercontent.com/68835451/179647446-044912f3-b240-4491-9bc6-369b6d24ca87.jpg)

- 예약하기 페이지입니다.
- 이 페이지에서는 예약하고 싶은 서비스와 예약 날짜를 입력받습니다.
- 예약 서비스는 Choice를 이용하였습니다
- 예약하기 페이지도 로그인한 회원만 가능하도록 권한 설정을 해두었습니다

### 마이 페이지

![10](https://user-images.githubusercontent.com/68835451/179647448-191005d6-2aba-4ebc-a6c8-8cf3c08f1ce9.jpg)

- 마이 페이지입니다.
- 마이 페이지에서는 회원이 한 문의들과 예약들을 조회할 수 있습니다.
- 마이 페이지에서 예약을 취소할 수 있습니다.
