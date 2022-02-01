"""# SAM
# DEAL CREATION
    # User creates a WIX page with:
    # SKU, KEYWORDS, COUNT/DAY, FINAL DATE, 
    # Upon submission of a form

    # As of right now it can't initialize our variables
    # It checks if the user is the admin
    # And the special test code
    # Then it retrieves the data from the hidden fields
    # Initializes the data in the database and everything
# MISC
    # Needs to initialize the count of deals sent in a zapier storage variable
    # Needs to reset it every day
    
# Sends emails with new deals, with a link to the submission page for users to accept deals
"""

# DANIEL
# DEAL SELECTION
    # WIX API sends webhook to Zapier upon form submission in WIX PAGE 1
    # Form needs to contain some hidden fields to identify the deal submitted/accepted by the user
    # Zapier code step retrieves the following:
        # Deal SKU
        # Deal keywords
        # Deal count per day
        # Deal final date of rebate
        # Deal marketplace (AMZ/WALMART)
        # Wix user's email & other info 
    # Zapier STORAGE 1 step adds a count to a variable containing the number of people who received the deal today
    # In code, compare the zapier storage variable to the count per day defined in the Wix form
    # If it's not past the final date and under the total count per day
    # Then Klavyio API is used to send an email to the user, reusing the email retrieved
    # The email generated uses a template that is filled out with the SKU, keywords, etc
    # Zapier adds the user to a STORAGE 2 variable with a value saying the deal has been accepted but not redeemed
    # Sends an email with a link to WIX PAGE 2 for order verification
# PURCHASE VERIFICATION
    # WIX API: Wix form submitted from WIX PAGE 2 by user sends a webhook as a trigger in Zapier, webhook contains form data
    # ZAPIER: Receives the form data
    # Recognizes the SKU from the form
    # Recognizes the Order ID input from the user
    # Recognizes the user from Wix
    # Looks up in zapier STORAGE 2 if the user was assigned a deal
    # Looks up in zapier STORAGE 3 that the SKU is an active deal
    # Looks up the Amazon order ID if it exists
    # Confirms the SKU in Amazon order and the Wix form are the same
    # Generates a refund with Seller.tools API
    # Notifies the user of the refund
# REPORTING SYSTEM
    # Zapier daily retrieves the storage variables for each deal, the number of users who accepted the deal
    # The number of users who redeemed the deal
    # Sends an email with that information
