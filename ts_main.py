from ts_riot_api import *
from ts_firebase import *
from ts_test import *
from ts_squad import *
from ts_constants import *
import time
import json
import webbrowser

def open_homepage():
    #test(APIKEY)
    #memberList = handleUserInput()
    projStart = time.time()
    init_firebase()
    APIKEY = get_riot_api_key()

    #TEST_SQUAD_LIST_01 = ["ShenDaddyyDom", "PureLunar", "Serandipityyy"]
    #TEST_SQUAD_LIST_0 = ["Chrispychickn25", "ShenDaddyyDom", "PureLunar", "Serandipityyy"]
    #TEST_SQUAD_LIST_1 = ["Chrispychickn25", "ShenDaddyyDom", "PureLunar"]
    #TEST_SQUAD_LIST_2 = ["Chrispychickn25", "ShenDaddyyDom"]
    #TEST_SQUAD_LIST_3 = ["Chrispychickn25", "PureLunar", "Serandipityyy"]
    #TEST_SQUAD_LIST_4 = ["ShenDaddyyDom", "PureLunar"]
    #TEST_SQUAD_LIST_5 = ["PureLunar", "Serandipityyy"]
    #Shensëi

    squadStart = time.time()
    memberList = TEST_SQUAD_LIST_5
    squad = new_squad(memberList, APIKEY)
    squadEnd = time.time()
    totalSquadTime = round((squadEnd - squadStart), 2)
    print("***Squad Look-up Was Successful***")

    firebaseStart = time.time()
    build_squad(squad)
    firebaseEnd = time.time()
    totalFirebaseTime = round((firebaseEnd - firebaseStart), 2)
    print("***Updated or Added Squad to Database Successfully***")

    squad.show_squad_data()
    projEnd = time.time()
    totalExeTime = round((projEnd - projStart), 2)

    EXE_META_DATA['exeTimeSquad'] = totalSquadTime
    EXE_META_DATA['exeTimeFirebase'] = totalFirebaseTime
    EXE_META_DATA['exeTimeProj'] = totalExeTime
    print("Project Execution Time: " + str(projEnd - projStart))

    #webbrowser.open_new('https://thesquad-ce16a.web.app')
    data = json.dumps(EXE_META_DATA, indent=3)
    print(data)

def new_squad(memberList, APIKEY):
    squad = Squad()
    squad.set_member_list(memberList)
    squad.show_member_list()
    squad.gather_squad_member_info(APIKEY)
    squad.create_squad_id()
    squad.show_squad_ID()
    #MIN_MATCH_HISTORY_COUNT = "0"
    #REC_MATCH_HISTORY_COUNT = "90"
    #MAX_MATCH_HISTORY_COUNT = "100"
    #DEF_MATCH_HISTORY_COUNT = "20"
    squad.gather_squad_match_history(REC_MATCH_HISTORY_COUNT, APIKEY)
    squad.find_shared_matches(APIKEY)
    squad.show_shared_match_history()
    squad.show_request_count()
    return squad
def handle_user_input():
    print("Hello! Welcome to TheSquad. Continue entering summoner names")
    print("below. Squad member count must be between 2 and 5. Once finished")
    print("type 'n' and press enter.")
    userFinished = False
    userInputSquad = []
    while(not userFinished):
        newMember = input('Summoner Name: ')
        isMemberValid = is_mem_name_valid(newMember)
        userInputSquad.append(newMember)
        print("Current Squad --> ")
        print(userInputSquad)
        response = input('Add more? (y) for yes or (n) for no: ')
        if(response != "y"):
            userFinished = True
            return userInputSquad
def test(APIKEY):
    test_response_codes(APIKEY)
    test_response_rate_limit_exceeded(APIKEY)

open_homepage()







