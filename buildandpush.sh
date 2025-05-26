docker build -t debankurs/sagemakerimages .
docker tag debankurs/sagemakerimages:latest 531181936590.dkr.ecr.ap-south-1.amazonaws.com/debankurs/sagemakerimages:latest
docker push 531181936590.dkr.ecr.ap-south-1.amazonaws.com/debankurs/sagemakerimages:latest