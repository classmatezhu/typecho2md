for file in `find . | egrep 'md$' | tr ' ' '\?'`
do
    echo $file
    for i in $(egrep '\[\w\]: https://www.bodkin' "$file" | sed 's/\[/\//g' | sed 's/\]/\//g' | awk -F '/' '{print $2"-"$NF}')
    do
        echo $i
        declare -i var_id=`echo $i | awk -F '-' '{print $1}'`
        echo var_id
        var_src=`echo $i | awk -F '-' '{print $2}'`
        echo $var_src
    done
done