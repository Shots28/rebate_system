# REVIEW SYSTEM 777

# WIX 
    # DEAL CREATION
        # Upon submission of a form
        # It checks if the user is the admin
        # And the special test code
        # Then it retrieves the data from the hidden fields
        # Initializes the data in the database and everything
    # DEAL SELECTION
        # WIX API: When user selects a deal, they actually send a wix form
        # The wix form triggers Zapier
        # From the form, as hidden fields
        # Zapier recognizes the SKU
        # Recognizes the email of the user
        # Recognizes the keywords
        # Recognizes the frequency
        # Recognizes the count per day
        # Recognizes the final date of rebate
        # Recognizes the marketplace
        # Recognizes the product SKU
        # Retrieves from a database/GSheets the count of emails already sent
        # If it's not past the final date and under the count of the day
        # KLAVIYO API: Sends an email to the user using a template with the keywords to use, product info, etc
        # Creates in a database/GSheets the user that received a deal and the SKU
            # Otherwise, sends an error notification
    # PURCHASE VERIFICATION
        # WIX API: Wix form submitted by user sends a webhook as a trigger in Zapier, webhook contains form data
        # ZAPIER: Receives the form data
        # Recognizes the SKU from the form
        # Recognizes the Order ID input from the user
        # Recognizes the user from Wix
        # Looks up in database/GSheets that the user was sent a deal
        # Looks up in database/GSheets that the SKU is correct
        # Looks up the Amazon order ID if it exists
        # Confirms the SKU in Amazon order and the Wix form are the same
        # Generates a refund with Seller.tools API
        # Notifies the user of the refund
            # Otherwise, sends a Klaviyo notification of an error
