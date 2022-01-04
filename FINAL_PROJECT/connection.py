import pyodbc


class connection:
    def __init__(self):
        try:
            self.__con = pyodbc.connect("driver={SQL Server}; Server=DESKTOP-F4VPPKQ\DAKSH; database=currencies; uid=sa; pwd=daksh")
            print("sucessful")
        except:
            print("not working")
            
dal = connection()

