apt-get install docker-ce=5:23.0.1-1~debian.11~bullseye docker-ce-cli=5:23.0.1-1~debian.11~bullseye containerd.io

HubsSidebarEnabled

vim /etc/profile



3d3f5b7b0582a4a9bd512891f050892cb9e084c6ed76fd7f87a5a5f6c5ac4db6

# docker update --restart=always 容器名或容器ID
docker update --restart=always <CONTAINER ID>
# 例如将tomcat设为自启动
docker update --restart=always tomcat

# docker update --restart=no 容器名或容器ID
docker update --restart=no 3d3f5b7b0582a4a9bd512891f050892cb9e084c6ed76fd7f87a5a5f6c5ac4db6
# 例如取消tomcat的自启动
docker update --restart=no 3d3f5b7b0582a4a9bd512891f050892cb9e084c6ed76fd7f87a5a5f6c5ac4db6

docker update --restart=no $(docker ps -q)



export http_proxy=127.0.0.1:7890
export https_proxy=127.0.0.1:7890

source /etc/profile

docker run -d --name clash-client --restart always -p 7890:7890 -p 7891:7891 -p 9090:9090 -v /root/.config/clash/config.yaml:/root/.config/clash/config.yaml -v /root/clash/dashboard:/root/clash/dashboard dreamacro/clash


sudo nmtui

docker run -dit \
  --name QingLong \
  --hostname QingLong \
  --restart always \
  -p 5700:5700 \
  -v /data/docker/QingLong/config:/ql/config \
  -v /data/docker/QingLong/log:/ql/log \
  -v /data/docker/QingLong/db:/ql/db \
  -v /data/docker/QingLong/scripts:/ql/scripts \
  -v /data/docker/QingLong/jbot:/ql/jbot \
  whyour/qinglong:latest



wpa_passphrase 3232 1234567890 >> /etc/wpa.conf


apt-get install ifupdown



iwconfig wlan0 scan | grep SSID

$ nmcli dev wifi connect 3232 password 1234567890 	#连接wifi(密码含有空格则用引号括起)
nmcli dev wifi connect 6262 password 62626262

nmcli dev wifi connect 疾风拂地之时随风而起 password 

nmcli dev wifi




tmux new -s  pup


tmux ls



# 返回最近的一个进程
tmux a 
#-t: 当有多个会话时，使用会话编号或名称接入会话
tmux a -t 0
tmux a -t <session-name>

tmux ls

bash <(curl -L gitee.com/TimeRainStarSky/TRSS_Shell/raw/main/SWAP.sh)


DIR=/tf/bot CMD=trss DKNAME=TRSS bash <(curl -L gitee.com/TimeRainStarSky/TRSS_AllBot/raw/main/Install-Docker.sh)


DIR=/home/bot CMD=trss DKNAME=TRSS bash <(curl -L gitee.com/TimeRainStarSky/TRSS_AllBot/raw/main/Install-Docker.sh)

install-portainer.sh
install-qinglong.sh

mount -t vfat /dev/mmcblk1 /mnt/tf
umount /dev/mmcblk1
fdisk -l


mount /dev/mmcblk1 /mnt/tf
mkfs.ext4 /dev/mmcblk1
sudo vim /etc/fstab


recoverbackup


#将docker安装目录移动到/opt/docker
mv /opt/docker /tf/docker
#创建软连接
ln -s /tf/docker /opt/docker
#最后启动docker
systemctl start docker

systemctl stop docker
systemctl stop docker.socket

chattr -i /opt/docker/*


ln -s /mnt/tf/swap /swap

lsattr swap

chattr -i swap

rm -rf swap

dd if=/home/ubuntu/backup-64 of=/dev/mmcblk1

首先先通过blkid查看一下磁盘的信息
命令截图在此

root@hi3798model:~# blkid
/dev/mmcblk0p7: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/mmcblk0p8: UUID="57f8f4bc-abf4-655f-bf67-946fc0f9f25b" TYPE="ext4"
/dev/mmcblk0p9: UUID="8b5b1a45-3487-4b05-a446-ec9e3fa5d1ed" TYPE="ext4"
/dev/sda: UUID="8b5b1a45-3487-4b05-a446-ec9e3fa5d1ed" TYPE="ext4"

/dev/mmcblk0p8中取出backup.gz文件拷贝到你的现有系统目录
先创建一个要挂载的分区
mkdir /mnt/mm8

然后挂载分区

mount /dev/mmcblk0p8 /mnt/mm8

拷贝backup.gz到你的系统任意分区

cp /mnt/mm8/backup.gz /home/ubuntu

然后用gunzip解压backup.gz文件

cd /home/ubuntu

gunzip backup.gz

用命令写入挂载的u盘内

dd if=/home/ubuntu/backup-64 of=/dev/mmcblk1

最后执行resize2fs一下

resize2fs /dev/mmcblk1

在海思的HiTool工具内链接ttl终端 重新接入电源 一直按ctrl+c进入fastboot模式

执行printenv看一下参数

然后执行如下操作

setenv bootargs 'bootargs=model=mv200 console=ttyAMA0,115200 root=/dev/mmcblk1 rootfstype=ext4 rootwait blkdevparts=mmcblk0:1M(boot),1M(bootargs),4M(baseparam),4M(pqparam),4M(logo),40M(kernel),64M(busybox),512M(backup),-(ubuntu)'

主要是这一句root=/dev/mmcblk1

最后再执行

saveenv

断电再开机 收工

PS：在此感谢神雕大神的指导