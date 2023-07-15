# SKT_Docker

## 프로그램 소개

- generator.py : 0 ~ 1000 사이 숫자 두개를 중복을 허용해서 추출하고 result 폴더의 input.txt에 저장하고 종료.
  
- calculator.py : flask로 구성된 백엔드 서버. result 폴더에 존재하는 input.txt에 존재하는 숫자 두개를 읽어들인후 uri를 통해서 Operator를 전달받아서 연산된 결과를 반환한다.(+: 덧샘, -: 뺄샘, *: 곱샘, %: 나눗샘의 몫 )
  
- calculator_test.py : 총 5개의 테스트 케이스가 주어진다. 미리 설정된 두개의 숫자의 연산결과가 옳을 경우 통과를 한다. 


## 직접 빌드 및 실행 명령어


docker build -t generator-app -f Dockerfile.generator .

docker build -t calculator-app -f Dockerfile.calculator .

docker run -it -v "C:\Users\064\Desktop\HW2:/app" generator-app

docker run -it -v "C:\Users\064\Desktop\HW2:/app" -p 5000:5000 calculator-app

curl -X POST http://localhost:5000/calculate/%

- "C:\Users\064\Desktop\HW2:/app" 에서 C:\Users\064\Desktop\HW2 해당 부분은 사용자의 깃 클론 파일이 존재하는 디렉토리로 변환

## git hook 명령어


git add .

git commit -m "first commit"

docker run -it -v "C:\Users\064\Desktop\HW2:/app" generator-app

docker run -it -v "C:\Users\064\Desktop\HW2:/app" -p 5000:5000 calculator-app

- calculator_test.py를 통해서 2개의 수를 입력해서 반환값이 올바른지 비교함.
  
- "C:\Users\064\Desktop\HW2:/app" 에서 C:\Users\064\Desktop\HW2 해당 부분은 사용자의 깃 클론 파일이 존재하는 디렉토리로 변환


## github actions

- commit 발생시 도커 이미지 빌드후 도커 허브에 배포 자동화.

## Docker Swarm

docker service create --name calculator-app --replicas 3 --publish published=5000,target=5000 calculator-app
