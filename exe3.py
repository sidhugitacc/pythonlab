def decode(stringsplit):
 str = stringsplit.split('_')


 str = [str.strip() for str in str if str.strip()]
 dict={
  
  "name": str[0],
  "Domain_name": str[1],
  "Regno": str[2]
 }
 return dict
encode="sidharth__Automobile__2347257"
dict = decode(encode)
print(dict)