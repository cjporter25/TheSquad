from ts_riot_api import *
from ts_firebase import *
from ts_test import *
from ts_squad import *
from ts_constants import *
import time
import webbrowser

def open_homepage():
    #test(APIKEY)
    #memberList = handleUserInput()
    start = time.time()
    init_firebase()
    APIKEY = get_riot_api_key()

    memberList = TEST_SQUAD_LIST_4
    squad = create_new_squad(memberList, APIKEY)
    build_squad(squad)
    print("***Updated or Added Squad Successfully***")
    Event().wait(1)
    squad.show_squad_data()

    end = time.time()
    print("Project Execution Time: " + str(end-start))

    webbrowser.open_new('https://thesquad-ce16a.web.app')
def create_new_squad(memberList, APIKEY):
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







