class Schwa_Analysis:
    line = ""
    enter = [ '\r', '\n' ]
    scheme = []
    char_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    char_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
			  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def char_type(self):
        f= open("Char_Type.txt",'r',encoding='utf-8')
        while(True):
            line = f.readline()
            #print(line)
            if(line == ""):
                break
            key, val = line.split()
            self.scheme[key] = val
        
        return self.scheme

    def rule_one(self,word):  #// Implements Rule #1 - Replace first syllable schwa with /a/
        phones = word.split("-")
        trans = ""
        if(phones[0] in self.scheme):
            value = self.scheme[phones[0]]
            if(value == "c"):
                if(len(phones) > 2):
                    if(phones[0] == "k"):
                        if(phones[1] == "@"):
                            if(phones[2] != "r"):
                                phones[1] = "a"
                    
                    elif(phones[1] == "@"):
                        phones[1] = "a"

        for phone in phones:
            trans = trans + phone + "-"

        return trans

    def rule_two(self, word): #Implements Rule #2 - Occurrences with /r/ and /h/
        phones = word.split("-")
        trans = ""
        for i in range(1,len(phones)):
            phone = phone[i]

            if(phone == "r"):
                if(len(phone) > 2):
                    prev_phone = phones[i-1]
                    prev_type = self.scheme[prev_phone]
                    if(prev_type == "c"):
                        if(i+3 < len(phones)):
                            next_phone = phones[i+1]
                            if(next_phone == "@"):
                                nnext_phone = phones[i+2]
                                nnext_type = self.scheme[nnext_phone]
                                if(nnext_type == "c"):
                                    phones[i+1] = "a"
        
        for phone in phones:
            trans = trans + phone + "-"

        return trans