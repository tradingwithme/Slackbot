from pandas import DataFrame

def generate_dashboard():
    """
    Generates a dashboard for displaying data.
    
    Returns:
        DataFrame: A DataFrame containing the dashboard data.
    """
    # Sample data for the dashboard
    data = DataFrame({
        'User': ['Alice', 'Bob', 'Charlie'],
        'Sentiment': ['Positive', 'Negative', 'Neutral'],
        'Score': [0.8, -0.5, 0.0],
        'Comments': [
            'Great job on the project!',
            'I am not satisfied with the results.',
            'The outcome was as expected.'
        ]})
    print(data)
    
generate_dashboard()
