## 简介

**typecho2md**是一款将Typecho Pages格式导出为Markdown格式的python脚本；

**dlsrc**是将Page中的src资源使用wget工具下载到指定目录的shell脚本；

**srcinfo**是获取Page中的src资源id及url的shell脚本。

## 用法

修改typecho2md.py文件中的mysql链接配置，脚本基于Python3；

```
python3 typecho2md.py
```

dlsrc.sh需要的hh文件生成；

```
egrep '\[\w*\]: https://www.bodkin' -r . | sed 's/\.\///g' | sed 's/]: /-/g' | awk -F '-' '{print $1"-"$2"-"$3"#"$NF}' | tr -d '\r'  > hh
```

## 参考

[https://www.npmjs.com/package/typecho-to-md](https://www.npmjs.com/package/typecho-to-md)