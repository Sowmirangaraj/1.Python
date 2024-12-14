class ElegibilityForMarriage():
    def Elegible():
        gender=input("Your Gender:")
        if(gender=="Male"):
            age=int(input("Your Age:"))
            if(age>21):
                print("ELIGIBLE")
                message="ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                message="NOT ELIGIBLE"
        else:
            age=int(input("Your Age:"))
            if(age>18):
                print("ELIGIBLE")
                message="ELIGIBLE"
            else:
                print("NOT ELIGIBLE") 
                message="NOT ELIGIBLE"
