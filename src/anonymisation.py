def check_k_anonymity(df, quasi_identifiers, k):
    """
    Check k-anonymity of a DataFrame.
    
    Parameters:
    - df: DataFrame containing the dataset.
    - quasi_identifiers: List of column names that act as quasi-identifiers.
    - k: Minimum desired count of each unique combination of quasi-identifiers.
    
    Returns:
    - Boolean indicating whether the dataset satisfies k-anonymity.
    """
    # Group by quasi-identifiers and count occurrences
    grouped = df.groupby(quasi_identifiers).size()
    
    # Check if any group has less than k occurrences
    if any(grouped < k):
        print(f"The dataset does not satisfy {k}-anonymity.")
        return False
    else:
        print(f"The dataset satisfies {k}-anonymity.")
        return True
    
def check_l_diversity(df, quasi_identifiers, sensitive_attribute, l):
    """
    Check l-diversity of a DataFrame.
    
    Parameters:
    - df: DataFrame containing the dataset.
    - quasi_identifiers: List of column names that act as quasi-identifiers.
    - sensitive_attribute: Column name of the sensitive attribute.
    - l: Minimum desired distinct values of the sensitive attribute within each group.
    
    Returns:
    - Boolean indicating whether the dataset satisfies l-diversity.
    """
    # Group by quasi-identifiers and sensitive attribute, count distinct values
    grouped = df.groupby(quasi_identifiers)[sensitive_attribute].nunique()
    
    # Check if any group has less than l distinct sensitive attribute values
    if any(grouped < l):
        print(f"The dataset does not satisfy {l}-diversity.")
        return False
    else:
        print(f"The dataset satisfies {l}-diversity.")
        return True
