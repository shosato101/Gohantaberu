import os

def write1( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0 

str1 = '''
<html>
<head>
<meta charset="utf-8">
<title></title>
</head>
<body>
<a href="http://webservice.recruit.co.jp/"><img src="http://webservice.recruit.co.jp/banner/hotpepper-s.gif" alt="ホットペッパー Webサービス" width="135" height="17" border="0" title="ホットペッパー Webサービス"></a> 
</body>
</html>
'''.format() 

print( str1 ) 

path1 = os.path.dirname(__file__) + "/" 
file1 = path1 + "html1.html" 
write1( file1, str1 ) 