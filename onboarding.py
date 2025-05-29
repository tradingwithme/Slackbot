def onboarding_path(user_profile):
    """
    Determines the onboarding path based on the user's profile.
    
    Args:
        user_profile (dict): A dictionary containing user profile information.
        
    Returns:
        str: The onboarding path for the user.
    """
    if user_profile.get('role') == 'new': return "Welcome! Let's start with the basics."'
    elif user_profile.get('role') == 'advanced': return "Great! We'll tailor insights to your expertise."
    else: return "Let's get started with leadership coaching."
