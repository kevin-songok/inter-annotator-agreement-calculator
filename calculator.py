def calculate_cohens_kappa(annotator1, annotator2):
    """
    Calculates Cohen's Kappa score to measure inter-annotator agreement 
    for categorical data labeling.
    """
    if len(annotator1) != len(annotator2):
        raise ValueError("Both annotators must have labeled the same number of items.")

    # Get unique categories/labels used
    categories = list(set(annotator1 + annotator2))
    n = len(annotator1)
    
    # 1. Calculate Observed Agreement (Po)
    agreements = sum(1 for a, b in zip(annotator1, annotator2) if a == b)
    po = agreements / n

    # 2. Calculate Chance Agreement (Pe)
    pe = 0
    for cat in categories:
        count1 = annotator1.count(cat)
        count2 = annotator2.count(cat)
        
        prob1 = count1 / n
        prob2 = count2 / n
        
        pe += (prob1 * prob2)

    # 3. Calculate Kappa
    if pe == 1:
        return 1.0  # Perfect agreement handling
    
    kappa = (po - pe) / (1 - pe)
    return round(kappa, 4)

def interpret_kappa(kappa_score):
    """Provides a standard framework interpretation of the Kappa score."""
    if kappa_score < 0:
        return "Poor Agreement (Less than chance)"
    elif kappa_score <= 0.20:
        return "Slight Agreement"
    elif kappa_score <= 0.40:
        return "Fair Agreement"
    elif kappa_score <= 0.60:
        return "Moderate Agreement"
    elif kappa_score <= 0.80:
        return "Substantial Agreement"
    else:
        return "Almost Perfect Agreement"

# Example Evaluation Simulation
if __name__ == "__main__":
    print("--- AI Data Quality Control: Inter-Annotator Agreement Test ---")
    
    # Simulating data labels applied by two different annotators on 10 images
    # Labels: 'Positive', 'Negative', 'Neutral'
    labels_worker_A = ['Positive', 'Negative', 'Positive', 'Neutral', 'Positive', 'Negative', 'Neutral', 'Positive', 'Positive', 'Negative']
    labels_worker_B = ['Positive', 'Negative', 'Neutral',  'Neutral', 'Positive', 'Negative', 'Neutral', 'Positive', 'Negative', 'Negative']

    score = calculate_cohens_kappa(labels_worker_A, labels_worker_B)
    interpretation = interpret_kappa(score)

    print(f"Calculated Cohen's Kappa Score: {score}")
    print(f"Data Reliability Status: {interpretation}")
