
BAD_WORDS_LIST = ["personal trainer", "executive assistant", "low cost","ultimate software", "app tester", "1-2 hours a day","secretary", "front desk", "office manager", "use referr", "commission", "motivated individuals" , "sales specialist","no experience required", "amazing opportunity", "court researcher","technical support", "tech support", "mystery shopper","customer service", "field engineer", "administrative", "book keeping", "extra money", "extra cash", "extra income", "data entry", "have a car", "debit card", "earn extra income", "step by step training", "dollars a week", "supplemental income", "sales rep","closed lead", "do you want to make", "facebook page", "facebook fan page", "theater installation", "game tester", "% stake","printing and mailing", "laserjet", "credit score","real estate investment", "marketing", "research study","in person", "focus group", "survey", "you must live", "local", "must be local", "tutor", "instructor", "partner ", "equity", "cofounder", "co founder", "co-founder", "unpaid", "volunteer", "get paid", "get pay", "weekly", "webcam", "money making", "fast money", "workfromhome", "fast cash", "scam", "make money", "selling cell phones", "wireless sales", "it's legit", "telemarketer", "fb account", "Cell Phone Repair", "earn money by just", "only applicants residing in", "from his location", "virtual assistant", "by working less", "earn extra money", "experienced seller", "looking for a job", "earn over", "motorclub",  "office assistant", "event planner", "____________________________________________________________", "Filter by:"]

description_web_data = "   Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the things that need to get done here at Twitch. If you're a smart engineer who's capable of learning things on the fly and isn't afraid to venture into the unknown, Twitch is definitely the place for you.\n\n   As a Software Engineer at Twitch, some things you may be working on are:\n\n   Our chat system, which supports millions of concurrent users\n   Our video distribution system, which is one of the largest in the world\n   Elegant, highly-available web services to support one of our many front end platforms\n   Front end web engineering that is functional, beautiful, and delightful\n   Building applications for one of the many non-web platforms we support, including iOS, Android, XBox 360, XBox One, and Playstation 4\n   Building new features that millions of users will be seeing\n   Helping build robust deployment tools to help us move forward rapidly\n   Building great tools that lets us support our customers and partners\n\nRequirements\n\n     * Professional software development experience, the more the better\n     * You don't need a degree, but you should know how engineering works in the real world.\n     * Proficiency in at least one of the following languages: Javascript, Ruby, Python, Go, or C++\n\nBonus Points\n\n     * A strong knowledge of internet and web technology fundamentals\n     * Experience working in agile development teams\n     * Experience working on complex, multi-layer applications\n     * A passion for games or other interactive media\n\nPerks\n\n     * Full benefits, including medical, dental, vision and life\n     * 401(k) savings plan with a company match\n     * Catered daily lunch and dinners (and twice a week hearty breakfasts)\n     * Unlimited snacks and drinks\n     * Monthly in-office massages\n     * Corporate gym membership\n     * Commuter benefits\n     * Flexible time off policy\n     * Weekly happy hours and opportunity to attend one gaming event or tournament\n     * Top of the line technology to help you build your own workspace\n\n   About Twitch\n\n   Twitch is the world's leading video platform and community for gamers, with more than 100 million visitors per month. We connect gamers from around the world by allowing them to broadcast, watch, and chat with each other. Twitch's live and on-demand video platform forms the backbone of a distribution network for video game broadcasters including pro players, tournaments, leagues, developers and gaming media organizations. Twitch is leading a revolution in gaming culture, turning gameplay into an immersive video experience. Learn more at http://twitch.tv.\n\n   We are an equal opportunity employer and value diversity at Twitch. We do not discriminate on the basis of race, religion, color, national origin, gender, sexual orientation, age, marital status, veteran status, or disability status. Pursuant to the local San Francisco Fair Chance Ordinance, we will consider for employment qualified applicants with arrest and conviction records.\n\n   #LI-MD1\n\n   Apply for this job\n"

for bad_word in BAD_WORDS_LIST:
    if bad_word in description_web_data:
        any_bad_words = True
        print('** bad word:', bad_word)
    else:
    	continue

# why is his not formatted?
# bad_words = [
# “personal trainer”
# , “executive assistant”
# , “low cost”
# , “ultimate software”
# , “app tester”
# , “1-2 hours a day”
# , “secretary”
# , “front desk”
# , “office manager”
# , “use referr”
# , “commission”
# , “motivated individuals”
# , “sales specialist”
# , “no experience required”
# , “amazing opportunity”
# , “court researcher”
# , “technical support”
# , “tech support”
# , “mystery shopper”
# , “customer service”
# , “field engineer”
# , “administrative”
# , “book keeping”
# , “extra money”
# , “extra cash”
# , “extra income”
# , “data entry”
# , “have a car”
# , “debit card”
# , “earn extra income”
# , “step by step training”
# , “dollars a week”
# , “supplemental income”
# , “sales rep”
# , “closed lead”
# , “do you want to make”
# , “facebook page”
# , “facebook fan page”
# , “theater installation”
# , “game tester”
# , “% stake”
# , “printing and mailing”
# , “laserjet”
# , “credit score”
# , “real estate investment”
# , “research study”
# , “in person”
# , “focus group”
# , “survey”
# , “you must live”
# , “local”
# , “must be local”
# , “tutor”
# , “instructor”
# , “partner “
# , “equity”
# , “cofounder”
# , “co founder”
# , “co-founder”
# , “unpaid”
# , “volunteer”
# , “get paid”
# , “get pay”
# , “weekly”
# , “webcam”
# , “money making”
# , “fast money”
# , “workfromhome”
# , “fast cash”
# , “scam”
# , “make money”
# , “selling cell phones”
# , “wireless sales”
# , “it’s legit”
# , “telemarketer”
# , “fb account”
# , “Cell Phone Repair”
# , “earn money by just”
# , “only applicants residing in”
# , “from his location”
# , “virtual assistant”
# , “by working less”
# , “earn extra money”
# , “experienced seller”
# , “looking for a job”
# , “earn over”
# , “motorclub”
# , “office assistant”
# , “event planner”
# ]