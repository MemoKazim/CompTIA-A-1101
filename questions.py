with open("data.txt" , "r") as allData:
    Data = allData.read()
    question_list = Data.split("QUESTION ")

