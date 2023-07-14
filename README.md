# SKT_Docker

## 직접 빌드 및 실행 명령어


docker build -t generator-app -f Dockerfile.generator .

docker build -t calculator-app -f Dockerfile.calculator .

docker run -it -v "C:\Users\064\Desktop\HW2:/app" generator-app

docker run -it -v "C:\Users\064\Desktop\HW2:/app" -p 5000:5000 calculator-app

curl -X POST http://localhost:5000/calculate/%


## git hook 명령어


git add .

git commit -m "fourth commit"

docker run -it -v "C:\Users\064\Desktop\HW2:/app" generator-app

docker run -it -v "C:\Users\064\Desktop\HW2:/app" -p 5000:5000 calculator-app

- calculator_test.py를 통해서 2개의 수를 입력해서 반환값이 올바른지 비교함.


## github actions

- commit 발생시 도커 이미지 빌드후 도커 허브에 배포 자동화.
