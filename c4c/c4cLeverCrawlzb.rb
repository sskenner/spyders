def create_gig_opportunity_metum

        all_txt = “#{params[‘description’]} #{params[‘title’]}“.downcase
        bad_words=[“personal trainer”, “executive assistant”, “low cost”,“ultimate software”, “app tester”, “1-2 hours a day”,“secretary”, “front desk”, “office manager”, “use referr”, “commission”, “motivated individuals” , “sales specialist”,“no experience required”, “amazing opportunity”, “court researcher”,“technical support”, “tech support”, “mystery shopper”,“customer service”, “field engineer”, “administrative”, “book keeping”, “extra money”, “extra cash”, “extra income”, “data entry”, “have a car”, “debit card”, “earn extra income”, “step by step training”, “dollars a week”, “supplemental income”, “sales rep”,“closed lead”, “do you want to make”, “facebook page”, “facebook fan page”, “theater installation”, “game tester”, “% stake”,“printing and mailing”, “laserjet”, “credit score”,“real estate investment”, “research study”,“in person”, “focus group”, “survey”, “you must live”, “local”, “must be local”, “tutor”, “instructor”, “partner “, “equity”, “cofounder”, “co founder”, “co-founder”, “unpaid”, “volunteer”, “get paid”, “get pay”, “weekly”, “webcam”, “money making”, “fast money”, “workfromhome”, “fast cash”, “scam”, “make money”, “selling cell phones”, “wireless sales”, “it’s legit”, “telemarketer”, “fb account”, “Cell Phone Repair”, “earn money by just”, “only applicants residing in”, “from his location”, “virtual assistant”, “by working less”, “earn extra money”, “experienced seller”, “looking for a job”, “earn over”, “motorclub”,  “office assistant”, “event planner”]
        if bad_words.any?{|bw| all_txt.include?(bw) }
            render json: {status: “error”, code: 23, message: “Not a dev job!“}
        elsif params[‘key’] == config.api_key
            metum = GigOpportunityMetum.new
            metum.title = params[“title”]
            metum.description = params[“description”]
            metum.website = params[“website”]
            metum.utc_datetime = params[“utc_datetime”]
            metum.lat = params[:lat] # BigDecimal
            metum.lng = params[:lng] # BigDecimal
            metum.country = params[:country] # text, e.g. “Canada” .. “Lebanon” ..
            metum.employment_type = params[:employment_type] if params[:employment_type].present? # format: fte, contract, internship, either - nil if we don’t have the info.  either means either contract or fte, employee’s choice
            metum.remote_ok = params[:remote_ok] if params[:remote_ok].present? # format: remote_not_ok, remote_ok - nil if we don’t have the info
            metum.time_commitment = params[:time_commitment] if params[:time_commitment].present? # format: fulltime, parttime, project - nil if we don’t have the info
            metum.reviewed = true if metum.title and metum.description and metum.website and metum.utc_datetime and metum.lat and metum.lng and metum.country and metum.employment_type and metum.remote_ok and metum.time_commitment != nil
            if metum.save
                render json: {status: “success”, code: 11, message: “Job added successfully.“}
                if metum.reviewed
                    MatchOpportunityToUsersWorker.perform_async(metum.id)
                end
            else
                render json: {status: “error”, code: 22, message: “Probably invalid values format!“}
            end
        else
            render json: {status: “error”, code: 21, message: “Invalid API key!“}
        end
    end



[10:15] 
class GigOpportunityMetum < ActiveRecord::Base
    has_many :gig_opportunities, class_name: ‘GigOpportunity’, foreign_key: ‘website’, primary_key: ‘website’

    validates_presence_of :title
    validates_presence_of :description
    validates_presence_of :website
    validates_uniqueness_of :website
    validates :employment_type, :inclusion=> { :in => [‘fte’, ‘contract’, ‘internship’, ‘either’, ‘doesnt_say’] }, :allow_nil => true
    validates :remote_ok, :inclusion=> { :in => [‘remote_not_ok’, ‘remote_ok’, ‘doesnt_say’] }, :allow_nil => true
    validates :time_commitment, :inclusion=> { :in => [‘fulltime’, ‘parttime’, ‘project’] }, :allow_nil => true

...

# zackburt [12:46 PM] 
# Here’s some info on how our internal API works…

# I don’t know if you speak ruby, but hopefully this code-sample is self-documenting.. this is what we call via the ruby crons:

def post_job(title, website, description, utc_datetime, lat = nil, lng = nil, country = nil, employment_type = nil, remote_ok = nil, time_commitment = nil)
    if old_job_listing?(utc_datetime)
        return
    end

   if low_quality_keywords_present?(title, description)
        puts “LQ keywords”
        return
    end

   encoding_options = {
      :invalid           => :replace,  # Replace invalid byte sequences
      :undef             => :replace,  # Replace anything not defined in ASCII
      :replace           => ‘’,        # Use a blank for those replacements
      :universal_newline => true       # Always break lines with \n
    }
    title = title.encode(Encoding.find(‘ASCII’), encoding_options)
    description = description.encode(Encoding.find(‘ASCII’), encoding_options)
    website = website.encode(Encoding.find(‘ASCII’), encoding_options)


   options = {
      :body => {
           :key => @api_key,
           :title => title,
           :website => website,
           :description => description,
           :utc_datetime => utc_datetime,
           :lat => lat,
           :lng => lng,
           :country => country,
           :employment_type => employment_type,
           :remote_ok => remote_ok,
           :time_commitment => time_commitment
      }
   }

  begin
        HTTParty.post(@api_base_url + ‘/api/metum/create’, options)
    rescue Exception => e
        puts e
    end
end

# utc_datetime is utc_datetime.  lat, lng are decimals.  country is a string… for employment_type, remote_ok, time_commitment…

validates :employment_type, :inclusion=> { :in => [‘fte’, ‘contract’, ‘internship’, ‘either’, ‘doesnt_say’] }, :allow_nil => true
validates :remote_ok, :inclusion=> { :in => [‘remote_not_ok’, ‘remote_ok’, ‘doesnt_say’] }, :allow_nil => true
validates :time_commitment, :inclusion=> { :in => [‘fulltime’, ‘parttime’, ‘project’] }, :allow_nil => true

# Internally, we store records as a GigOpportunityMetum object.  These are unique based on website.


# `old_job_listing?` and `low_quality_keywords_present?` are methods that we should just move directly into the API
