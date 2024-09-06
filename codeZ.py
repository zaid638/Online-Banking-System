import datetime
class Account:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,ac_no):
        self.ac_no = ac_no
        self.amount = float(input("Enter The Amount To Deposit: "))
        self.balance += self.amount
        for j in self.ac_lst:
            if j[0] == self.ac_no:
                j[1] = self.balance
                j.append(f"Deposit {self.amount}")
        f7 = open("Accounts.csv","w")
        for k in self.ac_lst:
            for l in range(len(k)):
                if l == (len(k)-1):
                    f7.write(f"{k[l]}")
                else:
                    f7.write(f"{k[l]},")            
            f7.write("\n")
        f7.close()
        Account.account_lists(self)
        
    def withdraw(self,ac_no):
        self.ac_no = ac_no       
        self.w_amount = float(input("Enter The Amount To withdraw: "))
        if self.balance >= self.w_amount:
            self.balance -= self.w_amount           
            for k in self.ac_lst:
                if k[0] == self.ac_no:
                    k[1] = self.balance
                    k.append(f"Withdraw {self.w_amount}")
            f9 = open("Accounts.csv","w")
            for l in self.ac_lst:
                for m in range(len(l)):
                    if m == (len(l)-1):
                        f9.write(f"{l[m]}")
                    else:
                        f9.write(f"{l[m]},")            
                f9.write("\n")
            f9.close()
            Account.account_lists(self)

        else:
            print("Insufficient balance")
            
    def transfer(self,ac_no):
        self.ac_no = ac_no       
        self.sender = input("Enter The Sender Account No: ")
        if self.sender in self.lac:
            self.s_amount = float(input("Enter The Amount To Send: "))
            if self.balance >= self.s_amount:
                self.balance -= self.s_amount           
                for n in self.ac_lst:
                    if n[0] == self.ac_no:
                        n[1] = self.balance
                        n.append(f"Transfered {self.s_amount} To {self.sender}")
                    if n[0] == self.sender:
                        n[1] = float(n[1])+self.s_amount
                        n.append(f"Transfered {self.s_amount} From {self.ac_no}")                        
                        print(f"Successfully Transfered {self.s_amount} To {n[0]}")
                f10 = open("Accounts.csv","w")
                for o in self.ac_lst:
                    for p in range(len(o)):
                        if p == (len(o)-1):
                            f10.write(f"{o[p]}")
                        else:
                            f10.write(f"{o[p]},")            
                    f10.write("\n")
                f10.close()                
                Account.account_lists(self)
                                
            else:
                print("Insufficient balance")
                
        else:
            print("Enter Correct Account Number!")
            
    def account_lists(self):
        self.lac = []        
        self.ac_lst = []
        f5 = open("Accounts.csv","r")
        f5.seek(0)
        for i in f5:
            a = i.strip()
            b = a.split(",")
            self.ac_lst.append(b)
            self.lac.append(b[0])            
        f5.close()

    def balance_enquiry(self):
        print("Your Current Balance is Rs.",self.balance) 



class CheckingAccount(Account):
    def __init__(self, balance, ac_no, credit_limit=5000):
        self.balance = balance
        self.ac_no = ac_no
        self.credit_limit = credit_limit            

    def withdraw(self):
        self.cw_amount = float(input("Enter The Amount To withdraw: "))
        if self.balance + self.credit_limit >= self.cw_amount:
            if self.balance >= self.cw_amount:
                self.balance -= self.cw_amount
            else:
                self.balance -= self.cw_amount
                self.balance -= 500 #overdraft fee
            account3 = Account()
            account3.account_lists()
            for i in account3.ac_lst:
                if i[0] == self.ac_no:
                    i[1] = self.balance
                    if self.balance >= self.cw_amount:
                        i.append(f"Withdraw {self.cw_amount}")
                    else:
                        i.append(f"Withdraw {self.cw_amount}+overdraft fee 500")
            f11 = open("Accounts.csv","w")
            for l in account3.ac_lst:
                for m in range(len(l)):
                    if m == (len(l)-1):
                        f11.write(f"{l[m]}")
                    else:
                        f11.write(f"{l[m]},")            
                f11.write("\n")
            f11.close()
            Account.account_lists(self)
            
        else:
            print("Insufficient balance")


class SavingAccount(Account):
    def __init__(self,ac_no,interest_rate=0.05):
        self.ac_no = ac_no
        self.interest_rate = interest_rate
 
    def add_interest(self,balance,ac_no):
        self.balance = float(balance)
        self.ac_no = ac_no
        self.monthly_interest = float(self.balance)*(float(self.interest_rate)/12)
        self.balance += self.monthly_interest
        account_2 = Account()
        account_2.account_lists()
        for j in account_2.ac_lst:
            if j[0] == self.ac_no:
                j[1] = self.balance
                j.append(f"Interest {self.monthly_interest}")
        f12 = open("Accounts.csv","w")
        for k in account_2.ac_lst:
            for l in range(len(k)):
                if l == (len(k)-1):
                    f12.write(f"{k[l]}")
                else:
                    f12.write(f"{k[l]},")            
            f12.write("\n")
        f12.close()
        Account.account_lists(self)

        
