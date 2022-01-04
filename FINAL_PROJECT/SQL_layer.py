import pyodbc

from compoCurren import Product

class SQLLayer:
    def __init__(self):
        self.__con = pyodbc.connect("driver={SQL Server}; Server=DESKTOP-F4VPPKQ\DAKSH; database=currencies; uid=sa; pwd=daksh")


    def __del__(self):
        if self.__con!= None:
            self.__con.close()
            self.__con = None


    def get_products(self):
            allproducts = []

            cur = self.__con.cursor()
            cur.execute("Select * from world_cur")
            records = cur.fetchall()

            for record in records:
                pro = Product()
                pro.S_no = record[0]
                pro.Currencies_Name = record[1]
                pro.Date = record[2]
                pro.Price_USD = record[3]

                allproducts.append(pro)

            return allproducts


    def additem(self,pro):
        ret = False
        cur = self.__con.cursor()
        

        try :
            query = "Insert into world_cur values(?,?,?)"
            row = (pro.Currencies_Name ,pro.Date, pro.Price_USD)

            cur.execute(query,row)
            self.__con.commit()
            
            print('sucess')
            ret = True
            
        except:
            cur.rollback()

        return ret


    
    def delitem(self,pid):
        ret = False
        try:
            cur = self.__con.cursor()

            query = "Delete from world_cur where S_no=?"
            row = (pid)
            cur.execute(query,row)

            self.__con.commit()
            ret = True

        except:
            self.__con.rollback()            

        return ret

    
            
                