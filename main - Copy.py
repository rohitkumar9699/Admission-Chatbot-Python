import re
import long_responses as ans

def mess_prob(user_message, recognised_words, single_response=False, required_words=[]):
    chance = 0
    contain_word = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            chance += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(chance) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            contain_word = False
            break

    # Must either have the required words, or be a single response
    if contain_word or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    maximum_prob = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal maximum_prob
        maximum_prob[bot_response] = mess_prob(message, list_of_words, single_response, required_words)

    # # Responses -------------------------------------------------------------------------------------------------------
    response('Hello! How can I help you', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
 
    # Longer responses
    response(ans.Hostel_Fee, ['hostel', 'hostel details', 'room' , 'room details'],required_words=['hostel'])
    response(ans.scholarships_Type, ['scholarships','scholarship', 'financial', 'economically','differently abled', 'scholarships awarded'], single_response=True)
    response(ans.College_Info,['overview', 'about','university'], single_response=True)
    response(ans.get_admission,['admission', 'admisssion process'], single_response=True)  #****************************
    response(ans.many_campuses ,['campus','campuses','tour'], single_response=True)
    response(ans.ratio ,['faculty student ratio','ratio', 'teacher student ratio'],single_response=True)
    response(ans.collaborations , ['collaborations','collaboration','tieup'],single_response=True)
    response(ans.student_clubs , ['club', 'clubs'],single_response=True)
    response(ans.sports_facilities ,['sports', 'cricket', 'football'],single_response=True)
    response(ans.change_branch ,['change branch', 'change stream'],single_response=True) #*****************************
    response(ans.courses_available ,['course', 'courses', 'subjects', 'branches'],single_response=True)
    response(ans.Placements ,['package', 'highest package','average package'],single_response=True)
    response(ans.top_companies ,['companies', 'internships','top companies'],single_response=True)
    response(ans.Faculty ,['faculty','staff','experience'],single_response=True)
    response(ans.extracurricular_activities,['curriculum','activities'],single_response=True)
    response(ans.fee_structure,['fee', 'fees', 'tuition fees'], single_response=True) 
    response(ans.Infrastructure,['architecture', 'infrastructure', 'architect'],single_response=True)
    response(ans.Library,['library', 'books', 'book'],single_response=True)
    response(ans.Transport_Fee,['transport', 'bus'],single_response=True)
    response(ans.Medical_facilities,['medical', 'doctor'],single_response=True)
    response(ans.B_Tech_courses,['b.Tech', 'cse','computer science' ,'engineering'],single_response=True)

    best_match = max(maximum_prob, key=maximum_prob.get)

    return ans.unknown() if maximum_prob[best_match] < 1 else best_match




# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response 


# Testing the response system
while True:
    user_input =input('\nYou: ').lower()
    stop =["exit", "close", "terminate","shut","quit"]
    if user_input in stop:
        break
    print('Bot: ' + get_response(user_input))



#*************************************************************************************************************
