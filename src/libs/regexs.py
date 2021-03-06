to_match = [
    {'match_regex': 'password', 'match_type': 'Password'},
    {'match_regex': '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3,}', 'match_type': 'IP'},
    {'match_regex': 'username', 'match_type': 'Username'},
    {'match_regex': '([A-Za-z0-9._%%+-]+[a-zA-Z0-9])@([A-Za-z0-9.-]+[a-zA-Z0-9])\.([A-Za-z]{2,})', 'match_type': 'Email'},
    {'match_regex': '(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16,}', 'match_type': "AWS Client ID"},
    {'match_regex': '(?i)aws(.{0,20})\?[\\\'\\\"][0-9a-zA-Z\/+]{40,}[\\\'\\\"]', 'match_type': "AWS Secret Key"},
    {'match_regex': 'amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12,}', 'match_type': "AWS MWS key"},
    {'match_regex': '\-\-\-\-\-BEGIN PRIVATE KEY\-\-\-\-\-', 'match_type': "PKCS8"},
    {'match_regex': '\-\-\-\-\-BEGIN RSA PRIVATE KEY\-\-\-\-\-', 'match_type': "RSA"},
    {'match_regex': '\-\-\-\-\-BEGIN OPENSSH PRIVATE KEY\-\-\-\-\-', 'match_type': "SSH"},
    {'match_regex': '\-\-\-\-\-BEGIN PGP PRIVATE KEY BLOCK\-\-\-\-\-', 'match_type': "PGP"},
    {'match_regex': '(?i)(facebook|fb)(.{0,20})?[\\\'\\\"][0-9a-f]{32,}[\\\'\\\"]', 'match_type': "Facebook Secret Key"},
    {'match_regex': '(?i)(facebook|fb)(.{0,20})?[\\\'\\\"][0-9]{13,17}[\\\'\\\"]', 'match_type': "Facebook Client ID"},
    {'match_regex': '[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*[\\\'|\\\"][0-9a-f]{32,}[\\\'|\\\"]', 'match_type': "Facebook Oauth"},
    {'match_regex': 'EAACEdEose0cBA[0-9A-Za-z]+', 'match_type': "Facebook access token"},
    {'match_regex': '(?i)twitter(.{0,20})?[\\\'\\\"][0-9a-z]{35,44}[\\\'\\\"]', 'match_type': "Twitter Secret Key"},
    {'match_regex': '(?i)twitter(.{0,20})?[\\\'\\\"][0-9a-z]{18,25}[\\\'\\\"]', 'match_type': "Twitter Client ID"},
    {'match_regex': '[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}[\\\'\\\"\\s][0-9a-zA-Z]{35,44}[\\\'\\\"\\s]', 'match_type': "Twitter Oauth"},
    {'match_regex': '(?i)github(.{0,20})?[\\\'\\\"][0-9a-zA-Z]{35,40}[\\\'\\\"]', 'match_type': "Github"},
    {'match_regex': '(?i)linkedin(.{0,20})?[\\\'\\\"][0-9a-z]{12,}[\\\'\\\"]', 'match_type': "LinkedIn Client ID"},
    {'match_regex': '(?i)linkedin(.{0,20})?[\\\'\\\"][0-9a-z]{16,}[\\\'\\\"]', 'match_type': "LinkedIn Secret Key"},
    {'match_regex': 'xox[baprs]-([0-9a-zA-Z]{10,48})?', 'match_type': "Slack"},
    {'match_regex': '\-\-\-\-\-BEGIN EC PRIVATE KEY\-\-\-\-\-', 'match_type': "EC"},
    {'match_regex': '(?i)api_key(.{0,20})?[\\\'|\\\"][0-9a-zA-Z]{32,45}[\\\'|\\\"]', 'match_type': "Generic API key"},
    {'match_regex': '(?i)secret(.{0,20})?[\\\'|\\\"][0-9a-zA-Z]{32,45}[\\\'|\\\"]', 'match_type': "Generic Secret"},
    {'match_regex': 'AIza[0-9A-Za-z\\\-\_]{35,}', 'match_type': "Google API key"},
    {'match_regex': '(?i)(google|gcp|youtube|drive|yt)(.{0,20})?[\\\'\\\"][AIza[0-9a-z\\\-\_]{35,}][\\\'\\\"]', 'match_type': "Google Cloud Platform API key"},
    {'match_regex': '(?i)(google|gcp|auth)(.{0,20})?[\\\'\\\"][0-9]+-[0-9a-z_]{32,}\.apps\.googleusercontent\.com[\\\'\\\"]', 'match_type': "Google OAuth"},
    {'match_regex': 'ya29\.[0-9A-Za-z\-_]+', 'match_type': "Google OAuth access token"},
    {'match_regex': '(?i)heroku(.{0,20})?[\\\'\\\"][0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}[\\\'\\\"]', 'match_type': "Heroku API key"},
    {'match_regex': '(?i)(mailchimp|mc)(.{0,20})?[\\\'\\\"][0-9a-f]{32,}-us[0-9]{1,2}[\\\'\\\"]', 'match_type': "MailChimp API key"},
    {'match_regex': '(?i)(mailgun|mg)(.{0,20})?[\\\'\\\"][0-9a-z]{32,}[\\\'\\\"]', 'match_type': "Mailgun API key"},
    {'match_regex': '[a-zA-Z]{3,10}:\/\/[^\/\s:@]{3,20}:[^\/\s:@]{3,20}@.{1,100}\/?.?', 'match_type': "Password in URL"},
    {'match_regex': 'access_token\$production\$[0-9a-z]{16,}\$[0-9a-f]{32,}', 'match_type': "PayPal Braintree access token"},
    {'match_regex': 'sk_live_[0-9a-z]{32,}', 'match_type': "Picatic API key"},
    {'match_regex': 'https\:\/\/hooks.slack.com\/services\/T[a-zA-Z0-9_]{8}\/B[a-zA-Z0-9_]{10,}\/[a-zA-Z0-9_]{24,}', 'match_type': "Slack Webhook"},
    {'match_regex': '(?i)stripe(.{0,20})?[\\\'\\\"][sk|rk]_live_[0-9a-zA-Z]{24,}', 'match_type': "Stripe API key"},
    {'match_regex': 'sq0atp-[0-9A-Za-z\-_]{22,}', 'match_type': "Square access token"},
    {'match_regex': 'sq0csp-[0-9A-Za-z\\-_]{43,}', 'match_type': "Square OAuth secret"},
    {'match_regex': '(?i)twilio(.{0,20})?[\\\'\\\"][0-9a-f]{32,}[\\\'\\\"]', 'match_type': "Twilio API key"}
    ]