class LoanAccount(Account):
    def __init__(self, principal=0, interest_rate=0.05, duration=12):
        self.principal = principal
        self.interest_rate = interest_rate
        self.duration = duration

    def get_loan(self,ac_no):
        self.ac_no = ac_no
        self.p_amount = float(input("Enter Amount:"))
        self.principal += self.p_amount
        account2 = Account()
        account2.account_lists()
        for j in account2.ac_lst:
            if j[0] == self.ac_no:
                j[1] = self.principal
                j.append(f"Loan {self.p_amount}")
        f15 = open("Accounts.csv","w")
        for k in account2.ac_lst:
            for l in range(len(k)):
                if l == (len(k)-1):
                    f15.write(f"{k[l]}")
                else:
                    f15.write(f"{k[l]},")            
            f15.write("\n")
        f15.close()
        Account.account_lists(self)        

    def pay_loan(self,ac_no):
        self.ac_no = ac_no
        self.pay_amount = float(input("Enter Amount:"))
        self.principal -= self.pay_amount
        account3 = Account()
        account3.account_lists()
        for j in account3.ac_lst:
            if j[0] == self.ac_no:
                j[1] = self.principal
                j.append(f"Payed {self.pay_amount}")
        f16 = open("Accounts.csv","w")
        for k in account3.ac_lst:
            for l in range(len(k)):
                if l == (len(k)-1):
                    f16.write(f"{k[l]}")
                else:
                    f16.write(f"{k[l]},")            
            f16.write("\n")
        f16.close()
        Account.account_lists(self)        
        
    def monthly_interest(self,ac_no):
        self.ac_no = ac_no
        self.month_interest = self.principal * (self.interest_rate) / (self.duration)
        self.principal += self.month_interest
        account_5 = Account()
        account_5.account_lists()
        for j in account_5.ac_lst:
            if j[0] == self.ac_no:
                j[1] = self.principal
                j.append(f"Interest {self.month_interest}")
        f19 = open("Accounts.csv","w")
        for k in account_5.ac_lst:
            for l in range(len(k)):
                if l == (len(k)-1):
                    f19.write(f"{k[l]}")
                else:
                    f19.write(f"{k[l]},")            
            f19.write("\n")
        f19.close()
        Account.account_lists(self)
                              

