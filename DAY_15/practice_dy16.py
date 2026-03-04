#Exceptional handling(TRY,ECXEPT,ELSE,FINALLY)

"""
print("starting of code")


try:
    list = [10, 20, 30]
    print(list[5])
   
except NameError:
    print("a is not defined")
except ZeroDivisionError:
    print("cant divide with 0")
except ValueError:
    print("Enter the requested value")
except IndexError:
    print("index is not present")
except FileNotFoundError:
    print("file dosen't exist")
except KeyError:
    print("dict not found")    
else:
    print("No error")
finally:
    print("end of the block")




#another wayof multi exception handling

try:
    10/0
except( NameError, ZeroDivisionError ,  ValueError, IndexError  ,KeyError ,FileNotFoundError) as e:
    print(f'Error occured:{e}')
else:
    print("No Error")
finally:
    print("End of the block")



#another method(without mentioning)


try:
   list=[1,2,3]
   print(list[4])
except Exception as e:
    print(f'Error occured:{e}')
else:
    print("No Error")
finally:
    print("End of the block")



#raising the error exception explictly

try:
   a=int(input())
   if a<0:
       raise Exception("Enter the positive value")
    
except Exception as e:
    print(f'Error occured:{e}')
else:
    print("No Error")
finally:
    print("End of the block")


"""

accounts = {
    "1001": {"name": "Shanu", "balance": 5000, "transactions": [1000, -500, 200]},
    "1002": {"name": "Saaketh5", "balance": 3000, "transactions": [500, -200]}
}

while True:
    print("\n--- ATM Simulation Menu ---")
    print("1. Check Average Transaction (ZeroDivisionError)")
    print("2. Withdraw with Invalid Input (ValueError)")
    print("3. Deposit with Invalid Data Type (TypeError)")
    print("4. Access Invalid Transaction History (IndexError)")
    print("5. Access Non-Existent Account (KeyError)")
    print("6. Read Missing Transaction Log File (FileNotFoundError)")
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    try:

        # 1️⃣ ZeroDivisionError
        if choice == "1":
            acc = input("Enter Account Number: ")
            transactions = accounts[acc]["transactions"]
            avg = sum(transactions) / len(transactions)
            print("Average Transaction:", avg)

        # 2️⃣ ValueError
        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))  # If user types text
            print("Withdrawal successful:", amount)

        # 3️⃣ TypeError
        elif choice == "3":
            amount = input("Enter deposit amount: ")
            result = amount + 1000   # Adding string + int causes TypeError
            print(result)

        # 4️⃣ IndexError
        elif choice == "4":
            acc = input("Enter Account Number: ")
            index = int(input("Enter transaction index: "))
            print("Transaction:", accounts[acc]["transactions"][index])

        # 5️⃣ KeyError
        elif choice == "5":
            acc = input("Enter Account Number: ")
            print(accounts[acc])   # If account not in dictionary

        # 6️⃣ FileNotFoundError
        elif choice == "6":
            file = open("transaction_log.txt", "r")
            print(file.read())
            file.close()

        # 7️⃣ Exit
        elif choice == "7":
            print("Exiting ATM...")
            break

        else:
            print("Invalid Choice")

    except ZeroDivisionError:
        print("Error: No transactions available to calculate average.")

    except ValueError:
        print("Error: Invalid numeric input.")

    except TypeError:
        print("Error: Invalid data type used in operation.")

    except IndexError:
        print("Error: Transaction index out of range.")

    except KeyError:
        print("Error: Account number does not exist.")

    except FileNotFoundError:
        print("Error: Transaction log file not found.")
   




































































    









    
