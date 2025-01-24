from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import boto3
import botocore

app = Flask(__name__)
CORS(app)

# AWS credentials - Replace with your own or use AWS CLI configuration
AWS_ACCESS_KEY = 'your-access-key'
AWS_SECRET_KEY = 'your-secret-key'
AWS_REGION = 'your-region'  # e.g., 'us-east-1'

comprehend = boto3.client('comprehend',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def analyze_persian_sentiment(text):
    try:
        response = comprehend.detect_sentiment(
            Text=text,
            LanguageCode='fa'  # Persian/Farsi language code
        )
        
        sentiment_score = {
            'POSITIVE': 1,
            'NEGATIVE': -1,
            'NEUTRAL': 0,
            'MIXED': 0
        }
        
        score = sentiment_score.get(response['Sentiment'], 0)
        
        sentiment_mapping = {
            'POSITIVE': "مثبت",
            'NEGATIVE': "منفی",
            'NEUTRAL': "خنثی",
            'MIXED': "ترکیبی"
        }
        
        sentiment = sentiment_mapping.get(response['Sentiment'], "نامشخص")
        
        return {
            "sentiment": sentiment,
            "score": score,
            "confidence_scores": response['SentimentScore'],
            "raw_response": response
        }
        
    except botocore.exceptions.ClientError as e:
        print(f"Error in AWS Comprehend API: {str(e)}")
        return {
            "sentiment": "خطا",
            "score": 0,
            "error": str(e)
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()
        feedback_text = data.get('text')
        
        if not feedback_text:
            return jsonify({'success': False, 'error': 'No text provided'}), 400
            
        result = analyze_persian_sentiment(feedback_text)
        
        if 'error' in result:
            return jsonify({'success': False, 'error': result['error']}), 500
            
        return jsonify({'success': True, 'result': result})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)