
import  pyhdfs


fs = pyhdfs.HdfsClient(hosts="10.18.134.94:9870",user_name="hadoop")
print(fs.get_home_directory())

fs.copy_from_local("/home/zhangcheng/桌面/shangchuan.docx","/user/hadoop/shangchuan.docx")
fs.copy_to_local("/user/hadoop/shangchuan.docx","/home/zhangcheng/桌面")

print(fs.listdir("/user/hadoop"))