bad_words=["personal trainer", "executive assistant", "low cost","ultimate software", "app tester", "1-2 hours a day","secretary", "front desk", "office manager", "use referr", "commission", "motivated individuals" , "sales specialist","no experience required", "amazing opportunity", "court researcher","technical support", "tech support", "mystery shopper","customer service", "field engineer", "administrative", "book keeping", "extra money", "extra cash", "extra income", "data entry", "have a car", "debit card", "earn extra income", "step by step training", "dollars a week", "supplemental income", "sales rep","closed lead", "do you want to make", "facebook page", "facebook fan page", "theater installation", "game tester", "% stake","printing and mailing", "laserjet", "credit score","real estate investment", "research study","in person", "focus group", "survey", "you must live", "local", "must be local", "tutor", "instructor", "partner ", "equity", "cofounder", "co founder", "co-founder", "unpaid", "volunteer", "get paid", "get pay", "weekly", "webcam", "money making", "fast money", "workfromhome", "fast cash", "scam", "make money", "selling cell phones", "wireless sales", "it's legit", "telemarketer", "fb account", "Cell Phone Repair", "earn money by just", "only applicants residing in", "from his location", "virtual assistant", "by working less", "earn extra money", "experienced seller", "looking for a job", "earn over", "motorclub",  "office assistant", "event planner"]
        if bad_words.any?{|bw| all_txt.include?(bw) }
            render json: {status: "error", code: 23, message: "Not a dev job!"}

"executive assistant" - 18
customer service - 4
administrative - 54

# Works for phrases
string = "It's not safe to go alone. Take this."
list_of_bad_words = ["go alone"]

for bad_word in list_of_bad_words:
    if bad_word in string:
        print('The message is safe.')


# DOESNT WORK FOR PHRASES
#my_word_list = ['one', 'four', 'three']
#my_word_list = ['one', 'two', 'three']
bad_words_list = ["personal trainer", "executive assistant", "low cost","ultimate software", "app tester", "1-2 hours a day","secretary", "front desk", "office manager", "use referr", "commission", "motivated individuals" , "sales specialist","no experience required", "amazing opportunity", "court researcher","technical support", "tech support", "mystery shopper","customer service", "field engineer", "administrative", "book keeping", "extra money", "extra cash", "extra income", "data entry", "have a car", "debit card", "earn extra income", "step by step training", "dollars a week", "supplemental income", "sales rep","closed lead", "do you want to make", "facebook page", "facebook fan page", "theater installation", "game tester", "% stake","printing and mailing", "laserjet", "credit score","real estate investment", "research study","in person", "focus group", "survey", "you must live", "local", "must be local", "tutor", "instructor", "partner ", "equity", "cofounder", "co founder", "co-founder", "unpaid", "volunteer", "get paid", "get pay", "weekly", "webcam", "money making", "fast money", "workfromhome", "fast cash", "scam", "make money", "selling cell phones", "wireless sales", "it's legit", "telemarketer", "fb account", "Cell Phone Repair", "earn money by just", "only applicants residing in", "from his location", "virtual assistant", "by working less", "earn extra money", "experienced seller", "looking for a job", "earn over", "motorclub",  "office assistant", "event planner"]


#a_string = 'one two three'
#a_string = 'four five six'
a_string = "   Thanks for your data entry interest in working at LeapYear.\n\n   This is an overview of the problem we are solving, what we've done so far, and how you can get involved.\n\n   LeapYear is a secure, automated machine learning platform for integrating, analyzing, and protecting sensitive data.\n\n   Enterprises cannot safely leverage their data for analytics and machine learning because of security, privacy, and regulatory risks. LeapYear's technology enables enterprises to securely analyze and share sensitive data without exposing any confidential information."

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

if words_in_string(my_word_list, a_string):
    print('One or more words found!')
else:
    print('nada')
