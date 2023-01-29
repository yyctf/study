apt-get update 
apt-get install -y apt-transport-https ca-certificates 
apt install docker.io 
docker -v 
systemctl start docker 
docker ps -a 
apt-get install python3-pip 
pip3 install docker-compose 
docker-compose -v
- 克隆仓库
git clone https://github.com/vulhub/vulhub.git 
- 进入目录
cd /vulhub/flask/ssti
- 启动环境 
docker-compose build //可选 
docker-compose up -d 
- 查看端口
docker-compose ps 
-  移除环境
docker-compose down 