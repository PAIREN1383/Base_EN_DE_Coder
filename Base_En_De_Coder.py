import base64

Built_List = []
def result():
    print("How decoded:", Built_List)
    Built_List.reverse()
    print("How you can build it:", Built_List)

def Err(VAR, MAP, NOTRUN, ERR_RUN):
    if MAP == [] and NOTRUN == ERR_RUN and VAR < 2:
        VAR += 1 
    return VAR

def b_85(Entxt, S_tep, M_a_p_2="none", NotRun2=""):
    global B85, RB85
    for num in range(50):
        try:
            if M_a_p_2 == [] and NotRun2[0] == "b85" and B85 < 2 or M_a_p_2[0] != "b85" and M_a_p_2 != "none" and M_a_p_2 != []:
                B85 = Err(B85, M_a_p_2, NotRun2, "b85")
                raise StopIteration()
            Entxt0 = base64.b85decode(Entxt).decode()
            Entxt = Entxt0
            Built_List.append("b85")
            print("b85 decoded ---> " + Entxt)
            if M_a_p_2[0] == "b85":
                M_a_p_2.pop(0)
            if len(Built_List) == S_tep:
                return Entxt
        except:
            try:
                if M_a_p_2 == [] and NotRun2 == ["r", "b85"] and RB85 < 2 or M_a_p_2[0:2] != ["r", "b85"] and M_a_p_2 != "none" and M_a_p_2 != []:
                    RB85 = Err(RB85, M_a_p_2, NotRun2, ["r", "b85"])
                    raise StopIteration()
                Entxt0 = Entxt[-1::-1]
                Entxt0 = base64.b85decode(Entxt0).decode()
                Entxt = Entxt0
                Built_List.append("r")
                Built_List.append("b85")
                print("r & b85 decoded ---> " + Entxt)
                if M_a_p_2[0:2] == ["r", "b85"]:
                    M_a_p_2.pop(0)
                    M_a_p_2.pop(0)
                if len(Built_List) >= S_tep:
                    return Entxt
            except:
                return Entxt

def Decoder(Entxt, S_tep, M_a_p="none", NotRun=""):
    try:
        S_tep = int(S_tep)
    except:
        S_tep = 10
    if S_tep <= 0:
        return "You can not give less than or equal to 0 steps!!!"
    res0 = ""
    for num in range(150):
        try:
            if M_a_p == [] and NotRun[0] == "b64" and B64 < 2 or M_a_p[0] != "b64" and M_a_p != "none" and M_a_p != []:
                B64 = Err(B64, M_a_p, NotRun, "b64")
                raise StopIteration()
            Entxt = base64.b64decode(Entxt).decode()
            Built_List.append("b64")
            print("b64 decoded ---> " + Entxt)
            if M_a_p[0] == "b64":
                M_a_p.pop(0)
            if len(Built_List) == S_tep:
                result()
                return Entxt
        except:
            try:
                if M_a_p == [] and NotRun == ["r", "b64"] and RB64 < 2 or M_a_p[0:2] != ["r", "b64"] and M_a_p != "none" and M_a_p != []:
                    RB64 = Err(RB64, M_a_p, NotRun, ["r", "b64"])
                    raise StopIteration()
                Entxt0 = Entxt[-1::-1]
                Entxt0 = base64.b64decode(Entxt0).decode()
                Entxt = Entxt0
                Built_List.append("r")
                Built_List.append("b64")
                print("r & b64 decoded ---> " + Entxt)
                if M_a_p[0:2] == ["r", "b64"]:
                    M_a_p.pop(0)
                    M_a_p.pop(0)
                if len(Built_List) >= S_tep:
                    result()
                    return Entxt
            except:
                try:
                    if M_a_p == [] and NotRun[0] == "b32" and B32 < 2 or M_a_p[0] != "b32" and M_a_p != "none" and M_a_p != []:
                        B32 = Err(B32, M_a_p, NotRun, "b32")
                        raise StopIteration()
                    Entxt = base64.b32decode(Entxt).decode()
                    Built_List.append("b32")
                    print("b32 decoded ---> " + Entxt)
                    if M_a_p[0] == "b32":
                        M_a_p.pop(0)
                    if len(Built_List) == S_tep:
                        result()
                        return Entxt
                except:
                    try:
                        if M_a_p == [] and NotRun == ["r", "b32"] and RB32 < 2 or M_a_p[0:2] != ["r", "b32"] and M_a_p != "none" and M_a_p != []:
                            RB32 = Err(RB32, M_a_p, NotRun, ["r", "b32"])
                            raise StopIteration()
                        Entxt0 = Entxt[-1::-1]
                        Entxt0 = base64.b32decode(Entxt0).decode()
                        Entxt = Entxt0
                        Built_List.append("r")
                        Built_List.append("b32")
                        print("r & b32 decoded ---> " + Entxt)
                        if M_a_p[0:2] == ["r", "b32"]:
                            M_a_p.pop(0)
                            M_a_p.pop(0)
                        if len(Built_List) >= S_tep:
                            result()
                            return Entxt
                    except:
                        try:
                            if M_a_p == [] and NotRun[0] == "b16" and B16 < 2 or M_a_p[0] != "b16" and M_a_p != "none" and M_a_p != []:
                                B16 = Err(B16, M_a_p, NotRun, "b16")
                                raise StopIteration()
                            Entxt = base64.b16decode(Entxt).decode()
                            Built_List.append("b16")
                            print("b16 decoded ---> " + Entxt)
                            if M_a_p[0] == "b16":
                                M_a_p.pop(0)
                            if len(Built_List) == S_tep:
                                result()
                                return Entxt
                        except:
                            try:
                                if M_a_p == [] and NotRun == ["r", "b16"] and RB32 < 2 or M_a_p[0:2] != ["r", "b16"] and M_a_p != "none" and M_a_p != []:
                                    RB32 = Err(RB32, M_a_p, NotRun, ["r", "b16"])
                                    raise StopIteration()
                                Entxt0 = Entxt[-1::-1]
                                Entxt0 = base64.b16decode(Entxt0).decode()
                                Entxt = Entxt0
                                Built_List.append("r")
                                Built_List.append("b16")
                                print("r & b16 decoded ---> " + Entxt)
                                if M_a_p[0:2] == ["r", "b16"]:
                                    M_a_p.pop(0)
                                    M_a_p.pop(0)
                                if len(Built_List) >= S_tep:
                                    result()
                                    return Entxt
                            except:
                                try:
                                    if M_a_p == [] and NotRun[0] == "a85" and A85 < 2 or M_a_p[0] != "a85" and M_a_p != "none" and M_a_p != []:
                                        A85 = Err(A85, M_a_p, NotRun, "a85")
                                        raise StopIteration()
                                    Entxt = base64.a85decode(Entxt).decode()
                                    Built_List.append("a85")
                                    print("a85 decoded ---> " + Entxt)
                                    if M_a_p[0] == "a85":
                                        M_a_p.pop(0)
                                    if len(Built_List) == S_tep:
                                        result()
                                        return Entxt
                                except:
                                    try:
                                        if M_a_p == [] and NotRun == ["r", "a85"] and RA85 < 2 or M_a_p[0:2] != ["r", "a85"] and M_a_p != "none" and M_a_p != []:
                                            RA85 = Err(RA85, M_a_p, NotRun, ["r", "a85"])
                                            raise StopIteration()
                                        Entxt0 = Entxt[-1::-1]
                                        Entxt0 = base64.a85decode(Entxt0).decode()
                                        Entxt = Entxt0
                                        Built_List.append("r")
                                        Built_List.append("a85")
                                        print("r & a85 decoded ---> " + Entxt)
                                        if M_a_p[0:2] == ["r", "a85"]:
                                            M_a_p.pop(0)
                                            M_a_p.pop(0)
                                        if len(Built_List) >= S_tep:
                                            result()
                                            return Entxt
                                    except:
                                        res = b_85(Entxt, S_tep, M_a_p, NotRun)
                                        if res != None:
                                            Entxt = res
                                        if len(Built_List) >= S_tep:
                                            result()
                                            return Entxt
                                        if Entxt == res0:
                                            result()
                                            return Entxt
                                        else: 
                                            res0 = Entxt

