def foo() -> str:
    print ("foo boo")
    
def boo() -> str:
    print ("boo foo")

match input("yes or no: "):
 case "yes":
     foo()
 case "no":
     boo()  
     
     
     
     
