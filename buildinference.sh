docker build -f Dockerfileinference -t debankurs/xgbinference .
docker tag debankurs/xgbinference:latest 531181936590.dkr.ecr.ap-south-1.amazonaws.com/debankurs/xgbinference:latest
docker push 531181936590.dkr.ecr.ap-south-1.amazonaws.com/debankurs/xgbinference:latest