import pymysql
#conn = pymysql.connect('localhost','root','','pytest')
#print(conn)
def insert_data(nm,ro,fe):
	try:
		conn = pymysql.connect(user='root',password='',host='localhost',database='pytest',port=3306)
		print('Connected')
	except:
		print('Unable to Connect')

	myc = conn.cursor()

	sl = "INSERT INTO student(name,roll,fees) VALUES(%s,%s,%s)"
	val = (nm,ro,fe)
	myc.execute(sl,val)
	conn.commit()
	print("Row No.",myc.rowcount)
	#print(myc.lastrowid)
	myc.close()
	conn.close()

while True:
	nm = input('Enter Name:')
	ro = int(input('Enter Roll No.:'))
	fe = int(input('Enter Fees:'))
	insert_data(nm,ro,fe)

	ans = input('So You Want to exit (Y/N):')
	if (ans=='y'):
		break