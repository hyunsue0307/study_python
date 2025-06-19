#  github 프로젝트 폴더 가상환경&필요 모튤 설치방법

1. 프로젝트 폴더 만들기 (1회)
- mkcdir '폴더'
- cd '폴더'

2. 가상환경 만들기 (1회)
- python3 -m venv .venv

3. 가상환경 활성
- source .venv/venv/bin/activate
>> (venv) or (.venv)

4. 필요한 모듈 설정
- ex) pip install pandas matplotlib numpy

5. 파이썬 파일 실행
- python 파일이름.py or ./.venv/bin/python 파일이름.py
