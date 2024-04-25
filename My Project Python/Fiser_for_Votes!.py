import json

# import os

# script_directory = os.path.dirname(__file__)

# file_path_yes = os.path.join(script_directory, "file_txt_for_yes.json")
# with open(file_path_yes, "x") as file_yes:
# data_yes = {
# "details": []
# }
# json.dump(data_yes, file_yes)

# file_path_no = os.path.join(script_directory, "file_txt_for_no.json")
# with open(file_path_no, "x") as file_no:
# data_no = {
# "details": []
# }
# json.dump(data_no, file_no)

# except FileExistsError:
# pass


class Operation:
    def add_file(self):
        try:

            with open("file_txt_for_yes.json", "x") as file:#cid folosim with automat se inchide!
                file.write("""{
            "details": []}""")


            with open("file_txt_for_no.json", "x") as file:
                file.write("""{
            "details": []}""", )


        except FileExistsError as e:
            print(f"Error is existes: {e}")

class Voturi(Operation):

    def __init__(self):
        super().add_file()
        self.number_yes = 0
        self.number_no = 0

    def here_for_detal(self):
        super().add_file()
        while True:
            name = input("Your_name: ")
            second_name = input("Last_name: ")
            while True :
                try:
                    age = int(input("How old are you: "))
                    break
                except ValueError:
                    print("Here is the Numbers ,Are you understand?")
            while True:
                for_what = input("Are you vote for (yes/no): ").lower()
                if for_what == "yes" or for_what == "no":
                    break
                print("What The Hell , Put here (yes/no)")
            
            self.for_txt_votes_yes(name,second_name,age,for_what)
            self.for_txt_votes_no(name,second_name,age,for_what)
            self.check_how_many(for_what)
            numbers_yes, numbers_no = self.in_total()
            print("Number in total for no:", numbers_no)
            print("Number in total for yes:", numbers_yes)
            print("Number of yes votes", self.number_yes)
            print("Number of no votes", self.number_no)
            stop_voting = input("Type 'stop' to finish voting or press Enter to continue: ")
            if stop_voting.lower() == "stop":
                break

    def for_txt_votes_yes(self,name,second_name,age,for_what):
        if for_what == "yes":
            with open ("file_txt_for_yes.json","r") as file_yes:
                reads = json.load(file_yes)
            new_person = {"First_name":name ,
            "Last_name":second_name ,"Age":age ,"For_what":for_what}
            reads["details"].append(new_person)
            json.dumps(reads)
            with open("file_txt_for_yes.json", "w") as file_yes:
                json.dump(reads,file_yes,indent=4)

    def for_txt_votes_no(self,name,second_name,age,for_what):
        if for_what == "no":
            with open ("file_txt_for_no.json","r") as file_no:
                reads = json.load(file_no)
            new_person = {"First_name":name ,
            "Last_name":second_name ,"Age":age ,"For_what":for_what}
            reads["details"].append(new_person)
            json.dumps(reads)
            with open("file_txt_for_no.json", "w") as file_no:
                json.dump(reads,file_no,indent=4)

    def check_how_many(self,for_what):
        if for_what == "yes":
            self.number_yes += 1
        elif for_what == "no":
            self.number_no += 1

    def in_total(self):
        numbers_yes = 0
        numbers_no = 0
        with open("file_txt_for_yes.json", "r") as file_yes:
            templates_yes = json.load(file_yes)
            for element in templates_yes["details"]:
                if element.get("For_what") == "yes":
                    numbers_yes += 1

        with open("file_txt_for_no.json", "r") as file_no:
            templates_no = json.load(file_no)
            for element in templates_no["details"]:
                if element.get("For_what") == "no":
                    numbers_no += 1
        return numbers_yes, numbers_no
if __name__ == "__main__" :
    voturi = Voturi()
    voturi.here_for_detal()