def Encoder(LIST, txt):
    try:
        LIST = list(map(lambda x: x.lower().replace(" ", ""), LIST))
        if LIST[0] == "r":
            print("You can not reverse your text in the first step!!!")
            exit()
        for obj in LIST:
            if obj == "b64":
                txt = base64.b64encode(txt.encode("utf-8")).decode()
            elif obj == "b32":
                txt = base64.b32encode(txt.encode("utf-8")).decode()
            elif obj == "b16":
                txt = base64.b16encode(txt.encode("utf-8")).decode()
            elif obj == "a85":
                txt = base64.a85encode(txt.encode("utf-8")).decode()
            elif obj == "b85":
                txt = base64.b85encode(txt.encode("utf-8")).decode()
            elif obj == "r":
                txt = txt[-1::-1]
            else:
                pass
    except:
        txt = "Error!!!"
    return txt

while True:                    
    print("*********************************** \nEnter 'Q' to quit the program.")
    what = input("[1] --> Encoder \n[2] --> Decoder \n[3] --> Decode with map \nEnter your choise: ")
    if what.lower() == "q":
        exit()
    elif what == "1":
        print("***********************************")
        Text = input("Enter your text: ")
        L_I_S_T = input("Enter your List_Operation: ").split(",")
        EnCode = Encoder(L_I_S_T, Text)
        print("Your encrypted text: " + EnCode)
    elif what == "2":
        print("***********************************")
        Code = input("Enter your encoded text: ")
        if Code.replace(" ", "") == "":
            continue
        S_tep0 = input("Enter number of step(s) (Default steps = 10): ")
        DeCode = Decoder(Code, S_tep0)
        print("Your decrypted text: " + DeCode)
        for num in range(50):
            y_n_Q = input("Is it true??? y/n: ")
            if y_n_Q.lower() == "n" or y_n_Q.lower() == "no":
                try:
                    Not_Run = [Built_List[0], Built_List[1]]
                except:
                    try:
                        Not_Run = [Built_List[0]]
                    except:
                        print("Error!!!")
                Map = Built_List.copy()
                Built_List.clear()
                try:
                    Map.pop(0)
                except:
                    print("Error!!!")
                Map.reverse()
                B64, RB64, B32, RB32, B16, RB16, A85, RA85, B85, RB85 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                DeCode = Decoder(Code, S_tep0, Map, Not_Run)
                print("Your decoded text: " + DeCode)
            else:
                Built_List.clear()
                break
    elif what == "3":
        Code = input("Enter your encoded text: ")
        if Code.replace(" ", "") == "":
            continue
        print("<<<<<<<<<<<<< Reverse the build map to made the map for decoding. >>>>>>>>>>>>>")
        MapDC = input("Enter a map to decode your code: ").split(",")
        MapDC = list(map(lambda x: x.replace(" ", ""), MapDC))
        S_tepMap = len(MapDC)
        DeCode = Decoder(Code, S_tepMap, MapDC)
        print("Your decoded text: " + DeCode)
        Built_List.clear()
        
        # Author: M == PAIREN
