while read LINE
do
	pwd_time=$(echo $LINE | awk -F '#' '{print $1}')
	echo "pwd_time:"$pwd_time
	mkdir $pwd_time
	url=$(echo $LINE | awk -F '#' '{print $2}')
	echo "url:"$url
	file=${url:43}
	echo "file:"$file
	pwd=${pwd_time}"/"${file}
	echo "pwd:"$pwd
	wget -O $pwd $url
done  < hh