def send_job_listings_to_codeforcash(listings):
    data_to_send_in_request_body = {
        'title': listings[0]['title'],
        'website': listings[0]['link'],
        'description': listings[0]['snippet'],
    }
    return requests.post(data=data_to_send_in_request_body)

send_job_listings_to_codeforcash()