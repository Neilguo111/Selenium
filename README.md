# Selenium
learn selenium
YAML 基本语法：
  1、大小写敏感
  2、使用缩进表示层级关系
  3、禁止使用tab缩进，只能使用空格键
  4、缩进长度没有限制，只要元素对齐就表示这些元素属于一个层级。
  5、使用#表示注释
  6、字符串可以不用引号标注
三种数据结构：
  1. map散列表 使用冒号（：）表示键值对，同一缩进的所有键值对属于一个map
示例： 
YAML格式：                                     Json格式:
age:23                                            {"age":23,"name":"Neilguo"}
name:Neilguo  或  {age:12,name:huang}
  2.list，数组  使用连字符（-）表示
示例：
YAML格式：                                     Json格式：
-a                                                 ["a","b",12]
-b
-12   或[a,b,12]
  3. scalar，纯量  数据最小的单位，不可以再分割。
数据结构嵌套：
  1. map嵌套map
示例:
YAML格式：                                     Json格式:
websites:                                           {"websites":
 YAML:yaml.org                                                {"YAML":"yaml.org"
 Ruby: ruby-lang.org                                           "Ruby":"ruby-lang.org"
 Python: python.org                                            "Python":"python.org"
 Perl: use.perl.org                                            "Perl":"use.perl.org"}}
  2. map嵌套list
 示例:
 YAML表示:                                     Json格式:
-                                                      [["Yaml","Ruby","Python","Perl"],["c","c#","java"]]   
 -Yaml
 -Ruby              或 --Yaml    或    -[Ruby,Perl,Python]
 -Python                -Ruby         -[c,c#,java]
 -Perl                  -Python
-                       -Perl
 -c                    --c
 -c#                    -c# 
 -java                  -java
  3.list嵌套map
示例：
YAML格式：                                      Json格式：
-                                                 [{"id":1,"name":"Neilguo"},{"id":2,"name":"python"}]
 id:1
 name:Neilguo
-
 id:2
 name:Python