class Customer:
    f1 = open("Customer_Details.csv","r")
    f1.seek(0)
    f1.readline()
    for i in f1:
        a = i.strip()
        b = a.split(",")
    count = int(b[0])
    f1.close()
    def create_account(self):
        self.customerID = Customer.count + 1
        Customer.count += 1
        while True:
            self.acccount_type = int(input(" 01)Savings Account\n 02)Checking Account\n 03)Loan Account\n Select The Type of Account Want To Create:"))
            if self.acccount_type == 1:
                self.acccount_type = "Savings Account"
            elif self.acccount_type == 2:
                self.acccount_type = "Checking Account"
            elif self.acccount_type == 3:
                self.acccount_type = "Loan Account"
            else:
                print("Please Enter Correct Input!")
                continue
            self.first_name = input("Please Enter Your First Name (Must contain atleast 3 characters): ")
            self.last_name = input("Please Enter Your Last Name: ")
            self.address = input("Please Enter Your Address: ")
            self.username = input("Please Enter Your User Name (Must contain atleast 3 characters): ")
            self.password = input("Please Enter Your Password (Must contain atleast 3 characters): ")
            if len(self.first_name) < 3 or len(self.username) < 3 or len(self.password) < 3:
                print("Please Enter Valid Details!")
                continue
            break
            
    def set_account_no(self, account_no=None):
        self.account_no = "601-501-00"+str(self.customerID)
        print("Your Account is Successfully Created")
        print("Your Account Number is:",self.account_no)

    def save_details(self):
        f2 = open("Customer_Details.csv","a")
        f2.write(f"{self.customerID},{self.first_name},{self.last_name},{self.acccount_type},{self.account_no},{self.username},{self.password},{self.address}\n")
        f2.close()

        f4 = open("Accounts.csv","a")
        f4.write(f"{self.account_no},0\n")
        f4.close()

    def edit_account(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance
        while True:
            self.first_name = input("Please Enter Your First Name (Must contain atleast 3 characters): ")
            self.last_name = input("Please Enter Your Last Name: ")
            self.username = input("Please Enter Your User Name (Must contain atleast 3 characters): ")
            self.password = input("Please Enter Your Password (Must contain atleast 3 characters): ")
            self.address = input("Please Enter Your Address: ")
            if len(self.first_name) < 3 or len(self.username) < 3 or len(self.password) < 3:
                print("Please Enter Valid Details!")
                continue
            break
        
        for j in self.cst_lst:
            if j[4] == self.account_no:
                j[1] = self.first_name
                j[2] = self.last_name
                j[5] = self.username
                j[6] = self.password
                j[7] = self.address
        f11 = open("Customer_Details.csv","w")
        for k in self.cst_lst:
            f11.write(f"{k[0]},{k[1]},{k[2]},{k[3]},{k[4]},{k[5]},{k[6]},{k[7]}\n")
        f11.close()
        print("Your Account Successfully Updated")
        
    def customer_lists(self):
        self.cst_lst = []
        f3 = open("Customer_Details.csv","r")
        f3.seek(0)
        for i in f3:
            a = i.strip()
            b = a.split(",")
            self.cst_lst.append(b)
        f3.close()

        
x = datetime.datetime.now()
y = x.strftime("%x")
z = y.split('/')
class My_Account(Account):   
    def __init__(self,balance,ac_no,actype):
        self.mybalance = balance
        self.ac_no = ac_no
        self.actype = actype
        print("Successfully Logged in")
        print("Login Time:",x.strftime("%c"))
        print("Account Number:",self.ac_no)
        print("Account Type:",self.actype)
               
        if self.actype == "Savings Account" or self.actype == "Checking Account":
            if self.actype == "Savings Account" and self.mybalance != 0:
                f13 = open("date.txt","r")
                a = f13.read()
                b = a.split('/')
                if (int(z[0])-int(b[0])) == 1 or (int(z[0])-int(b[0])) == -11:
                    savingaccount_1 = SavingAccount(self.ac_no)
                    savingaccount_1.add_interest(self.mybalance,self.ac_no)
                    obj_account = Account(self.mybalance)                    
                    My_Account.setbalance(self)
                f13.close()

                f14 = open("date.txt","w")
                f14.write(f"{y}")
                f14.close()
                    
            while True:
                obj_account = Account(self.mybalance)
                obj_account.account_lists()
                My_Account.setbalance(self)
                print("Current Balance:",self.mybalance)
                print("\n 01)Deposit Money\n 02)Withdraw Money\n 03)Transfer Money\n 04)Edit Account\n 05)Print Report\n 06)Logout ")
                n1 = int(input("\nPlease Select An Option: "))
                if n1 == 1:           
                    obj_account.deposit(self.ac_no)
                    My_Account.setbalance(self)
                elif n1 == 2:
                    if self.actype == "Checking Account":
                        checkingaccount_1 = CheckingAccount(self.mybalance,self.ac_no)
                        checkingaccount_1.withdraw()
                        My_Account.setbalance(self)
                        
                    else:
                        obj_account.withdraw(self.ac_no)
                        My_Account.setbalance(self)
                elif n1 == 3:
                    obj_account.transfer(self.ac_no)
                    My_Account.setbalance(self)
                    
                elif n1 == 4:
                    customer1 = Customer()
                    customer1.customer_lists()
                    customer1.edit_account(self.ac_no,self.mybalance)
                elif n1 == 5:
                    obj_account.account_lists()
                    for i in obj_account.ac_lst:
                        if i[0] == self.ac_no:
                            for j in i:
                                if j == i[0]:
                                    print()
                                elif j == i[1]:
                                    print("Balance:",j)
                                    print("Transections:")
                                else:
                                    print(j)
                elif n1 == 6:
                    print("Successfully Logged out")
                    break
                else:
                    print("Please Enter Correct Input!")
                
        else:
            self.actype == "Loan Account" 
            loanAccount_1 = LoanAccount(self.mybalance) 
            f17 = open("date.txt","r")
            a = f17.read()
            b = a.split('/')
            if self.mybalance != 0:
                if (int(z[0])-int(b[0])) == 1 or (int(z[0])-int(b[0])) == -11:
                    loanAccount_1.monthly_interest(self.ac_no)
                    My_Account.setbalance(self)
            f17.close()

            f18 = open("date.txt","w")
            f18.write(f"{y}")
            f18.close()
            
            while True:
                print("Loan Balance:",self.mybalance)
                print("\n 01)Get Loan\n 02)Pay Loan\n 03)Edit Account\n 04)Print Report\n 05)Logout ")
                n2 = int(input("\nPlease Select An Option: "))
                if n2 == 1:           
                    loanAccount_1.get_loan(self.ac_no)
                    My_Account.setbalance(self)
                elif n2 == 2:
                    loanAccount_1.pay_loan(self.ac_no) 
                    My_Account.setbalance(self)
                elif n2 == 3:
                    customer2 = Customer()
                    customer2.customer_lists()
                    customer2.edit_account(self.ac_no,self.mybalance)
                elif n2 == 4:
                    account4 = Account()
                    account4.account_lists()
                    for i in account4.ac_lst:
                        if i[0] == self.ac_no:
                            for j in i:
                                if j == i[0]:
                                    print()
                                elif j == i[1]:
                                    print("Balance:",j)
                                    print("Transections:")
                                else:
                                    print(j)
                elif n2 == 5:
                    print("Successfully Logged out")
                    break
                else:
                    print("Please Select Correct Option!!")

    def setbalance(self):
        obj_account = Account(self.mybalance)
        obj_account.account_lists()
        for i in obj_account.ac_lst:
            if i[0]== self.ac_no:
                self.mybalance = float(i[1])
        

class Create_Account:
    def __init__(self):
        print("Welcome To Account Creation Page")
        print("Please Provide Following Informations To Creat Account:\n")
        customer = Customer()
        customer.create_account()
        customer.customer_lists()    
        customer.set_account_no()
        customer.save_details()

    
class Login_Account:
    def __init__(self):
        lus = []
        print("############## Welcome To Login Page ###############")
        us = input("Please Enter Your User Name: ")
        ps = input("Please Enter Your Password: ")
        cstm_lst = []
        f8 = open("Customer_Details.csv","r")
        f8.seek(0)
        for i in f8:
            a = i.strip()
            b = a.split(",")
            cstm_lst.append(b)
            lus.append(b[5])
        f8.close()#####
        if us in lus:
            for j in cstm_lst:
                if us == j[5] and ps == j[6]:
                    c = j[4]
                    d = j[3] 
                    print(f"############## Hello {j[1]} {j[2]} Welcome To Your Account ###########")
                    f6 = open("Accounts.csv","r")
                    f6.seek(0)
                    for i1 in f6:
                        a1 = i1.strip()
                        b1 = a1.split(",")
                        if b1[0] == c:
                            myaccount = My_Account(float(b1[1]),b1[0],d)###

        else:
            print("Please Enter Correct Details!")


class Bank_Admin:
    def __init__(self):
        temp='{fname:15}{lname:13}{atype:20}{anum:18}{uname:15}{pswd:13}{adrs:15}\n'
        strg = "First Name     Last Name    Account Type        Account Number    User Name      Password     Address\n\n"
        temp2='{acnum:18}{lname:13}{atype:20}{anum:18}{uname:15}{pswd:13}{adrs:15}\n'
        strg2 = "First Name     Last Name    Account Type        Account Number    User Name      Password     Address\n\n"
        
        print("############## Welcome To Admin Dashboard ###############")
        print("Please Enter The Following Details To Print Customer Details")
        aus = input("Please Enter Your User Name: ")
        aps = input("Please Enter Your Password: ")
        if aus == "admin" and aps == "psadmin":
            while True:
                print("\n 01)Print Customer Details\n 02)Print Customer Transection Report\n 03)Exit ")
                n2 = int(input("\nPlease Select An Option: "))
                if n2 == 1:            
                    customer2 = Customer()
                    customer2.customer_lists()
                    for i in customer2.cst_lst:
                        strg+=temp.format(fname=i[1],lname=i[2],atype=i[3],anum=i[4],uname=i[5],pswd=i[6],adrs=i[7])
                    print(strg)                                                    
                elif n2 == 2:
                    account1 = Account()
                    account1.account_lists()
                    print("Account Number  |   Balance  |   Transections")
                    for j in account1.ac_lst:
                        for k in range(len(j)):
                            if k == 0:
                                print(f"{j[k]}     |   ",end="")
                            elif k == (len(j)-1):
                                print(f"{j[k]}\n")
                            elif k == 1:
                                print(f"{j[k]}     |  ",end="")
                            else:
                                print(j[k]," | ",end=" ")
                    
                elif n2 == 3:
                    break
                else:
                    print("Please Enter Valid Input!")
        else:
            print("Incorrect Details!")    


##### MAIN INTERFACE #####
class Main:
    def __init__(self):
        while True:
            print("###########################################################################################")
            print("########################## WELCOME TO ONLINE BANKING SYSTEM ###############################")
            print("###########################################################################################")
            print("\n 01)Create An Account\n 02)Login To My Accont\n 03)Bank Administrator\n 04)Exit ")
            try:
                n = int(input("\nPlease Select An Option: "))
                if n == 1:            
                    createaccount = Create_Account()
                elif n == 2:
                    loginaccount = Login_Account()
                elif n == 3:
                    bankadmin = Bank_Admin()
                elif n == 4:
                    break
            except:
                print("Please Enter Valid Input!")

main = Main()
