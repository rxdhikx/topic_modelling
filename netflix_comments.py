import pandas as pd
from transformers import pipeline
from collections import defaultdict
import torch
from tqdm import tqdm
import numpy as np
import json
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# [Previous InstagramPostAnalyzer class remains the same]

def generate_analysis_report(results: List[Dict], output_dir: str = "analysis_output"):
    """Generate comprehensive analysis reports"""
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Initialize DataFrames for different aspects
    topic_data = []
    sentiment_data = []
    engagement_data = []
    
    for post_analysis in results:
        sheet_name = post_analysis['sheet']
        
        # Topic analysis
        for topic, percentage in post_analysis['comments_analysis']['topics'].items():
            topic_data.append({
                'Sheet': sheet_name,
                'Topic': topic,
                'Percentage': percentage
            })
        
        # Sentiment analysis
        sentiment_data.append({
            'Sheet': sheet_name,
            'Positive_Sentiment': post_analysis['comments_analysis']['sentiment']['positive_percentage'],
            'Total_Comments': post_analysis['comments_analysis']['total_comments'],
            'Emoji_Usage': post_analysis['comments_analysis']['emoji_usage']['emoji_usage_percentage']
        })
        
    # Create DataFrames
    topic_df = pd.DataFrame(topic_data)
    sentiment_df = pd.DataFrame(sentiment_data)
    
    # Save to Excel with multiple sheets
    with pd.ExcelWriter(f"{output_dir}/analysis_report_{timestamp}.xlsx") as writer:
        topic_df.to_excel(writer, sheet_name='Topic Analysis', index=False)
        sentiment_df.to_excel(writer, sheet_name='Sentiment Analysis', index=False)
        
    # Generate visualizations
    plt.figure(figsize=(12, 6))
    sns.barplot(data=topic_df, x='Percentage', y='Topic')
    plt.title('Topic Distribution Across All Comments')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/topic_distribution_{timestamp}.png")
    plt.close()
    
    # Generate JSON report
    report = {
        'analysis_timestamp': timestamp,
        'overall_statistics': {
            'total_posts_analyzed': len(results),
            'average_sentiment': sentiment_df['Positive_Sentiment'].mean(),
            'average_emoji_usage': sentiment_df['Emoji_Usage'].mean()
        },
        'detailed_results': results
    }
    
    with open(f"{output_dir}/detailed_report_{timestamp}.json", 'w') as f:
        json.dump(report, f, indent=2)
    
    return report

def main(file_path: str):
    analyzer = InstagramPostAnalyzer()
    print("Loading data from Excel file...")
    posts_data = analyzer.load_excel_data(file_path)
    
    results = []
    for post_data in posts_data:
        analysis = analyzer.analyze_post(post_data)
        results.append(analysis)
        
        # Print immediate results
        print(f"\n=== Results for {post_data['sheet']} ===")
        print("\nTop Topics in Comments:")
        sorted_topics = sorted(
            analysis['comments_analysis']['topics'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]  # Top 5 topics
        
        for topic, percentage in sorted_topics:
            print(f"{topic}: {percentage:.1f}%")
            
        print(f"\nEngagement Statistics:")
        print(f"Total Comments: {analysis['comments_analysis']['total_comments']}")
        print(f"Positive Sentiment: {analysis['comments_analysis']['sentiment']['positive_percentage']:.1f}%")
        print(f"Emoji Usage: {analysis['comments_analysis']['emoji_usage']['emoji_usage_percentage']:.1f}%")
    
    # Generate comprehensive report
    report = generate_analysis_report(results)
    return report

if __name__ == "__main__":
    file_path = "Miquela Instagram Post_clean data.xlsx"
    results = main(file_path)
