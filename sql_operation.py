import mysql.connector #pip install mysql.connector 


class My_sql:
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'fci')

    def showTable(self):
        cur = self.db.cursor()
        formula = "SHOW TABLES"
        cur.execute(formula)
        r = cur.fetchall()
        for i in r:
            print(r)
 

    def insertdata(self,id , name, pas, bod, country, email):
        'id: give empty value ='', name:..., pas:..., bod:..., country:..., email:..., '
        self.id = id
        self.name = name 
        self.pas = pas
        self.bod = bod
        self.country = country
        self.email = email
        cur = self.db.cursor()
        formula = "INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s)"
        vlaue = (id,name, pas, bod, country, email)
        cur.execute(formula, vlaue)
        self.db.commit()

    def viewall(self):
        cur = self.db.cursor()
        formula = "SELECT* FROM student"
        cur.execute(formula)
        r = cur.fetchall()
        for i in r:
            print(i)

    def validation(self, id):
            self.id = id
            cur = self.db.cursor()
            formula = "SELECT* FROM student WHERE id = %s"
            value= (id,)
            cur.execute(formula, value)
            r = cur.fetchall()
            if not r:
                return False
            else:
                return True
    def viewone(self, id):
        'input Id as refrence'
        self.name = id
        cur = self.db.cursor()
        formula = "SELECT* FROM student WHERE id = %s"
        value = (id,)
        cur.execute(formula, value)
        r = cur.fetchall()
        if not r:
            print('404 error \nNo information found')
        else:
            for i in r:
                print(i)

            

    def update(self, id):
        
        self.name = id
        cur = self.db.cursor()
    
        v = self.validation(id)
        if v:
            self.viewone(id)
            i = int(input('''1 to update name:\n2 to update pas:\n3 to update bod:\n4 to update country:\n5 to update email:\n: '''))
            if i == 1:
                u_name = input('Enter your new name: ')
                formula ="UPDATE student SET NAME = %s WHERE id = %s "
                value = (u_name, id)
                cur.execute(formula, value)
                self.db.commit()
                self.viewone(id)

            elif i == 2:
                u_pass = input('Enter your new pass: ')
                formula ="UPDATE student SET PAS = %s WHERE id = %s "
                value = (u_pass, id)
                cur.execute(formula, value)
                self.db.commit()
                self.viewone(id)

            elif i == 3:
                u_bod = input('Enter your new bod: ')
                cur = self.db.cursor()
                formula = "UPDATE student SET BOD = %s WHERE id = %s"
                value = (u_bod, id)
                cur.execute(formula, value)
                self.db.commit()
                self.viewone(id)  

            elif i == 4:
                u_country = input('Enter your new Country: ')
                cur = self.db.cursor()
                formula = "UPDATE student SET COUNTRY = %s WHERE id = %s"
                value = (u_country, id)
                cur.execute(formula, value)
                self.db.commit()
                self.viewone(id) 

            elif i == 5:
                u_email = input('Enter your new Email: ')
                cur = self.db.cursor()
                formula = "UPDATE student SET EMAIL = %s WHERE id = %s"
                value = (u_email, id)
                cur.execute(formula, value)
                self.db.commit()
                self.viewone(id)
                    
            else:
                print('Invalid Choice')
        else:
            print('No Data Found')
            
            
            
            

    def delete(self, id):
        self.id= id 
        cur = self.db.cursor()
        worning = input(f'Your id is = {id}, DO You Want To Delete All Data: (Y/N)\t').lower()
        if worning == 'y':
            formula = "DELETE FROM student WHERE id = %s"
            value= (id,)
            cur.execute(formula, value)
            self.db.commit()
            print('Your data successfully deleted..')
        elif worning == 'n':
            print("Thank You...")
        else:
            print('Invalid Choice')


obj = My_sql()
obj.update(12)



