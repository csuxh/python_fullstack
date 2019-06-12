#!/bin/bash
CHECK_NAME=`hostname`.csv
CHECK_REPORT_PATH=/tmp/nari
ls -d $CHECK_REPORT_PATH
if [ $? -gt 0 ]
then
    mkdir $CHECK_REPORT_PATH
fi
chmod -R 777 $CHECK_REPORT_PATH
a="版本信息检查"
b=`cat /etc/redhat-release|awk '{print $7}'`
c=6.5
if [ `echo "$b < $c|bc" ` ];
then
    echo "$a,`cat /etc/redhat-release`,$c,合格" >>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
    echo "$a,`cat /etc/redhat-release`,$c,不合格" >>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="主机名信息"
echo "$a,`hostname`,,,">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
a="DNS信息"
b=`cat /etc/resolv.conf |grep -v ^#|grep nameserver`
c=`cat /etc/sysconfig/network-scripts/ifcfg-* |grep -v ^# |grep DNS|grep [0-9].[0-9].[0-9].[0-9]`
if [ "$b"="" -a "$c"="" ];
then
    echo "$a,$b $c, ,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
    echo "$a,$b $c, ,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="IP地址信息"
b=`ifconfig |grep -w inet|awk '{gsub(/addr/,"ip")}{print $2}'|xargs`
echo "$a,$b,,,">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
a="系统时区信息"
b=`cat /etc/sysconfig/clock |grep ZONE`
c='ZONE="Asia/Shanghai"'
if [ "$b" == "$c" ];
then
    echo  "$a,$b,$c,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
    echo  "$a,$b,$c,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="系统时区信息"
b=`date |awk '{print $5}'`
c="CST"
if [ "$b" == "$c" ];
then
    echo  "$a,$b,$c,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
    echo  "$a,$b,$c,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="内存信息"
b=`cat /proc/meminfo |grep MemTotal|awk '{print $2/1024/1024 "GB"}'`
echo "$a,$b,,,">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
a="swap信息"
b=`free -m|grep Swap|awk '{print $2/1024 "GB"}'`
echo "$a,$b,,,">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
a="ntp信息"
echo "$a,`cat /etc/ntp.conf |grep -v ^#|grep server|xargs`,,,">>$CHECK_REPORT_PATH/Check_$CHECK_NAME

a="文件系统信息"
for i in / /boot /var /tmp
do
Type=`df -Th |grep -w $i|awk '{print $2}'`
if [ "$Type" != "ext4" ];
then
echo "$i,$Type,EXT4,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$i,$Type,EXT4,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
done

a="口令策略信息"
b=`cat /etc/login.defs |grep -v ^#|grep PASS_MAX_DAYS|awk '{print $2}'`
if [ $b -eq 90 ];
then
echo "$a,`cat /etc/login.defs |grep -v ^#|grep PASS_MAX_DAYS`,90,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$a,`cat /etc/login.defs |grep -v ^#|grep PASS_MAX_DAYS`,90,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="口令策略信息"
b=`cat /etc/login.defs |grep -v ^#|grep PASS_WARN_AGE|awk '{print $2}'`
if [ $b -eq 7 ];
then
echo "$a,`cat /etc/login.defs |grep -v ^#|grep PASS_WARN_AGE`,7,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$a,`cat /etc/login.defs |grep -v ^#|grep PASS_WARN_AGE`,7,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="口令策略信息"
b=`cat /etc/login.defs |grep -v ^#|grep PASS_MIN_LEN|awk '{print $2}'`
if [ $b -gt 8 ];
then
echo "$a,`cat /etc/login.defs |grep -v ^#|grep PASS_MIN_LEN`,8,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$a,`cat /etc/login.defs |grep -v ^#|grep PASS_MIN_LEN`,8,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="非root的超级用户信息"
b=`cat /etc/passwd |grep -v ^#|grep -v root|awk -F : '{print $3}'|grep -w 0`
if [ $? -eq 0 ];
then
echo "$a,`cat /etc/passwd |grep -v ^#|grep -v root|awk -F : '{print $1}'|grep -w 0`,存在非root的超级用户,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$a,,不存在非root的超级用户,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="selinux 信息"
b=`cat /etc/selinux/config |grep -v ^#|awk -F = '{print $1,$2}'|grep -w SELINUX|awk '{print $2}'`
if [ "$b" == "disabled" ];
then
echo "$a,$b,disabled,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$a,$b,disabled,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="网卡数量"
b=`lspci | grep Ethernet|wc -l`
if [ "$b" -lt 4 ];
then
echo "$a,$b,4,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$a,$b,4,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="网卡速率"
b=`ls /etc/sysconfig/network-scripts/ifcfg-eth*|awk -F - '{print $3}'`
for i in $b
do
c=`ethtool $i|grep Speed|awk '{print $2}'`
d=`ethtool $i|grep Speed|awk -F : '{gsub (/Mb\/s/,"")} {print int($2)}'`
if [ "$d" -lt 1000 ];
then
echo "$a,$i $c,1000Mb/s,不合格,">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
echo "$a,$i $c,1000Mb/s,合格,">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
done
a="检查禁用服务信息"
for i in ip6tables iptables Bluetooth postfix cups NetworkManager vsftpd dhcpd
do
    chkconfig --list|grep $i|awk '{print $5}'|grep on >>/dev/null
    if [ $? -ne 0 ];
    then
        echo "$i,`chkconfig --list|grep $i|awk '{print $5}'`, 已禁用,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
    else
        echo "$i,`chkconfig --list|grep $i|awk '{print $5}'`, 未禁用,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
    fi
done
a="检查启用服务信息"
for i in sshd ntpd ntpdate cman clvmd rgmanager ricci luci
do
    chkconfig --list|grep $i|awk '{print $5}'|grep off  >>/dev/null
    if [ $? -ne 0 ];
    then
        echo "$i,`chkconfig --list|grep -w $i|awk '{print $5}'`, 未禁用,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
    else
        echo "$i,`chkconfig --list|grep -w $i|awk '{print $5}'`, 已禁用,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
    fi
done
a="SNMP信息检查"
b=`ps -ef |grep snmp|grep -v grep`
c=`cat /etc/snmp/snmpd.conf|grep -v ^#|grep strongpass`
if [ -z "$b"  ];
then
    echo "$a,未启用,未启用,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
elif [ -z "$c" ];
then
    echo "$a,,未修改,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
    echo "$a,启用,已修改,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi
a="密码为空的用户"
for i in `cat /etc/passwd |grep /bin/bash|awk -F : '{print $1}'`
do
    for j in `awk -F: 'length($2)==2 {print $1}' /etc/shadow`
    do
        if [ "$i" == "$j" ];
        then
            echo "$a,$i,"密码为空",不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
        else
            echo "  ">>/dev/null
        fi
    done
done
a="ctrl+alt+del信息"
b=`cat /etc/init/control-alt-delete.conf|grep -v ^#|grep control-alt-delete`
if [ $? -eq 0 ];
then
    echo "$a,$b,未禁用,不合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
else
    echo "$a,$b,已禁用,合格">>$CHECK_REPORT_PATH/Check_$CHECK_NAME
fi

a="日志信息检查"
b=`cat /etc/rsyslog.conf |grep ^authpriv`
if [ $? == 0 ];
then
    echo "$a,The authpriv file has restricted access,authpriv,合格"
else
    echo "$a,there don't have authpriv set in /etc/syslog.conf,authpriv,不合格"
fi

a="日志信息检查"
b=`cat /etc/rsyslog.conf |grep ^cron`
if [ $? == 0 ];
then
    echo "$a,Log cron stuff,cron,合格"
else
    echo "$a,there don't have cron set in /etc/syslog.conf,cron,不合格"
fi